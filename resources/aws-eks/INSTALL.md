# Prerequisites
KSM and cAdvisor generates a high number of metrics. As the Sysdig Agent has a limit of timesieres that can send to Sysdig Monitor, you have to deploy a Prometheus server and create the recording rules that we provide. This way, we will filter only the metrics that we need.

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
To use the Sysdig agent, you have to create the recording rules for only scrape the metrics we will use in our dashboards.

1. Copy the agent configuration provided and save it as `sysdig-agent.yaml`. Then apply it:

```
kubectl apply -f sysdig-agent.yaml
```
