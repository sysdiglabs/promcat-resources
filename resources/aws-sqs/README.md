# AWS SQS
Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.

The metrics for AWS SQS are obtained through AWS Cloudwatch by using the [YACE exporter](https://github.com/ivx/yet-another-cloudwatch-exporter).

## Cloudwatch billing considerations
Using AWS Cloudwatch for monitoring can incur additional costs in your AWS billing.
See the [AWS Cloudwatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html) for further details.

# Metrics
- ApproximateAgeOfOldestMessage
- ApproximateNumberOfMessagesDelayed
- ApproximateNumberOfMessagesNotVisible
- ApproximateNumberOfMessagesVisible
- NumberOfEmptyReceives
- NumberOfMessagesDeleted
- NumberOfMessagesReceived
- NumberOfMessagesSent
- SentMessageSize

For further information, see the [Cloudwatch documentation on EBS metrics](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html).

# Number of time series generated
Cloudwatch generates ~10 time series per queue.

# Attributions
The configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/).

Using [Yace - yet another cloudwatch exporter](https://github.com/ivx/yet-another-cloudwatch-exporter) with Apache 2.0 license.