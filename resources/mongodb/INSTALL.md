## Prerequisites

### Create Credentials for MongoDB Exporter

If you want to use a non-admin user for the exporter, you will have to create a user and grant the roles to be able to scrape statistics.

In the mongo shell:
```sql
use admin
db.auth("<YOUR-ADMIN-USER>", "<YOUR-ADMIN-PASSWORD>")
db.createUser(
   {
      user: "<YOUR-EXPORTER-USER>",
      pwd: "<YOUR-EXPORTER-PASSWORD>",
      roles: [
        { role: "clusterMonitor", db: "admin" },
        { role: "read", db: "admin" },
        { role: "read", db: "local" }
      ]
   }
)
```

### Create Kubernetes Secret for Connection and Authentication
To configure authentication, do the following:

1. Create a text file with the connection string (mongodb-uri) for your MongoDB by using these examples:
  ```
 # Basic authentication
  mongodb://<YOUR-EXPORTER-USER>:<YOUR-EXPORTER-PASSWORD>@<YOUR-MONGODB-HOST>:<PORT>

  # TLS
  mongodb://<YOUR-EXPORTER-USER>:<YOUR-EXPORTER-PASSWORD>@<YOUR-MONGODB-HOST>:<PORT>/admin?tls=true&amp;tlsCertificateKeyFile=/etc/mongodb/mongodb-exporter-key.pem&amp;tlsAllowInvalidCertificates=true&amp;tlsCAFile=/etc/mongodb/mongodb-exporter-ca.pem

  # SSL
  mongodb://<YOUR-EXPORTER-USER>:<YOUR-EXPORTER-PASSWORD>@<YOUR-MONGODB-HOST>:<PORT>/admin?ssl=true&amp;sslclientcertificatekeyfile=/etc/mongodb/mongodb-exporter-key.pem&amp;sslinsecure=true&amp;sslcertificateauthorityfile=/etc/mongodb/mongodb-exporter-ca.pem
  ```
2. Create the secret for the connection string:
  ```
  kubectl create secret -n Your-Exporter-Namespace generic Your-Mongodb-Uri-Secret-Name \
    --from-file=mongodb-uri=<route-to-file-with-mongodb-uri.txt>
  ```
3. In case of TLS or SSL authentication, create the secret with the private key and the certificate authority (CA). If you do not have a CA file, you can use an empty file instead:
  ```
  kubectl create secret -n Your-Exporter-Namespace generic mongodb-exporter-auth \
    --from-file=mongodb-key=<route-to-your-private-key.pem> \
    --from-file=mongodb-ca=<route-to-your-ca.pem>
  ```

## Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm install --repo https://sysdiglabs.github.io/integrations-charts mongodb-exporter mongodb-exporter
```