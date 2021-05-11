# Installing the exporter
Nginx ingress controller is already instrumented so you don't have to add any extra exporter. However, ensure that your nginx ingress controller is already exposing these metrics.

For exmaple if you are deploying your nginx ingress controller with helm, make sure you have these values.

```yaml
controller:
  metrics:
    port: 10254
    # if this port is changed, change healthz-port: in extraArgs: accordingly
    enabled: true
  podAnnotations:
    promcat.sysdig.com/port: "10254"
```

# Sysdig Agent configuration
For the Sysdig Agent to discover and scrape the ngnix ingress controller automatically, enable the `use_promscrape` option in the agent configuration.

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
An example of the Sysdig Agent configuration file is given below.
