# Getting the authentication of the HAProxy router
The metrics endpoint of the HAProxy router in OpenShift 4.7 has a basic HTTP authentication configuration with username and password.

To retrieve the username and password, run the following commands:
```
# USER
export USER=`echo $(kubectl -n openshift-ingress get secret router-stats-default -o json | jq -r '.data.statsUsername') | base64 --decode`

# PASSWORD
export PASS=`echo $(kubectl -n openshift-ingress get secret router-stats-default -o json | jq -r '.data.statsPassword') | base64 --decode`
```

>Note: to execute these commands ou will need the tool [jq](https://stedolan.github.io/jq/)

The Prometheus Monitoring stack is installed with OpenShift Container Platform by default so there is no need of additional configuration in prometheus.yml file

You can now check haproxy router metrics:

```
curl -u $USER:$PASS http://ROUTERIP:1936/metrics
```

# Sysdig Agent configuration

To configure Sysdig Agent to collect metrics from the HAProxy router in OpenShift 4.7, do the following:

1. Create a new secret in your cluster with the USER/PASS gathered before

```
kubectl create secret generic router-secret -n sysdig-agent --from-literal=username=$USER --from-literal=password=$PASS
````

2. Mount this secret in the sysdig agent

Create a yaml file named secret.yaml and copy this content

```yaml
spec:
  template:
    spec:
      containers:
      - name: sysdig
        volumeMounts:
        - name: secret-volume
          mountPath: /etc/secret-volume
      volumes:
        - name: secret-volume
          secret:
             secretName: router-secret
```

Execute the following command in your cluster to apply the patch:

```
kubectl patch ds sysdig-agent -n sysdig-agent --patch-file secret.yaml
````

### Download and apply configuration

1. Copy the USER value retrieved in the first step

2. Add it to the job section of prometheus.yaml file as follows:

```yaml
- job_name: 'haproxy-router'
  basic_auth:
    username: USER
    password_file: '/etc/secret-volume/password'
  tls_config:
    insecure_skip_verify: true
  kubernetes_sd_configs:
  - role: pod
  relabel_configs:
  - action: keep
    source_labels: [__meta_kubernetes_pod_host_ip]
    regex: __HOSTIPS__
  - action: drop
```

See the example configuration given below.