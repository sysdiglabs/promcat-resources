# Installing the exporter
## Without credentials
If it is not secured, download the `exporter_no_credentials.yaml` file and execute:
```
kubectl apply -f exporter_no_credentials.yaml
```
The exporter will try to connect to the service named `elasticsearch` on the port `9200`. If this is not the port or the service, change these lines:
```yaml
- name: ES_URI
  value: https://elasticsearch:9200
```
Located here
```yaml
...
spec:
  template:
    spec:
      containers:
      - command:
      ...
        env:
          - name: ES_URI
            value: https://elasticsearch:9200
      ...
```
## With credentials
If elasticsearch is secured, download the `exporter_with_credentials.yaml` file. 

This configuration will use the user and the password saved as secrets, and will mount a volume with the ca certificate.

Create the secret with the ElasticSearch certificates for the exporter and edit in the yaml file:
* Secrets name (by default `elasticsearch-tls` and `es-certs`)
* Service
* Host
* Port

```yaml
...
spec:
  template:
    spec:
      containers:
      - command:
      ...
        env:
        - name: ELASTIC_USER
          valueFrom:
            configMapKeyRef:
              key: elasticsearch.adminuser
              name: sysdigcloud-config
        - name: ES_URI
          value: https://$(ELASTIC_USER):$(ELASTICSEARCH_ADMIN_PASSWORD)@YOUR-HOST:9200
      envFrom:
      - secretRef:
          name: elasticsearch-tls
      ...
```

Apply by configuration changes by executing the following:
```
kubectl apply -f exporter_with_credentials.yaml
```
# Sysdig Agent configuration
> Requires Sysdig Agent >= v11.3 

In the ElasticSearch exporter deployment, use the Sysdig annotations to configure the port of the exporter as scraping port. You can see an example in the `exporter_no_credentials.yaml` file.

Additionally, you can use these labels to add the namespace, workload type, and name of the database the exporter will retrieve the data from.

```yaml
spec:
  template:
    metadata:
      annotations:
        promcat.sysdig.com/integration_type: elasticsearch
        promcat.sysdig.com/port: "9108"
        # Add here the namespace, workload type (deployment, statefulset, replicaset, daemonset) 
        # and workload name of the instance that the exporter will take data from
        promcat.sysdig.com/target_ns: elastic-namespace
        promcat.sysdig.com/target_workload_type: statefulset
        promcat.sysdig.com/target_workload_name: elasticsearch
```
This way, on Sysdig Monitor, you can view the associated metrics corresponding to ElasticSearch pods and the exporter.

After you configure the Sysdig annotations, download the sample configuration file and apply it by:
```bash
kubectl apply -f sysdig-agent-config.yaml
```