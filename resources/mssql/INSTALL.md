# Prerequisites
In order to get access to the tables you should create a user with the right permissions or use one with the right permissions.

# Installing the exporter
To deploy the [SQL Exporter](https://github.com/free/sql_exporter) you have to deploy the deployment that is specified below or the image in your cluster or machine.

To configure the exporter in your Kubernetes deployment, you can install the deployment with a configmap and write the username and password as given below:

```yaml
target:
  # Data source name always has a URI schema that matches the driver name. In some cases (e.g. MySQL)
  # the schema gets dropped or replaced to match the driver expected DSN format.
  data_source_name: 'sqlserver://USER:PASSWORD@mssql:1433'
```

The configmap has a `custom-metrics` inside with a series of SLQ queries. You can add more queries to the configmap if required.
