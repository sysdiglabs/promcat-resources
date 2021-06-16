# Basic authentication
You can create a user and password in your Redis instance for the exporter.
```
ACL SETUSER USERNAME +client +ping +info +config|get +cluster|info +slowlog +latency +memory +select +get +scan +xinfo +type +pfcount +strlen +llen +scard +zcard +hlen +xlen +eval allkeys on >PASSWORD
```
Replace `USER` and `PASSWORD` with yours for the Redis instance.

If your Redis server requires user and password authentication, you must first create a secret with the user and password for the exporter.
```
kubectl create secret generic redis-exporter-auth \
  --from-literal=user=USER \
  --from-literal=password=PASSWORD
```
Replace `USER` and `PASSWORD` with yours for the Redis instance:

# Installing the exporter
You will use the [Prometheus Redis Metrics Exporter](https://github.com/oliver006/redis_exporter).

The `redis-exporter-deploy.yaml` file provides a deployment with the exporter.

To deploy it, download the file and run:
```
kubectl apply -f redis-exporter-deploy.yaml
```
> Make sure to edit the environment variable `REDIS_ADDR` with the proper address name of your redis instance

If your Redis instance does not requires authentication, you can remove the `REDIS_USER` and `REDIS_PASSWORD` environment variables.

# Sysdig Agent configuration
In the Redis exporter Deployment use the Sysdig annotations to configure the port of the exporter as the scraping port. See the example given in the `redis-exporter-deploy.yaml` file.

Additionally, you can use the labels to add the namespace, workload type, and name of the database the exporter will take data from.
This way, you can view the metrics associated directly with the database pods and the exporter in Sysdig Monitor.

```yaml
spec:
  template:
    metadata:
      annotations:
        promcat.sysdig.com/port: "9121"

        # Add here the namespace, workload type (deployment, statefulset, replicaset, daemonset)
        # and workload name of the Redis instance that the exporter will take data from
        promcat.sysdig.com/target_ns: default
        promcat.sysdig.com/target_workload_type: deployment
        promcat.sysdig.com/target_workload_name: redis
```

After configuring the Sysdig annotations, download the sample configuration file and apply it by:
```bash
kubectl apply -f sysdig-agent-config.yaml
```
