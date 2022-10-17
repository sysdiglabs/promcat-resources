# Ceph
The definition of ceph by the [wikipedia] (https://en.wikipedia.org/wiki/Ceph_(software)):
Ceph (pronounced /ˈsɛf/) is an open-source software storage platform, implements object storage on a single distributed computer cluster, and provides 3in1 interfaces for : object-, block- and file-level storage. Ceph aims primarily for completely distributed operation without a single point of failure, scalable to the exabyte level, and freely available.

Ceph replicates data and makes it fault-tolerant, by using commodity hardware and requiring no specific hardware support. As a result of its design, the system is both self-healing and self-managing, aiming to minimize administration time and other costs.

# Prometheus and exporters
Ceph already has a Prometheus endpoint with all the metrics exposed on the port 9283. In Kubernetes the pod is already annotated, so Prometheus can scrape the endpoint right away.

# Metrics
- Overview

# Attributions
Configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/).

Dashboards are based on [Grafana repository](https://grafana.com/grafana/dashboards/2842) as reference.

Alerts are based on [ceph mixing](https://monitoring.mixins.dev/ceph/#ceph-mgr-status) as reference
