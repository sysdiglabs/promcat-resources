# Installing the exporter
You will use the [Prometheus Memcached Metrics Exporter](https://github.com/prometheus/memcached_exporter).

The `memcached-exporter-deploy.yaml` file provides a deployment with the exporter.

To deploy it, download the file and run:
```
kubectl apply -f memcached-exporter-deploy.yaml
```
> Make sure to edit the argumment `memcached.address` with the proper address name of your memcached instance

# Sysdig Agent configuration
> Requires Sysdig Agent >= v11.3 

In the Redis exporter Deployment use the Sysdig annotations to configure the port of the exporter as the scraping port. See the example given in the `memcached-exporter-deploy.yaml` file.

Additionally, you can use the labels to add the namespace, workload type, and name of the database the exporter will take data from.
This way, you can view the metrics associated directly with the database pods and the exporter in Sysdig Monitor.

```yaml
spec:
  template:
    metadata:
      annotations:
        promcat.sysdig.com/integration_type: memcached
        promcat.sysdig.com/port: "9150"
        # Add here the namespace, workload type (deployment, statefulset, replicaset, daemonset)
        # and workload name of the Memcached instance that the exporter will take data from
        promcat.sysdig.com/target_ns: default
        promcat.sysdig.com/target_workload_type: deployment
        promcat.sysdig.com/target_workload_name: memcached
```

After configuring the Sysdig annotations, download the sample configuration file and apply it by:
```bash
kubectl apply -f sysdig-agent-config.yaml
```
