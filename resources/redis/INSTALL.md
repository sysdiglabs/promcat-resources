# Installing the exporter
We will use he [Prometheus Redis Metrics Exporter](https://github.com/oliver006/redis_exporter).
In the file below, you can find a deployment with the exporter as a sidecar of a redis instance.

To deploy it, just download the file and run:
```
kubectl apply -f redis-deploy.yaml
```

# Sysdig Agent configuration
No need for special configuration in the agent.
Just, be sure to annotate the deployment with the prometheus tags as shown in the deployment file below.
