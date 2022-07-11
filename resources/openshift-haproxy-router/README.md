# OpenShift HAProxy router
OpenShift offers different options as ingress router, one of them is based in HAProxy 2.0.

# Metrics
The HAProxy ingress router instruments Prometheus metrics, in OpenShift the endpoint is protected with user and password by default.

## Number of time series generated
The HAProxy ingress router generates ~400 time series.

# Attributions
The configuration files, dashboards, and alerts are maintained by [Sysdig team](https://sysdig.com/).

Using the [HAProxy Kubernetes ingress controller](https://github.com/haproxytech/kubernetes-ingress) and [OpenShift router](https://github.com/openshift/router) with the Apache 2.0 license.