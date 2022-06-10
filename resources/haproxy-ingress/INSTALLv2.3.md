# Adding HAProxy Ingress 
To install the HAProxy, you can use the [official Helm chart](https://github.com/haproxytech/helm-charts):
```sh
helm repo add haproxytech https://haproxytech.github.io/helm-charts
helm repo update
```

# Install k8s HAProxy ingress controller and configuring Prometheus metrics
This command will install haproxy-ingress helm chart with prometheus metrics and haproxy stats enabled
```
helm install haproxy-ingress haproxy-ingress/haproxy-ingress \
--set-string "controller.stats.enabled = true" \
--set-string "controller.metrics.enabled = true"
```

Metrics will be exposed via 9101 port and /metrics path

# Pod and metrics check

To get the pods of the ingress:
```
kubectl get pods -l app.kubernetes.io/instance=haproxy-ingress -n haproxy-ingress
```
Port forward 9101 to your localhost

```
kubectl port-forward -n haproxy-ingress pod-name 9101:9101
```
To count the metrics of a pod: 
```
curl 'http://localhost:9101/metrics' | grep -v "# HELP\|# TYPE" | wc -l
```
