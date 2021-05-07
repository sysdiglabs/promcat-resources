# Istio
Istio can do the following:

* Intelligently control the flow of traffic and API calls between services, conduct a range of tests, and upgrade gradually with red/black deployments.
* Automatically secure your services through managed authentication, authorization, and encryption of communication between services.
* Apply policies and ensure that they are enforced and the resources are fairly distributed among consumers.
* See what's happening with rich automatic tracing, monitoring, and logging of all your services.

# Prometheus and exporters
Istio already provides a Prometheus and a Grafana servers with all the metrics you need to monitor. However, Prometheus is not a LTS and you only can get a few hours of metrics because of the retention limit provided by the given Prometheus server. If you want additional hours, use external services such as the Sysdig agent.

# Metrics
- Services
- Workloads

# Attributions
Configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/).

All dashboards are modified from the [dashboards provided by Istio](https://grafana.com/orgs/istio/dashboards) as reference.
