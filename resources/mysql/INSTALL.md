# Prerequisites

### Create Credentials for MySQL Exporter

1. Create the user and password for the exporter in the database:
  ```sql
  CREATE USER 'exporter' IDENTIFIED BY 'YOUR-PASSWORD' WITH MAX_USER_CONNECTIONS 3;
  GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter';
  ```
  > Replace the user name and the password in the SQL sentence for your custom ones.

2. Create a *mysql-exporter.cnf* file with the credentials of the exporter:
  ```ini
  [client]
  user = exporter
  password = "YOUR-PASSWORD"
  host=YOUR-DB-IP
  ```

3. In your cluster, create the secret with the *mysql-exporter.cnf* file. This file will be mounted in the exporter to authenticate with the database:
  ```
  kubectl create secret -n Your-Application-Namespace generic mysql-exporter \
    --from-file=.my.cnf=./mysql-exporter.cnf
  ```

### Using SSL Authentication

If your database requires SSL authentication, you need to create secrets with the certificates.
To do so, create the secret with SSL certificates for the exporter:
```
kubectl create secret -n Your-Application-Namespace generic mysql-exporter \
  --from-file=.my.cnf=./mysql-exporter.cnf
  --from-file=ca.pem=./certs/ca.pem \
  --from-file=client-key.pem=./certs/client-key.pem \
  --from-file=client-cert.pem=./certs/client-cert.pem
```

In the *mysql-exporter.cnf* file, include the following lines to route to the certificates in the exporter:
```ini
[client]
user = exporter
password = "YOUR-PASSWORD"
host=YOUR-DB-IP
ssl-ca=/lib/cert/ca.pem
ssl-key=/lib/cert/client-key.pem
ssl-cert=/lib/cert/client-cert.pem
```# Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm install --repo https://sysdiglabs.github.io/integrations-charts mysql-exporter mysql-exporter
```