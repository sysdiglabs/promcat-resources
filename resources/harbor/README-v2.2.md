# Harbor

Harbor is an open-source container registry, originally developed by VMware and now under the CNCF umbrella. Although many of us typically use
hosted container registries such as DockerHub, Quay, ECR, GCR or ACR; when you need a self-hosted registry, Harbor is a great choice.
Harbor provides great features such as RBAC, replication and image scanning.

# Prometheus and exporters

Harbor is already instrumented so you don't have to add any extra exporter.

```
  helm install harbor harbor/harbor
```


# Attributions
Configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/).
