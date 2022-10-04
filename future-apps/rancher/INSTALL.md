# Prerequisites
## Enable monitoring
Rancher can deploy a Prometheus server. To get a default monitoring you have to enable it in the monitoring tab.
## Mount the etcd certificates in the sysdig agent
```sh
kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"volumes":[{"hostPath":{"path":"/etc/kubernetes/pki/etcd-manager-main","type":"DirectoryOrCreate"},"name":"etcd-certificates"}]}}}}'

kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"containers":[{"name":"sysdig-agent","volumeMounts": [{"mountPath": "/etc/kubernetes/pki/etcd-manager","name": "etcd-certificates"}]}]}}}}'
```
# Gather the metrics from the prometheus deployed by Rancher
For the control plane metrics, the services are not created by default. To get them in the Prometheus server you have to create new services and seviceMonitors. To gather that metrics with the Sysdig agent, you have to create the rules to filter them, and then federate the metrics with the agent itself.

You can either follow the steps given below or download the script and execute:
```sh
sh installation.sh
```
And then apply the configuration changes for the `sysdig-agent`.

1. Apply the services:
```bash
kubectl apply -f services.yaml
```
2. Apply the serviceMonitor:
```bash
kubectl apply -f service-monitor.yaml
```
## Configuring the Sysdig Agent

In order to collect the metrics you have to enable `promscrape_fastproto` to do. Therefore, ensure that your `dragent.yaml` includes the following values:
```yaml
metrics_excess_log: true
k8s_cluster_name: yourClusterName
10s_flush_enable: true
app_checks_enabled: false
use_promscrape: true
new_k8s: true
promscrape_fastproto: true
prometheus:
  enabled: true
  prom_service_discovery: true
  log_errors: true
  max_metrics: 200000
  max_metrics_per_process: 200000
  max_tags_per_metric: 100
  ingest_raw: true
  ingest_calculated: false
```

See the example `sysdig-agent.yaml` file given below:

With the promscrape v2 enabled you can scrape the etcd. To do so, ensure that your `sysdig-agent.yaml` includes the prometheus job as given below:
```yaml
- job_name: etcd
  scheme: https
  tls_config:
    insecure_skip_verify: true
    cert_file: /etc/kubernetes/pki/etcd-manager/etcd-clients-ca.crt
    key_file: /etc/kubernetes/pki/etcd-manager/etcd-clients-ca.key
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
    regex: 'kube-system/etcd-manager-main.+'
  - source_labels:
    - __address__
    action: replace
    target_label: __address__
    regex: (.+?)(\\:\\d)?
    replacement: $1:4001
    # Holding on to pod-id and container name so we can associate the metrics
    # with the container (and cluster hierarchy)
  - action: replace
    source_labels: [__meta_kubernetes_pod_uid]
    target_label: sysdig_k8s_pod_uid
  - action: replace
    source_labels: [__meta_kubernetes_pod_container_name]
    target_label: sysdig_k8s_pod_container_name
```
Additionally, you will need a job corresponding to the control plane:
```yaml
- job_name: control-plane
  honor_labels: true
  metrics_path: '/federate'
  params:
    'match[]':
      - '{sysdig="true"}'
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
    regex: 'cattle-prometheus/prometheus-cluster-monitoring-0'
  - source_labels:
    - __address__
    action: replace
    target_label: __address__
    regex: (.+?)(\\:\\d)?
    replacement: $1
    # Holding on to pod-id and container name so we can associate the metrics
    # with the container (and cluster hierarchy)
  - action: replace
    source_labels: [__meta_kubernetes_pod_uid]
    target_label: sysdig_k8s_pod_uid
  - action: replace
    source_labels: [__meta_kubernetes_pod_container_name]
    target_label: sysdig_k8s_pod_container_name
```

See the examples below.

3. Apply the rules:
```
kubectl apply -f rules.yaml
```
4. Apply the sysdig configuration:
```
kubectl apply -f sysdig-agent.yaml
```
