# OpenShift HAProxy router
OpenShift offers different options as ingress router, one of them is based in HAProxy 2.0.

# Metrics
The HAProxy ingress router instruments Prometheus metrics, and in OpenShift the endpoint is protected with user and password.

## Number of time series generated
The HAProxy ingress router generates ~400 time series. 

# Attributions
Configuration files, dashboards and alerts maintained by [Sysdig team](https://sysdig.com/).

Using [HAProxy Kubernetes ingress controller](https://github.com/haproxytech/kubernetes-ingress) and [OpenShift router](https://github.com/openshift/router), both with Apache 2.0 license.