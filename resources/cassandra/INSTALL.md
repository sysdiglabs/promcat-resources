# Prerequisites
The cassandra exporter generates a high number of metrics. As the Sysdig Agent has a limit of time series that can send to Sysdig Monitor, you have to deploy a Prometheus server and create the recording rules that we provide to filter only the metrics used in dashboards and alerts.

To deploy a Prometheus server you will need:
* [helm](https://helm.sh/docs/intro/install/)  
* [helmfile](https://github.com/roboll/helmfile)

# Installing the exporter
Cassandra expose the metrics with jmx and the exporter gather this metrics and expose them in Prometheus format. Usually jmx is unsecured and it has not user or password. In this case, the best way to deploy it is to add a sidecar with the exporter.

```yaml
    - name: cassandra-exporter
      image: gcr.io/mateo-burillo-ns/promcat-cassandra-exporter:latest
      imagePullPolicy: Always
      volumeMounts:
      - mountPath: /var/lib/cassandra
        name: data
      ports:
      - name: metrics
        containerPort: 9500
        protocol: TCP
      livenessProbe:
        tcpSocket:
          port: 9500
        initialDelaySeconds: 180
      readinessProbe:
        httpGet:
          path: /metrics
          port: 9500
        initialDelaySeconds: 180
        timeoutSeconds: 45
```

# Installing and configuring Prometheus
## Installing a new Prometheus with helm
In this section we will explain how to install and configure a new prometheus server with the recording rules.  

Download the following files: 
- helmfile.yaml
- recording_rules.yaml
- prometheus.yaml
- prometheus.yml.gotmpl

execute

```
helmfile sync
```

# Sysdig Agent configuration
To use the Sysdig agent, first create the recording rules to scrape only the metrics that will be use in the dashboards.

1. Copy the agent configuration provided and save it as `sysdig-agent.yaml`. Then apply it:

```
kubectl apply -f sysdig-agent.yaml
```
