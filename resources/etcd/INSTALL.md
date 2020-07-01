  # Configuring the etcd to get the metrics
  Etcd exposes all their metrics by default but the Prometheus has to know where it is and also the metrics have to be gathered with SSL, so we need to get the certificates first.
  1. Getting the certificates
    The certificates are located in the master node in `/etc/kubernetes/pki/etcd-manager-main/etcd-clients-ca.key` and `/etc/kubernetes/pki/etcd-manager-main/etcd-clients-ca.crt`
    Let's get them and save it to create the secrets after
  2. Creating the secrets for the certificates
    Once we have the certificates let’s proceed to create the secrets in the namespace where it is the Prometheus server, in our case, it will be located in the namespace monitoring.
    Let's create the secrets
    ```
    kubectl -n monitoring create secret generic etcd-ca --from-file=etcd-clients-ca.key --from-file etcd-clients-ca.crt
    ```
  # One line deployment
  To have all metrics in sysdig and because the limit of the timeseries you have to deploy a Prometheus create the recording rules that we later will use to filter only the metrics we need
  So to deploy a Prometheus you will need [helm](https://helm.sh/docs/intro/install/) and [helmfile](https://github.com/roboll/helmfile)
  1. Install the helm chart with helm file for Prometheus, you have to download the `helmfile.yaml` and the files for the rules `recording_rules.yaml` 
    and to configure the prometheus `prometheus.yaml`
    ```
    helmfile sync
    ```
  # With your prometheus
  If you have already a prometheus server up and running.
  1. Let’s mount the volume with the certificates
    ```
    kubectl -n monitoring patch sts prometheus-server -p '{"spec":{"template":{"spec":{"volumes":[{"name":"etcd-ca","secret":{"defaultMode":420,"secretName":"etcd-ca"}}]}}}}'
    kubectl -n monitoring patch sts prometheus-server -p '{"spec":{"template":{"spec":{"containers":[{"name":"prometheus-server","volumeMounts": [{"mountPath": "/opt/draios/kubernetes/prometheus/secrets","name": "etcd-ca"}]}]}}}}'
    ```
  2. Add the job to Prometheus
    To have the Prometheus scrapping the etcd endpoint it is necessary to add a job so just add this to the job part in the configmap of Prometheus inside of scrape_configs.
    You have a configmap for download with all jobs for kubernetes control plane if you want it and as reference.
    ```
    kubectl -n monitoring edit cm prometheus-server
    ```
    ```
    scrape_configs:
    ...
    - job_name: etcd
      scheme: https
      kubernetes_sd_configs:
      - role: pod
      relabel_configs:
      - action: keep
        source_labels:
        - __meta_kubernetes_namespace
        - __meta_kubernetes_pod_name
        separator: '/'
        regex: 'kube-system/etcd-manager-main.+'
      - source_labels:
        - __address__
        action: replace
        target_label: __address__
        regex: (.+?)(\\:\\d)?
        replacement: $1:4001
      tls_config:
        insecure_skip_verify: true
        cert_file: /opt/draios/kubernetes/prometheus/secrets/etcd-clients-ca.crt
        key_file: /opt/draios/kubernetes/prometheus/secrets/etcd-clients-ca.key
    ```
    
  # Sysdig Agent configuration, Federating the Prometheus
    In order to get the metrics in Sysdig the agent has to federate the Prometheus as do in the Kubernetes control plane so let's go to the Sysdig agent configuration part.

    If we choose not filtering the metrics will be saving a lot of useless metrics with debugging in the name, so if you want to avoid this just apply the rules and you only 
    will get the metrics you need to have the dashboards and alerts working.
    To install the rules just apply this commands.
    ```
    kubectl apply -f etcd-rules.yaml
    kubectl -n monitoring patch deployment prometheus-server -p '{"spec":{"template":{"spec":{"volumes":[{"name":"etcd-rules","configMap":{"defaultMode":420,"name":"etcd-rules"}}]}}}}'
    kubectl -n monitoring patch deployment prometheus-server -p '{"spec":{"template":{"spec":{"containers":[{"name":"prometheus-server","volumeMounts": [{"mountPath": "/opt/rules","name": "etcd-rules"}]}]}}}}'
    ```
    For federate the Prometheus just add the prometheus.yaml to the configuration of sysdig-agent.yaml
    ```
    prometheus.yaml: |-
    global:
      scrape_interval: 15s
      evaluation_interval: 15s
    scrape_configs:
    - job_name: 'prometheus' # config for federation
      honor_labels: true
      metrics_path: '/federate'
      metric_relabel_configs:
      - regex: 'kubernetes_pod_name'
        action: labeldrop
      params:
        'match[]':
          - '{sysdig="true"}'
      sysdig_sd_configs:
      - tags:
          namespace: monitoring
          deployment: prometheus-server
    ```