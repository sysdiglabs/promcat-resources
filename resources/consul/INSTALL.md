# Prerequisites
Consul instruments Prometheus metrics and annotates the pods with Prometheus annotations. 

As seen in Consul documentation pages (https://www.consul.io/docs/k8s/helm#v-global-metrics and https://www.consul.io/docs/agent/options#telemetry-prometheus_retention_time), to make Consul expose an endpoint for scraping metrics, you need to enable a few global.metrics configurations.
You also need to enable the telemetry.disable_hostname "extra configurations" in the Consul Server and Client, so the metrics don't contain the name of the instances.

If you install Consul with Helm, you need to use the following flags:
```
--set 'global.metrics.enabled=true'
--set 'global.metrics.enableAgentMetrics=true'
--set 'server.extraConfig="{"telemetry": {"disable_hostname": true}}"'
--set 'client.extraConfig="{"telemetry": {"disable_hostname": true}}"'
```
