# Prerequisites
In order to get access to the tables you should create a user with the right permissions or use one with the right permissions.

# Installing the exporter
To deploy the [SQL Exporter](https://github.com/free/sql_exporter) you have to deploy the deployment that is specified below or the image in your cluster or machine.

To configure the exporter in your Kubernetes deployment, you can install the deployment with a configmap and write the username and password as given below:

```yaml
target:
  # Data source name always has a URI schema that matches the driver name. In some cases (e.g. MySQL)
  # the schema gets dropped or replaced to match the driver expected DSN format.
  data_source_name: 'sqlserver://USER:PASSWORD@mssql:1433'
```

The configmap has a `custom-metrics` inside with a series of SLQ queries. You can add more queries to the configmap if required.

# Sysdig Agent configuration
Ensure that the Sysdig Agent configuration includes a job for the specific instance of MsSQL, such as the example given below. In this example, the exporter is deployed in the mssql namespace.

```yaml
scrape_configs:
- job_name: mssql
  tls_config:
    insecure_skip_verify: true
  kubernetes_sd_configs:
  - role: pod
  relabel_configs:
  - action: keep
    source_labels: [__meta_kubernetes_pod_host_ip]
    regex: __HOSTIPS__
  - action: keep
    source_labels:
    - __meta_kubernetes_namespace
    - __meta_kubernetes_pod_name
    separator: '/'
    regex: 'mssql/mssql-exporter.+'
  - source_labels:
    - __address__
    action: replace
    target_label: __address__
    regex: (.+?)(\\:\\d)?
    replacement: $1:9399
    # Holding on to pod-id and container name so we can associate the metrics
    # with the container (and cluster hierarchy)
  - action: replace
    source_labels: [__meta_kubernetes_pod_uid]
    target_label: sysdig_k8s_pod_uid
  - action: replace
    source_labels: [__meta_kubernetes_pod_container_name]
    target_label: sysdig_k8s_pod_container_name
```

You can download the sample configuration file and apply it by:
```bash
kubectl apply -f sysdig-agent.yaml
```
