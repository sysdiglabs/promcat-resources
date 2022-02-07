##  Mount the etcd certificates in the sysdig agent
```sh
kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"volumes":[{"hostPath":{"path":"/etc/kubernetes/pki/etcd-manager-main","type":"DirectoryOrCreate"},"name":"etcd-certificates"}]}}}}'
  
kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"containers":[{"name":"sysdig-agent","volumeMounts": [{"mountPath": "/etc/kubernetes/pki/etcd-manager","name": "etcd-certificates"}]}]}}}}'
```

# Exposing the Proxy port in kops
If you are using kops, you will have to change the cluster spec to expose the port for the proxy. To edit the cluster, run:

```
kops --state s3://name-of-s3 --name cluster-name edit cluster
```

And add the following lines:

```yaml
kubeProxy:
  metricsBindAddress: 0.0.0.0
```

And update the cluster:

```
kops --state s3://name-of-s3 --name cluster-name rolling-update cluster --yes
```