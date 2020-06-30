# Installing the exporter
We will use he [Prometheus Redis Metrics Exporter](https://github.com/oliver006/redis_exporter).
In the file below, you can find a deployment with the exporter as a sidecar of a redis instance.

To deploy it, just download the file and run:
```
kubectl apply -f redis-deploy.yaml
```

# Sysdig Agent configuration
Be sure to annotate the deployment with the prometheus tags as shown in the deployment file below.

Also, in the Sysdig Agent configuration, be sure to have these lines of configuration to scrape the containers with Prometheus annotations.
```yaml
process_filter:
  - include:
      kubernetes.pod.annotation.prometheus.io/scrape: true
      conf:
        path: "{kubernetes.pod.annotation.prometheus.io/path}"
        port: "{kubernetes.pod.annotation.prometheus.io/port}"
```

You can download the sample configuration file below and apply it by:
```bash
kubectl apply -f sysdig-agent-config.yaml
```