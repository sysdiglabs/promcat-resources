# AWS RDS
Amazon Relational Database Service ([Amazon RDS](https://aws.amazon.com/rds/)) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while automating time-consuming administration tasks, such as hardware provisioning, database setup, patching, and backups. It frees you up to focus on your applications and provide them with performance improvements, high availability, security, and compatibility they need.

The metrics for AWS RDS are obtained through AWS Cloudwatch by using the [YACE exporter](https://github.com/ivx/yet-another-cloudwatch-exporter).

# Metrics
- BinLogDiskUsage
- BurstBalance
- CPUUtilization
- CPUCreditUsage
- CPUCreditBalance
- DatabaseConnections
- DiskQueueDepth
- FailedSQLServerAgentJobsCount
- FreeableMemory
- FreeStorageSpace
- MaximumUsedTransactionIDs
- NetworkReceiveThroughput
- NetworkTransmitThroughput
- OldestReplicationSlotLag
- ReadIOPS
- ReadLatency
- ReadThroughput
- ReplicaLag
- ReplicationSlotDiskUsage
- SwapUsage
- TransactionLogsDiskUsage
- TransactionLogsGeneration
- WriteIOPS
- WriteLatency
- WriteThroughput

For further information, see the [Cloudwatch documentation on RDS metrics](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MonitoringOverview.html#monitoring-cloudwatch).

# Number of time series generated
Cloudwatch generates ~20 metrics per instance.


# Attributions
The configuration files, dashboards, and alerts are maintained by [Sysdig team](https://sysdig.com/).

Using [Yace - yet another cloudwatch exporter](https://github.com/ivx/yet-another-cloudwatch-exporter) with Apache 2.0 license.
