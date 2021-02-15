# Prerequisites
Create the user and password for the exporter in the database: 
```sql
CREATE USER 'exporter'@'%' IDENTIFIED BY 'YOUR-PASSWORD' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'%';
```
> Substitute the user name and the password in the SQL sentence for your custom ones. 

Create a `mysql-exporter.cnf` file with the credentials of the exporter:
```ini
[client]
user = exporter
password = "YOUR-PASSWORD"
host=YOUR-DB-IP
```

Create in your cluster the secret with this file that will be mounted in the exporter to authenticate with teh database: 
```
kubectl create secret generic mysql-exporter \
  --from-file=.my.cnf=./mysql-exporter.cnf
```

## SSL authentication
If your database requires SSL authentication, you need to create the secrets with the certificates:
Create secret with SSL certs for exporter: 
```
kubectl create secret generic mysql-exporter-ssl \
  --from-file=ca.pem=./certs/ca.pem \
  --from-file=client-key.pem=./certs/client-key.pem \
  --from-file=client-cert.pem=./certs/client-cert.pem 
```

In the `mysql-exporter.cnf` file you will need to include the lines to the routes to the certificates in the exporter: 
```ini
[client]
user = exporter
password = "YOUR-PASSWORD"
host=YOUR-DB-IP
ssl-ca=/lib/cert/ca.pem
ssl-key=/lib/cert/client-key.pem
ssl-cert=/lib/cert/client-cert.pem
```

# Installing the exporter
To install the exporter, you can use the example files provided below. 

Use `mysql-exporter.yaml` basic authentication and `mysql-exporter-ssl.yaml` for ssl authentication. 

# Sysdig Agent configuration
The default configuration of the Sysdig agent will detect the Prometheus annotated pod of the exporter and scrape it automatically. 

Also, in the `sysdig-agent-config.yaml` file you can find an example of the minimum configuration needed in the agent. 