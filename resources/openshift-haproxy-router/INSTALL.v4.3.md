# Getting the authentication of the HAProxy router
The metrics endpoint of the HAProxy router in OpenShift 4.3 has a simple HTTP authentication configuration with user and password.

To retrieve the username and password, run the following commands:
```
# USER
kubectl -n openshift-ingress get secret router-stats-default -o json | jq -r '.data.statsUsername'

# PASSWORD
kubectl -n openshift-ingress get secret router-stats-default -o json | jq -r '.data.statsPassword'
```

>Note: to execute these commands ou will need the tool [jq](https://stedolan.github.io/jq/)

# Sysdig Agent configuration
To configure Sysdig Agent to collect metrics from the HAProxy router in OpenShift 4.3, do the following:

1. Copy the values of `USER` and `PASSWORD` retrieved in the previous step.

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
