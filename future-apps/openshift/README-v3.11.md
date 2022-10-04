# Openshift
Red Hat® OpenShift® offers a consistent hybrid cloud foundation for building and scaling containerized applications.
Benefit from streamlined platform installation and upgrades from one of the enterprise Kubernetes leaders.

Openshift provides a prometheus with all targets and metrics but doesn't provide any dashboard with this information.
You can gather the metrics with our agent and show all metrics in our dashboards or even in the grafana dashboards with
the Sysdig datasource as a Prometheus datasource.

For more information, see the exporter config tab.

# Metrics
The metrics gives you the information about the following:
- Api-server
- Kubelet
- Control manager
- Scheduler

# Attributions
The configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/).

All the dashboards and alerts are modified from the [kubernetes mixin](https://github.com/kubernetes-monitoring/kubernetes-mixin) for reference.
