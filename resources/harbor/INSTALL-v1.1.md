# Installing the exporter
To install the exporter, do the following:

1. Install helm chart of Harbor as reference.

```
  helm install harbor harbor/harbor
```

2. Install the exporter with the configuration:

```
  kubectl apply -f harbor.yaml
```