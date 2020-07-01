# Prerequisites
Kubernetes generates a high number of metrics for the control plane. As the Sysdig Agent has a limit of timesieres that can send to Sysdig Monitor, you have to deploy a Prometheus server and create the recording rules that we provide. This way, we will filter only the metrics that we need.

To deploy a Prometheus server you will need:
* [helm](https://helm.sh/docs/intro/install/)  
* [helmfile](https://github.com/roboll/helmfile)

# Installing and configuring Prometheus
## Installing a new Prometheus with helm
In this section we will explain how to install and configure a new prometheus server with the recording rules.  

Download the following files: 
- helmfile.yaml
- recording_rules.yaml
- prometheus.yaml

execute: 
```bash 
helmfile sync
```

## Configuring an existing Prometheus
In this section we will explain how to configure an existing Prometheus server with the recording rules.

To do this, you can either annotate the StatefulSet:

```bash
kubectl -n monitoring patch sts prometheus-server -p '{"spec":{"template":{"metadata":{"annotations":{"prometheus.io/scrape": "true", "prometheus.io/port": "9090"}}}}}'
```

Or download the file `prometheus-deploy.yaml` and apply it:
```bash
kubectl -n monitoring apply -f prometheus-deploy.yaml
```

# Configuring the etcd to get the metrics
Etcd exposes all their metrics by default but Prometheus has to know where it is. 

First, you need to get the SSL certificates.
1. Getting the certificates: 
The certificates are located in the master node in `/etc/kubernetes/pki/etcd-manager-main/etcd-clients-ca.key` and `/etc/kubernetes/pki/etcd-manager-main/etcd-clients-ca.crt`. Save them in you local computer.
2. Creating the secrets for the certificates:
Once we have the certificates let’s proceed to create the secrets in the namespace where the Prometheus server is located. In our case, it will be located in the namespace `monitoring`. 
To create the secrets, run:
```bash
kubectl -n monitoring create secret generic etcd-ca --from-file=etcd-clients-ca.key --from-file etcd-clients-ca.crt
```
---
**NOTE**

> If you are using kops, you will have to change the cluster spec to expose the port for the proxy. To edit the cluster, run:

```bash
kops --state s3://name-of-s3 --name cluster-name edit cluster
```

And add the following lines:
```yaml
kubeProxy:
  metricsBindAddress: 0.0.0.0
```

And update the cluster:
```bash
kops --state s3://name-of-s3 --name cluster-name rolling-update cluster --yes
```
---
# Configuring the Sysdig Agent
To use the Sysdig agent, you have to create the recording rules for only scrape the metrics we will use in our dashboards.

1. Copy the agent configuration provided and save it as `sysdig-agent.yaml`. Then apply it:
```
kubectl apply -f sysdig-agent.yaml
```
