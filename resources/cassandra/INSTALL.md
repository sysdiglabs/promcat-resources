# Installing the exporter
Cassandra exposes the metrics with JMX (Java Management Extensions). The exporter gather this metrics and expose them in Prometheus format. Usually JMX is unsecured and it has no authentication methods. In this case, the best way to deploy JMX metrics is to add a sidecar with the exporter.

```yaml
spec:
  template:
    metadata:
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "9500"
    spec:
      containers:
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

To do so, run the following command:

```
kubectl patch deployment NameOfYourDeployment --patch https://raw.githubusercontent.com/sysdiglabs/promcat-resources/master/resources/cassandra/include/patch.yaml
```

Alternatively, you can download the file and run:

```
kubectl patch deployment NameOfYourDeployment --patch "$(cat patch.yaml)"
```

# Sysdig Agent configuration
To use the Sysdig agent, do the following:

1. Create the recording rules to scrape only the metrics that will be used in the dashboards.

2. Copy the agent configuration provided and save it as `sysdig-agent.yaml`.

3. Apply the configuration:

  ```
  kubectl apply -f sysdig-agent.yaml
  ```
