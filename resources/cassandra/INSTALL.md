## Prerequisites

### Create ConfigMap for the JMX-Exporter
The JMX-Exporter requires a ConfigMap with the Cassandra JXM configurations, which can be easily installed using a simple command.
The following example is for a Cassandra cluster which exposes the jmx port 7199 and it's deployed in the 'cassandra' namespace (modify the jmx port and the namespace as per your needs):

```
helm repo add promcat-charts https://sysdiglabs.github.io/integrations-charts 
helm repo update
helm -n cassandra install cassandra-jmx-exporter promcat-charts/jmx-exporter --set jmx_port=7199 --set integrationType=cassandra --set onlyCreateJMXConfigMap=true
```

## Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm template cassandra jmx-exporter --repo https://sysdiglabs.github.io/integrations-charts > patch.yaml
kubectl patch -n namespace workloadType workloadName --patch "$(cat patch.yaml)"
```