# Prerequisites
To deploy a Prometheus server you will need:
* [helm](https://helm.sh/docs/intro/install/)  
* [helmfile](https://github.com/roboll/helmfile)

# Installing and configuring Prometheus
## Installing a new Prometheus with helm
In this section we will explain how to install and configure a new prometheus server with the recording rules.  

Download the following files: 
- helmfile.yaml
- prometheus.yaml
- prometheus.yml.gotmpl

execute: 

```
helmfile sync
```

## Configuring an existing Prometheus
In this section we will explain how to configure an existing Prometheus server with the recording rules.

To do this, you can either annotate the StatefulSet:

```
kubectl -n monitoring patch sts prometheus-server -p '{"spec":{"template":{"metadata":{"annotations":{"prometheus.io/scrape": "true", "prometheus.io/port": "9090"}}}}}'
```

Or download the file `prometheus-deploy.yaml` and apply it:

```
kubectl -n monitoring apply -f prometheus-deploy.yaml
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
