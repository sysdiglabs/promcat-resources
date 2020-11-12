# Configuring MongoDB for the exporter
To install MongoDB, you can download the _mongo-deploy.yaml_ file and run:
```bash
kubectl apply -f mongo-deploy.yaml
```

If you want to use a no-admin user for the exporter, you will have to create the user and grant the roles to be able to scrape statistics. 

In the mongo shell:
```sql
use admin
db.auth("your-admin-user", "your-admin-password")
db.createUser(
   {
      user: "exporter-user",
      pwd: "exporter-pass",
      roles: [ 
        { role: "clusterMonitor", db: "admin" },
        { role: "read", db: "admin" },
        { role: "read", db: "local" } 
      ]
   }
)
```

# Installing the exporter
To install the MongoDB exporter, we will use the [Helm chart](https://github.com/helm/charts/tree/master/stable/prometheus-mongodb-exporter) available. 

First, create a _values.yaml_ file with the following parameters:
```yaml
fullnameOverride: "mongodb-exporter"
podAnnotations:
  prometheus.io/scrape: "true"
  prometheus.io/port: "9216"
serviceMonitor:
  enabled: false
mongodb:
  uri: mongodb://exporter-user:exporter-pass@mongodb:27017
```

Note that the _mongodb.uri_ parameter is a valid [MongoDB URI](https://github.com/prometheus-community/helm-charts/blob/main/charts/prometheus-mongodb-exporter/README.md).
In this URI, include the user and password of the exporter. The Helm chart will create a Kubernetes Secret with the URI so it is not visible. 

To install the exporter, add the helm repository and run the helm install command:
```
# Add repository
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

# Helm 3
helm install  mongodb-exporter prometheus-community/prometheus-mongodb-exporter -f values.yaml

# Helm 2
helm install --name mongodb-exporter prometheus-community/prometheus-mongodb-exporter -f values.yaml
```

The metrics will be available in port 9216 of the exporter pod.

## Using TLS or SSL Authentication
To use TLS or SSL authentication, you will need to use the file `mongodb-exporter-auth-deploy.yaml` and use it to deploy the exporter as the helm chart does not support authentication.

Follow these steps: 

1. Create a text file with the connection string for your MongoDB using these examples: 
```
# TLS
mongodb://mongodb-exporter-user:mongodb-exporter-pass@<YOUR-MONGODB-HOST>:<PORT>/admin?tls=true&tlsCertificateKeyFile=/etc/mongodb/mongodb-exporter-key.pem&tlsAllowInvalidCertificates=true&tlsCAFile=/etc/mongodb/mongodb-exporter-ca.pem

# SSL
mongodb://mongodb-exporter-user:mongodb-exporter-pass@<YOUR-MONGODB-HOST>:<PORT>/admin?ssl=true&sslclientcertificatekeyfile=/etc/mongodb/mongodb-exporter-key.pem&sslinsecure=true&sslcertificateauthorityfile=/etc/mongodb/mongodb-exporter-ca.pem
```
2. Create the secret for the connection string:
```
kubectl create secret generic mongodb-exporter \
  --from-file=mongodb-uri=<route-to-file-with-connection-uri.txt>
```

3. Create the secret with the private key and the certificate authority (CA). If you do not have a CA file, you can use an empty file instead:
```
kubectl create secret generic mongodb-exporter-auth \
  --from-file=mongodb-key=<route-to-your-private-key.pem> \
  --from-file=mongodb-ca=<route-to-your-ca.pem> 
```

1. Download the file `mongodb-exporter-auth-deploy.yaml` and apply it with the following command:
```
kubectl apply -f mongodb-exporter-auth-deploy.yaml
```

# SYSDIG AGENT CONFIGURATION
In the _values.yaml_ of the Helm chart we will include the Prometheus annotations configuring the port of the exporter as scraping port.    

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