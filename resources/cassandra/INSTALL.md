# Installing the exporter
Cassandra exposes the metrics via JMX (Java Management Extensions). The exporter filter these metrics using jmx-config file and exposes them in Prometheus format. Usually JMX is unsecured and it has no authentication methods. In this case, the best way to deploy JMX metrics is to add a sidecar with the exporter.

## Steps to install

1.- Create the following ConfiMap (you must specify the namespace where you have Cassandra deployed inside jmx-config.yaml file):

```
kubectl apply -f jmx-config.yaml
```

2.- Deploy exporter as sidecar running the following command:

```
kubectl patch sts -n cassandra cassandra-sts --patch https://raw.githubusercontent.com/sysdiglabs/promcat-resources/master/resources/cassandra/include/patch.yaml
```

Alternatively, you can download the file and run:

```
kubectl patch sts -n cassandra cassandra-sts --patch "$(cat patch.yaml)"
```