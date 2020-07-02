# Prerequisites
Kubernetes generates a high number of metrics for the control plane. As the Sysdig Agent has a limit of timesieres that can send to Sysdig Monitor, you have to deploy a Prometheus server and create the recording rules that we provide. This way, we will filter only the metrics that we need.

To deploy a Prometheus server you will need:
* [helm](https://helm.sh/docs/intro/install/)  
* [helmfile](https://github.com/roboll/helmfile)

## Extracting the SSL certificates to Secrets
Etcd exposes all their metrics by default but Prometheus has to know where it is. 

First, you need to get the SSL certificates.
1. Getting the certificates: 
The certificates are located in the master node in `/etc/kubernetes/pki/etcd-manager-main/etcd-clients-ca.key` and `/etc/kubernetes/pki/etcd-manager-main/etcd-clients-ca.crt`. Save them in you local computer.
2. Creating the secrets for the certificates:
Once we have the certificates let’s proceed to create the secrets in the namespace where the Prometheus server is located. In our case, it will be located in the namespace `monitoring`. 
To create the secrets, run:

```bash
kubectl -n monitoring create secret generic etcd-ca --from-file=etcd-clients-ca.key --from-file etcd-clients-ca.crt
```

# Installing and configuring Prometheus
## Installing a new Prometheus with helm
In this section we will explain how to install and configure a new Prometheus server with the recording rules.  

Download the following files: 
- helmfile.yaml
- recording_rules.yaml
- prometheus.yaml

Execute:

```
helmfile sync
```

## Configuring an existing Prometheus
In this section we will explain how to configure an existing Prometheus server

1. Let’s mount the volume with the certificates

```bash
kubectl -n monitoring patch sts prometheus-server -p '{"spec":{"template":{"spec":{"volumes":[{"name":"etcd-ca","secret":{"defaultMode":420,"secretName":"etcd-ca"}}]}}}}'

kubectl -n monitoring patch sts prometheus-server -p '{"spec":{"template":{"spec":{"containers":[{"name":"prometheus-server","volumeMounts": [{"mountPath": "/opt/draios/kubernetes/prometheus/secrets","name": "etcd-ca"}]}]}}}}'
```

2. Add the job to Prometheus:
To have the Prometheus scrapping the etcd endpoint it is necessary to add a job.  Add this to the job part in the ConfigMap of Prometheus, inside of `scrape_configs`.
You can download the file `prometheus-cm.yaml` with all jobs for kubernetes control plane as a reference.

```
kubectl -n monitoring edit cm prometheus-server
```

```yaml
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

# Configuring the Sysdig Agent
In order to get the metrics in Sysdig the agent has to federate the Prometheus.

If we choose to filter the metrics, it will save a lot of useless metrics with debugging in the name. If you want to avoid this, just apply the rules and you only 
will get the metrics that you need to have the dashboards and alerts working.

To install the rules just apply this commands:

```bash 
kubectl apply -f etcd-rules.yaml

kubectl -n monitoring patch deployment prometheus-server -p '{"spec":{"template":{"spec":{"volumes":[{"name":"etcd-rules","configMap":{"defaultMode":420,"name":"etcd-rules"}}]}}}}'

kubectl -n monitoring patch deployment prometheus-server -p '{"spec":{"template":{"spec":{"containers":[{"name":"prometheus-server","volumeMounts": [{"mountPath": "/opt/rules","name": "etcd-rules"}]}]}}}}'
```

To federate the Prometheus just add the `prometheus.yaml` to the configuration, as it is done in the `sysdig-agent-example.yaml` file:

```yaml
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

Copy the agent configuration provided and save it as `sysdig-agent.yaml`. Then apply it:

```bash
kubectl apply -f sysdig-agent.yaml
```