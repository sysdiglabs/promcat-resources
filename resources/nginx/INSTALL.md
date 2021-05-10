# Installing the exporter
The exporter can be installed as a sidecar of the pod with the Nginx server. You can find a deployment below with the exporter as a sidecar and the configmap with the configuration required to scrape metrics from the server.

Note that the deployment has a label, `app`. This label will be included in the metrics to be able to use it as a variable in the dashboards and alerts.

# Sysdig Agent configuration
In the Sysdig Agent configuration, add the following snippet to include the label `app` as a metric label.
```yaml
  dragent.yaml: |-
    metrics_excess_log: true
    k8s_cluster_name: YourClusterName
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

You can download the sample configuration file below and apply it by:
```bash
kubectl apply -f sysdig-agent-config.yaml
```
