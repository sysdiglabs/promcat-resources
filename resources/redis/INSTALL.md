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
In the file below, you can find a deployment with the exporter as a sidecar of a redis instance.

To deploy it, just download the file and run:
```
kubectl apply -f redis-deploy.yaml
```
> Make sure to edit the environment variable `REDIS_ADDR` with the proper address name of your redis instance

If your Redis instance does not requires authentication, you can remove the `REDIS_USER` and `REDIS_PASSWORD` environment variables. 

# Sysdig Agent configuration
The default configuration of the Sysdig agent will detect the Prometheus annotated pod of the exporter and scrape it automatically. 

Also, in the `sysdig-agent-config.yaml` file you can find an example of the minimum configuration needed in the agent. 