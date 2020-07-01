# Configuring Postgres for the exporter
## For existing databases
If you want to use a no-admin user for the exporter, you will have to create the user and the views and permissions to
be able to gather the data from the tables. In the [Postgres exporter documentation](https://github.com/wrouesnel/postgres_exporter) there is the following script 
that you can use in your database to create the exporter user:
```sql
-- To use IF statements, hence to be able to check if the user exists before
-- attempting creation, we need to switch to procedural SQL (PL/pgSQL)
-- instead of standard SQL.
-- More: https://www.postgresql.org/docs/9.3/plpgsql-overview.html
-- To preserve compatibility with <9.0, DO blocks are not used; instead,
-- a function is created and dropped.
CREATE OR REPLACE FUNCTION __tmp_create_user() returns void as $$
BEGIN
  IF NOT EXISTS (
          SELECT                       -- SELECT list can stay empty for this
          FROM   pg_catalog.pg_user
          WHERE  usename = 'postgres_exporter') THEN
    CREATE USER postgres_exporter;
  END IF;
END;
$$ language plpgsql;

SELECT __tmp_create_user();
DROP FUNCTION __tmp_create_user();

ALTER USER postgres_exporter WITH PASSWORD 'password';
ALTER USER postgres_exporter SET SEARCH_PATH TO postgres_exporter,pg_catalog;

-- If deploying as non-superuser (for example in AWS RDS), uncomment the GRANT
-- line below and replace <MASTER_USER> with your root user.
-- GRANT postgres_exporter TO <MASTER_USER>;
CREATE SCHEMA IF NOT EXISTS postgres_exporter;
GRANT USAGE ON SCHEMA postgres_exporter TO postgres_exporter;
GRANT CONNECT ON DATABASE postgres TO postgres_exporter;

CREATE OR REPLACE FUNCTION get_pg_stat_activity() RETURNS SETOF pg_stat_activity AS
$$ SELECT * FROM pg_catalog.pg_stat_activity; $$
LANGUAGE sql
VOLATILE
SECURITY DEFINER;

CREATE OR REPLACE VIEW postgres_exporter.pg_stat_activity
AS
  SELECT * from get_pg_stat_activity();

GRANT SELECT ON postgres_exporter.pg_stat_activity TO postgres_exporter;

CREATE OR REPLACE FUNCTION get_pg_stat_replication() RETURNS SETOF pg_stat_replication AS
$$ SELECT * FROM pg_catalog.pg_stat_replication; $$
LANGUAGE sql
VOLATILE
SECURITY DEFINER;

CREATE OR REPLACE VIEW postgres_exporter.pg_stat_replication
AS
  SELECT * FROM get_pg_stat_replication();

GRANT SELECT ON postgres_exporter.pg_stat_replication TO postgres_exporter;
```
> Note: Before running the script, be sure to set the correct password for the user in the line:
> 
> _ALTER USER postgres_exporter WITH PASSWORD 'password';_

## For new databases
This script is included in the _postgresql-deploy.yaml_ file for newly created databases. 

The script is split and mounted in the database container as two volumes in the _/docker-entrypoint-initdb.d/_ directory. 
* The first file is located in the ConfigMap _postgres-init_ and creates the user, views and permissions. 
* The second file is located in the Secret _postgres-secret_ and sets the password of the exporter user. 

# Installing the exporter
We will explain how to install the exporter as a sidecar of a postgres database. First, download the _postgresql-deploy.yaml_ file. 

In the Deployment, you can find 2 containers, one for the postgres database and another one for the exporter. In the container for the postgres server you can configure: 
* Environment variables from ConfigMap _postgres-config_: POSTGRES_DB, POSTGRES_USER
* Environment variables from Secret _postgres-secret_: POSTGRES_PASSWORD

In the container of the exporter you can configure: 
* Environment variable for the database to export: DATA_SOURCE_URI
* Environment variable for database autodiscovery: PG_EXPORTER_AUTO_DISCOVER_DATABASES
* Environment variable for DATA_SOURCE_USER in the ConfigMap _postgres-config_
* Environment variable for POSTGRES_EXPORTER_PASSWORD in the Secret _postgres-secret_
* Environment variable to the path of the user queries file. This is mounted as a volume in _/tmp/queries.yaml_ from the ConfigMap _postgres-queries_

## User queries
The Postgres Exporter allows to create user defined metrics based on SQL queries. 

The queries added in the ConfigMap _postgres-queries_ are based in the ones available in the [Postgres exporter repository](https://github.com/wrouesnel/postgres_exporter). 
The metrics from _pg_stat_statements_ has beed removed to avoid high cardinality scenarios caused by the _queryid_ label. 

# SYSDIG AGENT CONFIGURATION
In the Postgres Deployment we will include the Prometheus annotations configuring the port of the exporter as scraping port.    

Also, in the Sysdig Agent configuration, be sure to have these lines of configuration to scrape the containers with Prometheus annotations.
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