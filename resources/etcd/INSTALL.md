# Prerequisites
## Mount the etcd certificates in the sysdig agent
```sh
kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"volumes":[{"hostPath":{"path":"/etc/kubernetes/pki/etcd-manager-main","type":"DirectoryOrCreate"},"name":"etcd-certificates"}]}}}}'

kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"containers":[{"name":"sysdig-agent","volumeMounts": [{"mountPath": "/etc/kubernetes/pki/etcd-manager","name": "etcd-certificates"}]}]}}}}'
```