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