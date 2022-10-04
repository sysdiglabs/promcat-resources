# Portworx
Portworx provides a fully integrated solution for persistent storage, data protection, disaster recovery, data security, cross-cloud and data migrations, and automated capacity management for applications running on Kubernetes.

# Prometheus and exporters
Portworx already has a Prometheus endpoint with all the metrics exposed on the port 9001 (port 17001 if deployed in Openshift). In Kubernetes the pod is already annotated, so Prometheus can scrape the endpoint right away.

# Metrics
- Portworx cluster statistics
- Portworx volumes statistics

# Attributions
Configuration files, dashboards and alerts are maintained by [Sysdig team](https://sysdig.com/).