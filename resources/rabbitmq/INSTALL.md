# Prerequisites

### Enable Prometheus Metrics
Rabbitmq instruments Prometheus metrics and annotates the metrics API pod with Prometheus annotations. 

Make sure that Prometheus metrics are activated. If they are not, activate the plugin using this command inside of the rabbitmq container:

```sh
rabbitmq-plugins enable rabbitmq_prometheus
```
# Installation

The application is ready to be scraped