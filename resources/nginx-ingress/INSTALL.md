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
    prometheus.io/scrape: "true"
    prometheus.io/port: "10254"
```

# Sysdig Agent configuration
For the Sysdig Agent to discover and scrape the ngnix ingress controller automatically, enable the `use_promscrape` option in the agent configuration.

```yaml
  dragent.yaml: |-
    use_promscrape: true
    prometheus:
      enabled: true
      prom_service_discovery: true
```
An example of the Sysdig Agent configuration file is given below.
