# Installing the exporter
To install the exporter, download the file `oracle-db-deployment.yaml`. In the file, you can find an example of how to deploy an Oracle Database  with the [Oracle DB Exporter](https://github.com/iamseth/oracledb_exporter).

To configure the exporter in your own Kubernetes deployment, do the following:

1. Edit the secret `oracledb-exporter-secret`:
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
2. Run the following command and copy the output:
```
echo -n YOUR_CONN_STRING | base64
```

3. Substitute the value for the `datasource` field by the value you have copied. Ensure that `YOUR_CONN_STRING` is a valid Oracle Database connection string format.


A file with custom queries for extra metrics can be found in the `custom-metrics` ConfigMap. You can edit them or add new metrics following the [format defined in the exporter](https://github.com/iamseth/oracledb_exporter/blob/master/multi-metric-dual-example-labels.toml).

# Sysdig Agent configuration

Ensure that the Sysdig Agent configuration has the following configuration to scrape the containers with Prometheus annotations.
```yaml
process_filter:
  - include:
      kubernetes.pod.annotation.prometheus.io/scrape: true
      conf:
        path: "{kubernetes.pod.annotation.prometheus.io/path}"
        port: "{kubernetes.pod.annotation.prometheus.io/port}"
```

You can download the sample configuration file below and apply the changes by:
```bash
kubectl apply -f sysdig-agent-config.yaml
```
