#!/bin/bash
export SECRET=`oc get secret -n openshift-monitoring | grep  prometheus-k8s-token | head -n 1 | awk '{ print $1 }'`
export TOKEN=`echo $(oc get secret $SECRET -n openshift-monitoring -o json | jq -r '.data.token') | base64 -d`
oc -n sysdig-agent create secret generic prometheus-k8s-token --from-literal=token=$TOKEN
oc -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"volumes":[{"name":"prometheus-k8s-token","secret":{"defaultMode":420,"secretName":"prometheus-k8s-token"}}]}}}}'
oc -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"containers":[{"name":"sysdig-agent","volumeMounts": [{"mountPath": "/opt/draios/kubernetes/prometheus/secrets","name": "prometheus-k8s-token"}]}]}}}}'
wget 'https://raw.githubusercontent.com/sysdiglabs/promcat-resources/master/resources/openshift/include/rules-v4.3.yaml'
oc apply -f rules-v4.3.yaml 
