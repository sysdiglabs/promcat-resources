# Kubernetes
Kubernetes (K8s) is an open-source system for automating deployment, scaling, and management of containerized applications.

The metrics for the information of kubernetes control plane are gathered from the pods located in the namespace kube-system.

# Prometheus and exporters

For the instalation of the entire infrastructure you can just install the helm chart of prometheus and some configurations.

In the exporter config tab there is more information about it.

# Metrics
With this metrics we can see the information about:
- Api-server
- Kubelet
- Control manager
- Scheduler
- Proxy
- etcd

# Attributions
Configuration files and dashboards maintained by [Sysdig team](https://sysdig.com/).

All dashboards and alerts are modified from the [kubernetes mixin](https://github.com/kubernetes-monitoring/kubernetes-mixin) as reference.
