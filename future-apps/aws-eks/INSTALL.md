# Prerequisites

To deploy a Prometheus server you will need:
* [helm](https://helm.sh/docs/intro/install/)  
* [helmfile](https://github.com/roboll/helmfile)

# Installing and configuring Prometheus server
## Installing a new Prometheus server with Helm
This section helps you install and configure a new Prometheus server with the recording rules.  

1. Download the following files:
- helmfile.yaml
- recording_rules.yaml
- prometheus.yaml
- prometheus.yml.gotmpl

2. Execute:

```
helmfile sync
```

## Configuring an existing Prometheus server
This section explains how to configure an existing Prometheus server with the recording rules.

To do this, you can do one of the following:

* Annotate the StatefulSet:

```
kubectl -n monitoring patch sts prometheus-server -p '{"spec":{"template":{"metadata":{"annotations":{"prometheus.io/scrape": "true", "prometheus.io/port": "9090"}}}}}'
```

* Download the file `prometheus-deploy.yaml` and apply it:

```
kubectl -n monitoring apply -f prometheus-deploy.yaml
```