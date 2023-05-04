# Prerequisites

### Enable Prometheus Module
Ceph instruments Prometheus metrics and annotates the manager pod with Prometheus annotations. 

Make sure that the Prometheus module is activated in the Ceph cluster by running the following command:

```
ceph mgr module enable prometheus
```
# Installation
The application is ready to be scraped