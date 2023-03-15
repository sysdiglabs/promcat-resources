## Prerequisites

### Enable Prometheus Module
Ceph instruments Prometheus metrics and annotates the manager pod with Prometheus annotations. 

Make sure that the Prometheus module is activated in the Ceph cluster by running the following command:

```
ceph mgr module enable prometheus
```

## Installation

You can use our helm-charts in order to install the exporter in your cluster.