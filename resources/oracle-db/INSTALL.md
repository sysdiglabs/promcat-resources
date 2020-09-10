# Installing the exporter
To install the exporter, download the file `oracle-db-deployment.yaml`. There you can find an example of how to deploy an Oracle Database along with the [Oracle DB Exporter](https://github.com/iamseth/oracledb_exporter).

To configure the exporter in your own Kubernetes deployment, you will have to edit the secret `oracledb-exporter-secret`: 
```yaml
apiVersion: v1
kind: Secret
metadata:
  name:  oracledb-exporter-secret
  namespace: database-namespace
data:
    # Add here the result of: 
    # echo -n YOUR_CONN_STRING | base64 
    # YOUR_CONN_STRING be like: system/YOUR-PASSWORD-FOR-SYSTEM@//database:1521/DB_SID.DB_DOMAIN
    datasource: XXX
type: Opaque
```

Just substitute the value for the `datasource` field by the result of the following command, being `YOUR_CONN_STRING` a valid Oracle Database connection string format: 
```
echo -n YOUR_CONN_STRING | base64
```

A file with custom queries for extra metrics can be found in the ConfigMap `custom-metrics`. You can edit them or add new metrics following the [format defined in the exporter](https://github.com/iamseth/oracledb_exporter/blob/master/multi-metric-dual-example-labels.toml). 

# Sysdig Agent configuration
In the Sysdig Agent configuration, be sure to have these lines of configuration to scrape the containers with Prometheus annotations.
```yaml
process_filter:
  - include:
      kubernetes.pod.annotation.prometheus.io/scrape: true
      conf:
        path: "{kubernetes.pod.annotation.prometheus.io/path}"
        port: "{kubernetes.pod.annotation.prometheus.io/port}"
```

You can download the sample configuration file below and apply it by:
```bash
kubectl apply -f sysdig-agent-config.yaml
```