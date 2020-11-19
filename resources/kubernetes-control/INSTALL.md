# Prerequisites
Kubernetes generates a high number of metrics for the control plane. As the Sysdig Agent has a limit of time-series that can send to Sysdig Monitor, you have to deploy a Prometheus server and create the recording rules that we provide. This way, we will filter only the metrics that we need.

To deploy a Prometheus server you will need:
* [helm](https://helm.sh/docs/intro/install/)  
* [helmfile](https://github.com/roboll/helmfile)

##  Mount the etcd certificates in the sysdig agent
```sh
kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"volumes":[{"hostPath":{"path":"/etc/kubernetes/pki/etcd-manager-main","type":"DirectoryOrCreate"},"name":"etcd-certificates"}]}}}}'
  
kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"containers":[{"name":"sysdig-agent","volumeMounts": [{"mountPath": "/etc/kubernetes/pki/etcd-manager","name": "etcd-certificates"}]}]}}}}'
```

# Installing and configuring Prometheus
## Installing a new Prometheus with helm
In this section we will explain how to install and configure a new prometheus server with the recording rules.  

Download the following files: 
- helmfile.yaml
- recording_rules.yaml
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

# Configuring the Sysdig Agent
To use the Sysdig agent, you have to create the recording rules for only scrape the metrics we will use in our dashboards.

1. Copy the agent configuration provided and save it as `sysdig-agent.yaml`. Then apply it:

```
kubectl apply -f sysdig-agent.yaml
```
