# Rancher
Rancher is a complete software stack for teams adopting containers. It addresses the operational and security challenges of managing multiple Kubernetes clusters, while providing DevOps teams with integrated tools for running containerized workloads.

# Prometheus and exporters
Rancher give the option to install a Prometheus operator but it doesn't have all control plane metrics, only the kubelet and api server metrics. To get the other metrics you have to create the services and service monitors for the rest of them.

# Control plane metrics
- Api-server
- Kubelet
- Control manager
- Scheduler
- Proxy
- coreDNS
- etcd

# Attributions
Configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/).

All dashboards and alerts are modified from the [kubernetes mixin](https://github.com/kubernetes-monitoring/kubernetes-mixin) for reference.
