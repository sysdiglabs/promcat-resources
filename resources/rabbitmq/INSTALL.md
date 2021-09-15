## Enable Prometheus Metrics
Rabbitmq instruments Prometheus metrics and annotates the metrics API pod with Prometheus annotations. 

Make sure that the prometheus metrics are activated. In case you don't have activated the plugin use the next command:

```sh
rabbitmq-plugins enable rabbitmq_prometheus
```
