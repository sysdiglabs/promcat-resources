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