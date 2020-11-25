# Prerequisites
## Mount the etcd certificates in the sysdig agent
```sh
kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"volumes":[{"hostPath":{"path":"/etc/kubernetes/pki/etcd-manager-main","type":"DirectoryOrCreate"},"name":"etcd-certificates"}]}}}}'
  
kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"containers":[{"name":"sysdig-agent","volumeMounts": [{"mountPath": "/etc/kubernetes/pki/etcd-manager","name": "etcd-certificates"}]}]}}}}'
```

## Configuring the Sysdig agent
In this section we will explain how to configure the sysdig-agent

In order to get these metrics you have to enable promscrape v2 to do so make sure your dragent.yaml has these values
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

You will get an example of the `sysdig-agent.yaml` below

With the promscrape v2 enable you have to scrape the etcd, so just make sure in your `sysdig-agent.yaml` has the prometheus job like for example this
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
Like before you will see the example below