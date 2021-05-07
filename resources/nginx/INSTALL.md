# Installing the exporter
The exporter can be installed as a sidecar of the pod with the Nginx server. You can find a deployment below with the exporter as a sidecar and the configmap with the configuration required to scrape metrics from the server.

Note that the deployment has a label, `app`. This label will be included in the metrics to be able to use it as a variable in the dashboards and alerts.

# Sysdig Agent configuration
In the Sysdig Agent configuration, add the following snippet to include the label `app` as a metric label.
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

You can download the sample configuration file below and apply it by:
```bash
kubectl apply -f sysdig-agent-config.yaml
```
