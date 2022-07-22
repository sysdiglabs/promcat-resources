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

You can now check haproxy router metrics (remember to port-forward port 1936):

```
curl -u $USER:$PASS http://ROUTERIP:1936/metrics
```