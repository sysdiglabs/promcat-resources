# Ceph
The definition of ceph by the [wikipedia] (https://en.wikipedia.org/wiki/Ceph_(software)):
Ceph (pronounced /ˈsɛf/) is an open-source software storage platform, implements object storage on a single distributed computer cluster, and provides 3in1 interfaces for : object-, block- and file-level storage. Ceph aims primarily for completely distributed operation without a single point of failure, scalable to the exabyte level, and freely available.

Ceph replicates data and makes it fault-tolerant, using commodity hardware and requiring no specific hardware support. As a result of its design, the system is both self-healing and self-managing, aiming to minimize administration time and other costs.

# Prometheus and exporters
Ceph has already a Prometheus endpoint with all metrics in are exposed in the port 9283 and in Kubernetes the pod is already annotated so with the Sysdig agent we can scrape the endpoind right away.

# Metrics
- Overview

# Attributions
Configuration files and dashboards maintained by [Sysdig team](https://sysdig.com/).

Dashboards based on [Grafana repository](https://grafana.com/grafana/dashboards/2842) as reference.

Alerts based on [ceph mixing](https://monitoring.mixins.dev/ceph/#ceph-mgr-status) as reference