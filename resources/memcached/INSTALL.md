# Installing the exporter
You will use the [Prometheus Memcached Metrics Exporter](https://github.com/prometheus/memcached_exporter).

The `memcached-exporter-deploy.yaml` file provides a deployment with the exporter.

To deploy it, download the file and run:
```
kubectl apply -f memcached-exporter-deploy.yaml
```
> Make sure to edit the argumment `memcached.address` with the proper address name of your memcached instance
