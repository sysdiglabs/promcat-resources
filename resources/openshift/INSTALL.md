# Gather the metrics from the prometheus deployed by Openshift

You can either follow the steps given below or just download the script that includes all the commands and execute:
```sh
sh installation.sh
```

The Prometheus is behind an oauth proxy so you have to create the secret with the token:

1. Get the token:
  ```sh
  export SECRET=`oc get secret -n openshift-monitoring | grep  prometheus-k8s-token | head -n 1 | awk '{ print $1 }'`

  export TOKEN=`echo $(oc get secret $SECRET -n openshift-monitoring -o json | jq -r '.data.token') | base64 -d`
  ```
2. Create the secret in `sysdig-agent` namespace:
  ```sh
  oc -n sysdig-agent create secret generic prometheus-k8s-token --from-literal=token=$TOKEN
  ```
3. Edit the daemonset of sysdig to mount the secret:
  ```sh
  oc -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"volumes":[{"name":"prometheus-k8s-token","secret":{"defaultMode":420,"secretName":"prometheus-k8s-token"}}]}}}}'

  oc -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"containers":[{"name":"sysdig-agent","volumeMounts": [{"mountPath": "/opt/draios/kubernetes/prometheus/secrets","name": "prometheus-k8s-token"}]}]}}}}'
  ```
4. Apply the recording rules:
  ```sh
  oc apply -f rules.yaml
  ```
5. Apply the sysdig configuration:
  ```
  oc edit cm sysdig-agent
  ```
