# Prerequisites
KSM and cAdvisor generates a high number of metrics. As the Sysdig Agent has a limit of time series that can send to Sysdig Monitor, you have to deploy a Prometheus server and create the recording rules that we provide. This way, we will filter only the metrics that we need.

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

# Configuring the Sysdig Agent
To be able to install the Sysdig Agent, be sure to have at least one EC2 instance in your EKS cluster.

1. Install with helm Sysdig Agent in your cluster: 

```
kubectl create ns sysdig-agent
helm install -n sysdig-agent \
     --set sysdig.accessKey=<YOUR-ACCESS-KEY> \
     --set sysdig.settings.k8s_cluster_name=<YOUR-CLUSTER-NAME> \
     sysdig-agent sysdiglabs/sysdig
```

2. Copy the agent configuration provided and save it as `sysdig-agent.yaml`. Then apply it:

```
kubectl apply -f sysdig-agent.yaml
```
