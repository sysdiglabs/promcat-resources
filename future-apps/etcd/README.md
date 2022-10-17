# etcd
Etcd is a strongly consistent, distributed key-value store that provides a reliable way to store data that needs to be accessed by a distributed system or cluster of machines.
It gracefully handles leader elections during network partitions and can tolerate machine failure, even in the leader node.

Etcd is the core of any Kubernetes cluster so it is so important to monitor it, and etcd exposes all its metrics in Prometheus format so you only have to configure the Prometheus job that does it.

# Metrics
* Etcd has a leader?
* The number of leader changes seen
* The total number of failed proposals seen
* RPC Rate
* Active Streams
* DB Size
* Disk Sync Duration
* The total number of consensus proposals committed
* Memory
* CPU usage
* GoRoutines

# Attributions
Configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/).

The alerts are inspired from [monitoring mixin](https://monitoring.mixins.dev/etcd/).
