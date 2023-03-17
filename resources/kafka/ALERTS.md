# Alerts
## [Kafka] Broker Down
There are less Kafka brokers up than expected. The 'workload' label of the Kafka Deployment/Stateful set must be specified.
## [Kafka] No Leader
There is no ActiveController or 'leader' in the Kafka cluster.
## [Kafka] Too Many Leaders
There is more than one ActiveController or 'leader' in the Kafka cluster.
## [Kafka] Offline Partitions
There are one or more Offline Partitions. These partitions don’t have an active leader and are hence not writable or readable.
## [Kafka] Under Replicated Partitions
There are one or more Under Replicated Partitions.
## [Kafka] Under In-Sync Replicated Partitions
There are one or more Under In-Sync Replicated Partitions. These partitions will be unavailable to producers who use 'acks=all'.
## [Kafka] ConsumerGroup Lag Not Decreasing
The ConsumerGroup lag is not decreasing. The Consumers might be down, failing to process the messages and continuously retrying, or their consumption rate is lower than the production rate of messages.
## [Kafka] ConsumerGroup Without Members
The ConsumerGroup doesn't have any members.
## [Kafka] Producer High ThrottleTime By Client-Id
The Producer has reached its quota and has high throttle time. Applicable when Client-Id-only quotas are being used.
## [Kafka] Producer High ThrottleTime By User
The Producer has reached its quota and has high throttle time. Applicable when User-only quotas are being used.
## [Kafka] Producer High ThrottleTime By User And Client-Id
The Producer has reached its quota and has high throttle time. Applicable when Client-Id + User quotas are being used.
## [Kafka] Consumer High ThrottleTime By Client-Id
The Consumer has reached its quota and has high throttle time. Applicable when Client-Id-only quotas are being used.
## [Kafka] Consumer High ThrottleTime By User
The Consumer has reached its quota and has high throttle time. Applicable when User-only quotas are being used.
## [Kafka] Consumer High ThrottleTime By User And Client-Id
The Consumer has reached its quota and has high throttle time. Applicable when Client-Id + User quotas are being used.