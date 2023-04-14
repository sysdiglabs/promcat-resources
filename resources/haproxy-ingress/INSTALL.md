# Prerequisites


### Enable Prometheus Metrics
For HAProxy to expose Prometheus metrics, the following options must be enabled:
- controller.metrics.enabled = true	
- controller.stats.enabled = true

You can check all the properties in the [official web page](https://github.com/haproxy-ingress/charts/blob/release-0.13/haproxy-ingress/README.md#configuration).

If you are deploying HAProxy using the [official Helm chart](https://github.com/haproxytech/helm-charts/tree/main/kubernetes-ingress), they can be enabled with the following configurations:

```
helm install haproxy-ingress haproxy-ingress/haproxy-ingress \
--set-string "controller.stats.enabled = true" \
--set-string "controller.metrics.enabled = true"
```

This configuration creates the following section in haproxy.cfg file

```
frontend prometheus
    mode http
    bind :9101
    http-request use-service prometheus-exporter if { path /metrics }
    http-request use-service lua.send-prometheus-root if { path / }
    http-request use-service lua.send-404
    no log
```# Installation

The application is ready to be scraped