# Integrating HAProxy router in the Prometheus Cluster Monitoring
The HAProxy router metrics endpoint is not included in the Prometheus Cluster Monitoring in version 3.11 so you need to create a prometheus job and add some permissions to prometheus service account

Steps to execute:

1. Create the prometheus job for the HAProxy router executing the following command:

```
oc create -n openshift-monitoring -f haproxy-router-job.yaml
```

2. Give permission to prometheus to scrape router metrics using bearer token:

```
oc create -n openshift-monitoring -f router-clusterrolebinding-okd3.yaml
```

Now you can curl the metrics from prometheus pod or from the prometheus console

```
curl -v -s -k -H "Authorization: Bearer `cat /var/run/secrets/kubernetes.io/serviceaccount/token`" https://router.default.svc:1936/metrics
```
