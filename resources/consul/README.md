# Consul
Consul is a service mesh solution providing a full featured control plane with service discovery, configuration, and segmentation functionality. Each of these features can be used individually as needed, or they can be used together to build a full service mesh. Consul requires a data plane and supports both a proxy and native integration model. Consul ships with a simple built-in proxy so that everything works out of the box, but also supports 3rd party proxy integrations such as Envoy.

# Prometheus and exporters
Consul already has a Prometheus endpoint with all the metrics exposed on the port 8500 and the envoys are the 20200. In Kubernetes the pod is already annotated, so Prometheus can scrape the endpoint right away.

# Metrics
- Consul server statistics
- Consul client statistics
- Envoy metrics

# Attributions
Configuration files, dashboards and alerts are maintained by [Sysdig team](https://sysdig.com/).