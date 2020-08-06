# AWS Elastic Kubernetes Service with Fargate
Amazon Elastic Kubernetes Service ([Amazon EKS](https://aws.amazon.com/eks/)) is a fully managed Kubernetes service. 

You can choose to run the nodes on EC2 instances or use AWS Fargate, which is serverless compute for containers. Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design

# Metrics
The main challenge in EKS is to gather metrics for Fargate pods. To be able to collect metrics of pods and resources, EKS offers cAdvisor, that in combination with Kube-State-Metrics (KSM) offer full observability of the workloads of the cluster.

Being a fully managed Kubernetes service and due to the restrictions to access control plane endpoint, most of the control plane metrics are not available. 

# Number of time series generated
A newly created cluster generated about 450 metrics. The number increases with the number of pods and workloads.

# Attributions
Configuration files, dashboards and alerts maintained by [Sysdig team](https://sysdig.com/).

Recording rules, alerts and dashboards originally based on [Kubernetes mixin](https://github.com/kubernetes-monitoring/kubernetes-mixin) with Apache License 2.0. 