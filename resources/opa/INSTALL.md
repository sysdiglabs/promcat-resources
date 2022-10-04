# Installing the exporter
Gatekeeper exposes a Prometheus metrics endpoint to provide metrics for monitoring services, health, and performance. The Open Policy Agent (OPA) also exposes a metrics endpoint when running as a server. However, since Gatekeeper embeds OPA and you don’t run OPA as a server, you won’t be using that endpoint.

When installing Gatekeeper, you must either edit the Gatekeeper controller manager deployment or the service with the appropriate annotations for Prometheus scraping

```sh
kubectl -n gatekeeper-system patch deploy gatekeeper-controller-manager -p '{"spec":{"template":{"metadata":{"annotations":{"prometheus.io/scrape": "true", "prometheus.io/port": "8888"}}}}}'

kubectl -n gatekeeper-system patch deploy gatekeeper-audit -p '{"spec":{"template":{"metadata":{"annotations":{"prometheus.io/scrape": "true", "prometheus.io/port": "8888"}}}}}'
```

