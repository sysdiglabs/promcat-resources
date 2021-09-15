# Alerts
## RabbitMQClusterOperatorUnavailableReplicas
There are pods that are either running but not yet available or pods that still have not been created.
## InsufficientEstablishedErlangDistributionLinks
There are only `{{ $value }}` established Erlang distribution links
## LowDiskWatermarkPredicted
The predicted free disk space in 24 hours from now is `{{ $value | humanize1024 }}B`
## HighConnectionChurn
Over the last 5 minutes, `{{ $value | humanizePercentage }}` of total connections are closed or opened per second in RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}` in namespace `{{ $labels.namespace }}`.
## NoMajorityOfNodesReady
Only `{{ $value }}` replicas are ready in StatefulSet `{{ $labels.statefulset }}` of RabbitMQ cluster `{{ $labels.label_app_kubernetes_io_name }}` in namespace `{{ $labels.namespace }}`.
## PersistentVolumeMissing
PersistentVolumeClaim `{{ $labels.persistentvolumeclaim }}` of RabbitMQ cluster `{{ $labels.label_app_kubernetes_io_name }}` in namespace `{{ $labels.namespace }}` is not bound.
## UnroutableMessages
There were `{{ $value | printf "%.0f" }}` unroutable messages within the last 5 minutes in RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}` in namespace `{{ $labels.namespace }}`.
## FileDescriptorsNearLimit
`{{ $value | humanizePercentage }}` file descriptors of file descriptor limit are used in RabbitMQ node `{{ $labels.rabbitmq_node }}`, pod `{{ $labels.pod }}`, RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}`, namespace `{{ $labels.namespace }}`.
## ContainerRestarts
Over the last 10 minutes, container `{{ $labels.container }}` restarted `{{ $value | printf "%.0f" }}` times in pod `{{ $labels.pod }}` of RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}` in namespace `{{ $labels.namespace }}`.
## TCPSocketsNearLimit
`{{ $value | humanizePercentage }}` TCP sockets of TCP socket limit are open in RabbitMQ node `{{ $labels.rabbitmq_node }}`, pod `{{ $labels.pod }}`, RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}`, namespace `{{ $labels.namespace }}`.
## 