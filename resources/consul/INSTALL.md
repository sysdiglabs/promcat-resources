# Prerequisites


### Enable Prometheus Metrics and Disable Hostname in Metrics
As seen in Consul documentation pages [Helm Global Metrics](https://www.consul.io/docs/k8s/helm#v-global-metrics) and [Prometheus Retention Time](https://www.consul.io/docs/agent/options#telemetry-prometheus_retention_time), to make Consul expose an endpoint for scraping metrics, you need to enable a few global.metrics configurations.
You also need to enable the telemetry.disable_hostname "extra configurations" in the Consul Server and Client, so the metrics don't contain the name of the instances.

If you install Consul with Helm, you need to use the following flags:
```
--set 'global.metrics.enabled=true'
--set 'global.metrics.enableAgentMetrics=true'
--set 'server.extraConfig="{"telemetry": {"disable_hostname": true}}"'
--set 'client.extraConfig="{"telemetry": {"disable_hostname": true}}"'
```# Installation

The application is ready to be scraped