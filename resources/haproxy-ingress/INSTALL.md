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