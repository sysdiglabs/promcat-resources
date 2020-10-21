# Getting the authentication of the HAProxy router
The metrics endpoint of the HAProxy router in OpenShift 4.3 has a simple HTTP authentication configuration with user and password.

To get the user and password, execute the following commands: 
```
# USER
kubectl -n openshift-ingress get secret router-stats-default -o json | jq -r '.data.statsUsername'

# PASSWORD
kubectl -n openshift-ingress get secret router-stats-default -o json | jq -r '.data.statsPassword'
```

>Note: to execute these commands ou will need the tool [jq](https://stedolan.github.io/jq/)

# Sysdig Agent configuration
To set up the configuration of the Sysdig Agent to collect the metrics from the HAProxy router in OpenShift 4.3 you have to add the following configuration changing the `USER` and `PASSWORD` by the values extracted in the previous step:
```yaml
prometheus:
  process_filter: 
    - include: 
        port: 1936
        conf: 
          username: "USER"
          password: "PASSWORD"
```
