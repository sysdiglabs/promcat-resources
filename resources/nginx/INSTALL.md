# Installing the exporter
The exporter can be installed as a sidecar of the pod with the Nginx server.
Below you can find a deployment with the exporter as a sidecar and the ConfigMap with
the configuration needed to scrape metrics from the server.

Also note that the Deployment has a label 'app'. This label will be included in the metrics
to be able to use it as a variable in the dashboards and alerts.

# Sysdig Agent configuration
In the Sysdig Agent configuration, you have to add the following code to include the label 'app'
as a metric label.
```yaml
process_filter:
  - include:
      kubernetes.pod.annotation.prometheus.io/scrape: true
      conf:
        path: "{kubernetes.pod.annotation.prometheus.io/path}"
        port: "{kubernetes.pod.annotation.prometheus.io/port}"
        tags:
          app: "{kubernetes.pod.label.app}"
```
