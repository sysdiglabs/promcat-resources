# Installing HAProxy Ingress
To install the HAProxy, you can use the [official Helm chart](https://github.com/haproxytech/helm-charts):
```sh
helm repo add haproxytech https://haproxytech.github.io/helm-charts
helm repo update
helm install haproxy-ingress haproxytech/kubernetes-ingress
```

# Configuring HAPRoxy metrics
HAProxy ingress exposes prometheus metrics on the port 1024 of its pods. To scrape them, annotate the deployment with the Prometheus tags for scrape and port:
```sh
kubectl patch deployment haproxy-ingress-kubernetes-ingress \
    -p '{"spec":{"template":{"metadata":{"annotations":{"prometheus.io/scrape": "true", "prometheus.io/port": "1024", "prometheus.io/path": "/metrics"}}}}}'
```
After executing this, the pods will automatically restart with the new annotations.

# Sysdig Agent configuration
HAProxy generates metrics for the scopes global, frontend, backend, and server. This last scope usually have a high cardinality.
To scrape only the other scopes, use this configuration for the `prometheus.yaml` configuration file of the Sysdig agent.

You can download the sample configuration file and apply it by:
```bash
kubectl apply -f sysdig-agent-config.yaml
```
