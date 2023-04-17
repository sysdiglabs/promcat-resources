# Prerequisites

### Installation of the JMX-Exporter as a Sidecar
The JMX-Exporter can be easily installed in two steps. 

First deploy the ConfigMap which contains the Kafka JMX configurations. The following example is for a Kafka cluster which exposes the jmx port 9010:
```
helm repo add promcat-charts https://sysdiglabs.github.io/integrations-charts 
helm repo update
helm -n kafka install kafka-jmx-exporter promcat-charts/jmx-exporter --set jmx_port=9010 --set integrationType=kafka --set onlyCreateJMXConfigMap=true
```

Then generate a patch file and apply it to your workload (your Kafka Deployment/StatefulSet/Daemonset). The following example is for a Kafka cluster which exposes the jmx port 9010, and is deployed as a StatefulSet called 'kafka-cp-kafka':
```
helm template kafka-jmx-exporter promcat-charts/jmx-exporter --set jmx_port=9010 --set integrationType=kafka --set onlyCreateSidecarPatch=true > jmx-exporter-sidecar-patch.yaml
kubectl -n kafka patch sts kafka-cp-kafka --patch-file jmx-exporter-sidecar-patch.yaml
```

### Create Secrets for Authentication for the Kafka-Exporter
Your Kafka cluster external endpoints might be secured by using authentication for the clients that want to connect to it (TLS, SASL+SCARM, SASL+Kerberos). 
If you are going to make the Kafka-Exporter (which will be deployed in the next tab) use these secured external endpoints, then you'll need to create Kubernetes Secrets in the following step.
If you prefer using an internal not-secured (plaintext) endpoint for the Kafka-Exporter to connect to the Kafka cluster, then skip this step.

If using TLS, you'll need to create a Secret which contains the CA, the client certificate and the client key. The names of these files must be "ca.crt", "tls.crt" and "tls.key". The name of the secret can be any name that you want. Example:
```
kubectl create secret generic kafka-exporter-certs --from-file=./tls.key --from-file=./tls.crt --from-file=./ca.crt --dry-run=true -o yaml | kubectl apply -f -
```

If using SASL+SCRAM, you'll need to create a Secret which contains the "username" and "password". Example:
```
echo -n 'admin' > username
echo -n '1f2d1e2e67df' > password
kubectl create secret generic kafka-exporter-sasl-scram --from-file=username --from-file=password --dry-run=true -o yaml | kubectl apply -f -
```

If using SASL+Kerberos, you'll need to create a Secret which contains the "kerberos.conf". If the 'Kerberos Auth Type' is 'keytabAuth', it should also contain the "kerberos.keytab". Example:
```
kubectl create secret generic kafka-exporter-sasl-kerberos --from-file=./kerberos.conf --from-file=./kerberos.keytab --dry-run=true -o yaml | kubectl apply -f -
```# Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm install --repo https://sysdiglabs.github.io/integrations-charts jmx-exporter jmx-exporter
```
```sh
helm install --repo https://sysdiglabs.github.io/integrations-charts kafka-exporter kafka-exporter
```