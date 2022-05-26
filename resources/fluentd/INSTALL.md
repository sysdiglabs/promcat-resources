# Prerequisites
Fluentd instruments Prometheus metrics and annotates the pods with Prometheus annotations. 

For Fluentd to expose Prometheus metrics, the following plugins need to be enabled:
- 'prometheus' input plugin
- 'prometheus_monitor' input plugin
- 'prometheus_output_monitor' input plugin

As seen in the official plugin documentation (https://github.com/fluent/fluent-plugin-prometheus/blob/master/README.md), they can be enabled with the following configurations:
```
<source>
    @type prometheus
    @id in_prometheus
    bind "0.0.0.0"
    port 24231
    metrics_path "/metrics"
</source>

<source>
    @type prometheus_monitor
    @id in_prometheus_monitor
</source>

<source>
    @type prometheus_output_monitor
    @id in_prometheus_output_monitor
</source>
```

If you are deploying Fluentd using the official Helm chart (https://github.com/fluent/helm-charts/tree/main/charts/fluentd), it already has these plugins enabled by default in its configuration, so no additional actions are needed.