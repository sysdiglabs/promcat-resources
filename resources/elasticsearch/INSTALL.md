# Installing the exporter
To install the exporter follow this steps:
1. You have to know if your elastic is secured or not
2. If it is not secured, just download the file named 'exporter_no_credentials.yaml' and execute:
```
kubectl apply -f exporter_no_credentials.yaml
```
The exporter will try to connect to the service named `elasticsearch` in the port `9200`, so if this is no the port or the service just change these lines
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
3. If the elasticsearch is secured as the same way as the elasticseach deployed in the onprem environments for sysdig then download the file name 'exporter_with_credentials.yaml',
this configuration will works only executing the next command:
```
kubectl apply -f exporter_with_credentials.yaml
```
This configuration will use the user and the password saved as secrets, also will mount a volume with the ca.

4. If you are using the exporter with credentials but you are not using sysdig, then just edit the secrets name, and the service and the port.
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
        - name: ELASTIC_USER
          valueFrom:
            configMapKeyRef:
              key: elasticsearch.adminuser
              name: sysdigcloud-config
        - name: ES_URI
          value: https://$(ELASTIC_USER):$(ELASTICSEARCH_ADMIN_PASSWORD)@sysdigcloud-elasticsearch:9200
      envFrom:
      - secretRef:
          name: elasticsearch-tls
      ...
```
# Sysdig Agent configuration
In the side of Sysdig agent the only thing we have to make sure is the 'promscrape' option is enabled in the dragent.yaml
```yaml
use_promscrape: true
  prometheus:
    enabled: true
    ...
```
