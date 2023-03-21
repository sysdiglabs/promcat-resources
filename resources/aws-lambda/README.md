# AWS Lambda
AWS Lambda lets you run code without provisioning or managing servers.
With Lambda, you can run code for virtually any type of application or backend service - all with zero administration.
Just upload your code and Lambda takes care of everything required to run and scale your code with high availability.
You can set up your code to automatically trigger from other AWS services or call it directly from any web or mobile app.

The metrics for AWS Fargate are obtained through AWS Cloudwatch by using the [YACE exporter](https://github.com/ivx/yet-another-cloudwatch-exporter).

## Cloudwatch billing considerations
Using AWS Cloudwatch for monitoring can incur additional costs in your AWS billing.
See the [AWS Cloudwatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html) for further details.

# Metrics
Cloudwatch offers the following metrics for AWS Lambda:
- Invocations
- Errors
- Throttles
- Duration


For further information, see the [Cloudwatch documentation on Lambda metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html).

# Attributions
The configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/).

Using [Yace - yet another cloudwatch exporter](https://github.com/ivx/yet-another-cloudwatch-exporter) with Apache 2.0 license.