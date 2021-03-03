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
# Sysdig Agent configuration
To use the Sysdig agent, first create the recording rules to scrape only the metrics that will be use in the dashboards.

1. Copy the agent configuration provided and save it as `sysdig-agent.yaml`. Then apply it:

```
kubectl apply -f sysdig-agent.yaml
```
