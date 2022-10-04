# Installing the exporter
Nginx ingress controller is already instrumented so you don't have to add any extra exporter. However, ensure that your nginx ingress controller is already exposing these metrics. Don't forget to include the `prometheus.io/port` and `prometheus.io/scrape` annotations.

For example if you are deploying your nginx ingress controller using the helm chart from Kubernetes, the values would be:

```yaml
controller:
  metrics:
    port: 10254
    enabled: true
  podAnnotations:
    prometheus.io/port: "10254"
    prometheus.io/scrape: "true"
```
