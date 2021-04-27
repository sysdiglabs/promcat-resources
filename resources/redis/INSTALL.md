# Basic authentication
You can create a user and password in your Redis instance for the exporter (change USER and PASSWORD for your actual ones): 
```
ACL SETUSER USERNAME +client +ping +info +config|get +cluster|info +slowlog +latency +memory +select +get +scan +xinfo +type +pfcount +strlen +llen +scard +zcard +hlen +xlen +eval allkeys on >PASSWORD
```

If your Redis server requires user and password authentication, you must first create a secret with the user and password for the exporter (change USER and PASSWORD for your actual ones:
```
kubectl create secret generic redis-exporter-auth \
  --from-literal=user=USER \
  --from-literal=password=PASSWORD
```


# Installing the exporter
We will use he [Prometheus Redis Metrics Exporter](https://github.com/oliver006/redis_exporter).
In the file below, you can find a deployment with the exporter.

To deploy it, just download the file and run:
```
kubectl apply -f redis-exporter-deploy.yaml
```
> Make sure to edit the environment variable `REDIS_ADDR` with the proper address name of your redis instance

If your Redis instance does not requires authentication, you can remove the `REDIS_USER` and `REDIS_PASSWORD` environment variables. 

# Sysdig Agent configuration
In the Redis exporter Deployment use the Sysdig annotations to configure the port of the exporter as scraping port. You can see an example in `redis-exporter-deploy.yaml`.

Also, you can use these labels to add the namespace, workload type and name of the database the exporter will take data from. 
This way, in Sysdig Monitor you will see the metrics associated directly to the database pods and to the exporter. 

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

Once configured the Sysdig annotations, you can download the sample configuration file below and apply it by:
```bash
kubectl apply -f sysdig-agent-config.yaml
```