# Prerquisites
  To have all metrics in sysdig and because the limit of the timeseries you have to deploy a Prometheus create the recording rules that we later will use to filter only the metrics we need
  So to deploy a Prometheus you will need [helm](https://helm.sh/docs/intro/install/) and [helmfile](https://github.com/roboll/helmfile)

# Installing the prometheus with helm

  To get the metrics follow this steps:

  1. Install the helm chart with helm file for Prometheus, you have to download the `helmfile.yaml` and the files for the rules `recording_rules.yaml` 
    and to configure the prometheus `prometheus.yaml`
    ```
    helmfile sync
    ```
# With your prometheus
  If you have already a prometheus server up and running.
  1. Annotate the statefulset
    ```
    kubectl -n monitoring patch sts prometheus-server -p '{"spec":{"template":{"metadata":{"annotations":{"prometheus.io/scrape": "true", "prometheus.io/port": "9090"}}}}}'
    ```
    Or just apply the deploy yaml provided
     ```
    kubectl -n monitoring apply -f prometheus-deploy.yaml
    ```
  2. Apply the configuration for prometheus, is the configmap prometheus-server, the configuration has the recording rules and the alerts added if we only want
     the prometheus part we have to delete this lines:
    ```
    kubectl -n monitoring edit cm prometheus-server
    ```
    ```
    - /opt/rules/rules.yaml
    - /opt/alerts/alerts.yaml
    ```
    Once we have the file with only the configmap for prometheus we have to apply, if we have save it as prometheus-cm.yaml then execute the next command:
    ```
    kubectl apply -f prometheus-cm.yaml
    ```

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
    ---
    **NOTE**

    If you are using kops, you will have to change the cluster spec to expose the port for the proxy

    ```
    kops --state s3://name-of-s3 --name cluster-name edit cluster
    ```

    And add the follow

    ```
    kubeProxy:
      metricsBindAddress: 0.0.0.0
    ```

    And update the cluster

    ```
    kops --state s3://name-of-s3 --name cluster-name rolling-update cluster --yes
    ```

    ---

  If we want to use the Sysdig agent too, we have to create the recording rules for only scrape the metrics we will use in our dashboards.

  1. Copy the configuration and save it as config.yaml
    ```
    kubectl apply -f sysdig-agent.yaml
    ```