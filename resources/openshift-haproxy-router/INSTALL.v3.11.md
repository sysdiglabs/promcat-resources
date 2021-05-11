# Getting the authentication of the HAProxy router
The metrics endpoint of the HAProxy router in OpenShift 3.11 has a simple HTTP authentication configuration with username and password.

To retrieve the username and password, run the following commands:
```
# USER
kubectl -n default get deploymentConfig router -o json | jq -r '.spec.template.spec.containers[].env[] | select( .name | contains("STATS_USERNAME")) | .value'

# PASSWORD
kubectl -n default get deploymentConfig router -o json | jq -r '.spec.template.spec.containers[].env[] | select( .name | contains("STATS_PASSWORD")) | .value'
```

>Note: to execute these commands ou will need the tool [jq](https://stedolan.github.io/jq/)

# Sysdig Agent configuration
To configure Sysdig Agent to collect metrics from the HAProxy router in OpenShift 4.3, do the following:

1. Copy the values of the `USER` and `PASSWORD` retrieved in the previous step.

2. Add them to the job section of the `prometheus.yaml` file as follows:
```yaml
scrape_configs:
  - job_name: 'haproxy-router'
      basic_auth:
        username: USER
        password: PASSWORD
      relabel_configs:
      - action: keep
        source_labels:
        - __meta_kubernetes_namespace
        - __meta_kubernetes_pod_name
        separator: '/'
        regex: 'default/router-1-.+'
```
See the example configuration given below.
