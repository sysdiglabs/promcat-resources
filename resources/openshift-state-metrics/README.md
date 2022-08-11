# Openshift-state-metrics
Red Hat® OpenShift® state metrics is a expansion upon kube-state-metrics adding specific OpenShift® resource metrics

Openshift provides a prometheus with Openshift-state-metrics but doesn't provide any dashboard with this information.
You can gather the metrics with our agent and show all metrics in our dashboards or even in the grafana dashboards with
the Sysdig datasource as a Prometheus datasource.

# Metrics
The metrics gives you the information about the following:
- ClusterResourceQuotas
- BuildConfig
- DeploymentConfig
- Routes

# Attributions
The configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/).

All the metrics are maintained by [OpenShift-state-metrics](https://github.com/openshift/openshift-state-metrics).
