# Setting up permissions in the AWS account
## Creating an AWS IAM Policy
The exporter needs permissions to access the resources from the AWS account.

First, create an AWS IAM policy on your AWS infrastructure allowing read CloudWatch metrics and get resources by tags.
Here is a AWS IAM configuration example:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CloudWatchExporterPolicy",
            "Effect": "Allow",
            "Action": [
                "tag:GetResources",
                "cloudwatch:ListTagsForResource",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:GetMetricData",
                "cloudwatch:ListMetrics"
            ],
            "Resource": "*"
        }
    ]
}
```

## Creating the credentials for the exporter
Create a file $HOME/.aws/credentials as the following, substituting the values with your key and password:

```ini
# CREDENTIALS FOR AWS ACCOUNT
aws_region = us-east-1
aws_access_key_id = AYYYYYZZZZZZ3BLXXXXX
aws_secret_access_key = bXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

# Configuring the resources to monitor
The YACE exporter uses an API call that filters the resources by tags. 
This implies that if you want to monitor a resource, **it has to have at least one tag**. Else, it will not be scraped.

# Installing the exporter
To install the exporter follow this steps:

1. Download the yaml to a local file named 'rds-deploy.yaml'
2. Change the following line in the ConfigMap with the AWS region where the resources to monitor are located:
```
region: us-east-1
```
1. Change the field 'credentials' of the secret 'yace-rds-credentials' and paste the content of the following command:
```
cat ~/.aws/credentials | base64
```
4. Apply the deployment:
```
kubectl apply -f rds-deploy.yaml
```
5. You can check that the exporter is working checking that the pods are running:
```
kubectl -n yace get pods
```

# Sysdig Agent configuration
In the yace Deployment we will include the Prometheus annotations configuring the port of the exporter as scraping port.    

Also, in the Sysdig Agent configuration, be sure to have these lines of configuration to scrape the containers with Prometheus annotations.
```yaml
process_filter:
  - include:
      kubernetes.pod.annotation.prometheus.io/scrape: true
      conf:
        path: "{kubernetes.pod.annotation.prometheus.io/path}"
        port: "{kubernetes.pod.annotation.prometheus.io/port}"
```

You can download the sample configuration file below and apply it by:
```
kubectl apply -f sysdig-agent-config.yaml
```