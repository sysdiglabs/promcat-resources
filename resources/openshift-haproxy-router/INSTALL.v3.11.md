# Getting the authentication of the HAProxy router
The metrics endpoint of the HAProxy router in OpenShift 3.11 has a simple HTTP authentication configuration with user and password.

To get the user and password, execute the following commands: 
```
# USER
kubectl -n default get deploymentConfig router -o json | jq -r '.spec.template.spec.containers[].env[] | select( .name | contains("STATS_USERNAME")) | .value' 

# PASSWORD
kubectl -n default get deploymentConfig router -o json | jq -r '.spec.template.spec.containers[].env[] | select( .name | contains("STATS_PASSWORD")) | .value' 
```

>Note: to execute these commands ou will need the tool [jq](https://stedolan.github.io/jq/)

# Sysdig Agent configuration
To set up the configuration of the Sysdig Agent to collect the metrics from the HAProxy router in OpenShift 3.11 you have to add in the job of the `prometheus.yaml`file the following configuration changing the `USER` and `PASSWORD` by the values extracted in the previous step:
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
You can check a configuration example below. 