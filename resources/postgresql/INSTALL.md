# Prerequisites

### Create Credentials for the Exporter in the Database
If you want to use a no-admin user for the exporter, you will have to create the user and associated views and permissions to be able to gather the data from the tables.

The [Postgres exporter documentation](https://github.com/wrouesnel/postgres_exporter) contains the following script that you can use in your database to create the exporter user:

> Note: Before running the script, be sure to set the correct password for the user in the line:
> `ALTER USER postgres_exporter WITH PASSWORD 'password';`

```sql
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

### Create a Secret with the Credentials
To create the secret with the user and password, you have to take in mind:
* It has to be **in the same namespace where the exporter** will be deployed.
* Use the **same _user name_ and _password_ that you used to create the exporter user in the database** in the previous step.
* You can change the name of the secret. If you do it, you will need to **select it in the next steps** of the integration.

#### Without TLS certs
```sh
kubectl create -n Your-Application-Namespace secret generic postgresql-exporter \
  --from-literal=username=userName \
  --from-literal=password=password
```

#### With TLS certs
```sh
kubectl create -n Your-Application-Namespace secret generic postgresql-exporter \
  --from-literal=username=userName \
  --from-literal=password=password \
  --from-file=sslRootCert=/path/to/tls/cert
```
# Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm install --repo https://sysdiglabs.github.io/integrations-charts postgresql-exporter postgresql-exporter
```