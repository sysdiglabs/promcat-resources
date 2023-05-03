# Prerequisites

### Enable Prometheus Metrics
Keda instruments Prometheus metrics and annotates the metrics API pod with Prometheus annotations. 

Make sure that the prometheus metrics are activated. If you install Keda with Helm you need to use the following flag:
```
--set prometheus.metricServer.enabled=true
```

# Installation

The application is ready to be scraped