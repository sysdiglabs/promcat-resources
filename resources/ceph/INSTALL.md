# Prerequisites
Ceph instruments Prometheus metrics and annotates the manager pod with Prometheus annotations. 

Make sure that the prometheus module is activated in the Ceph cluster by running the following command:

```
ceph mgr module enable prometheus
```

