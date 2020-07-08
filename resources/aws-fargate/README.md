# AWS Fargate and ECS
AWS ECS (Elastic Container Service) is a container orchestration solution that can run either in Fargate or in EC2 instances.
All the configuration files, dashboards and alerts listed in this section works with ECS in both kind of infrastructure.

AWS Fargate is a serverless compute engine for containers that works with Amazon Elastic Container Service (ECS).

The metrics for AWS ECS are obtained through AWS Cloudwatch using the [YACE exporter](https://github.com/ivx/yet-another-cloudwatch-exporter).

Check out our blog post on [Monitoring AWS Fargate](https://sysdig.com/blog/monitor-aws-fargate-prometheus/), covering the main metrics to monitor and alert.

![Monitoring AWS Fargate](https://raw.githubusercontent.com/sysdiglabs/promcat-resources/master/resources/aws-fargate/images/Monitoring-AWS-Fargate-with-Prometheus-and-Sysdig_2.png)

## Cloudwatch billing considerations
Using AWS Cloudwatch for monitoring can incur in additional costs in your AWS billing.
Check the [AWS Cloudwatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html) for further details.

# Metrics
Cloudwatch offers the following metrics for AWS Fargate:
- ContainerInstanceCount
- CpuUtilized
- CpuReserved
- DeploymentCount
- DesiredTaskCount
- MemoryUtilized
- MemoryReserved
- NetworkRxBytes
- NetworkTxBytes
- PendingTaskCount
- RunningTaskCount
- ServiceCount
- StorageReadBytes
- StorageWriteBytes
- TaskCount
- TaskSetCount

> Note: The metrics NetworkRxBytes and NetworkTxBytes are available only for containers in bridge network mode.

For further information, consult the [Cloudwatch documentation on Container Insights for ECS metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html).

# Attributions
Configuration files and dashboards maintained by [Sysdig team](https://sysdig.com/).

Using [Yace - yet another cloudwatch exporter](https://github.com/ivx/yet-another-cloudwatch-exporter) with Apache 2.0 license.
