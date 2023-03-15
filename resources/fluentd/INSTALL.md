## Prerequisites

### OpenShift

If you have installed Fluentd using the OpenShift Logging Operator, no further action is required to enable monitoring.

### Kubernetes

#### Enable Prometheus Metrics
For Fluentd to expose Prometheus metrics, enable the following plugins:
- 'prometheus' input plugin
- 'prometheus_monitor' input plugin
- 'prometheus_output_monitor' input plugin

As seen in the [official plugin documentation](https://github.com/fluent/fluent-plugin-prometheus/blob/master/README.md), you can enable them with the following configurations:
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

If you are deploying Fluentd using the [official Helm chart](https://github.com/fluent/helm-charts/tree/main/charts/fluentd), it already has these plugins enabled by default in its configuration, so no additional actions are needed.


## Installation

You can use our helm-charts in order to install the exporter in your cluster.