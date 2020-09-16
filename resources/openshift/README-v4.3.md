# Openshift 
Red Hat® OpenShift® offers a consistent hybrid cloud foundation for building and scaling containerized applications. 
Benefit from streamlined platform installation and upgrades from one of the enterprise Kubernetes leaders.

Openshift provides a prometheus with all targets and metrics but doesn't provide any dashboard with this information.
We can gather the metrics with our agent and show all metrics in our dashboards or even in the grafana dashboards with
the Sysdig datasource as a Prometheus datasource.

In the exporter config tab there is more information about how we can achieve this kind of things.

# Metrics
With this metrics we can see the information about:
- Api-server
- Kubelet
- Control manager
- Scheduler
- etcd
- CoreDNS

# Attributions
Configuration files and dashboards maintained by [Sysdig team](https://sysdig.com/).

All dashboards and alerts are modified from the [kubernetes mixin](https://github.com/kubernetes-monitoring/kubernetes-mixin) as reference.
