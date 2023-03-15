## Prerequisites

### Create the Secrets
Keep in mind:
* If your ElasticSearch cluster is using basic authentication, the secret that contains the url must have the user and password.
* The secrets need to be created **in the same namespace where the exporter** will be deployed.
* Use the **same _user name_ and _password_ that you used for the api**.
* You can change the name of the secret. If you do this, you will need to **select it in the next steps** of the integration.

#### Create the Secret for the URL
##### Without Authentication
```sh
kubectl -n Your-Application-Namespace create secret generic elastic-url-secret \
  --from-literal=url='http://SERVICE:PORT'
```

##### With Basic Auth
```sh
kubectl -n Your-Application-Namespace create secret generic elastic-url-secret \
  --from-literal=url='https://USERNAME:PASSWORD@SERVICE:PORT'
```
NOTE: You can use either http or https in the URL.

#### Create the Secret for the TLS Certs
If you are using HTTPS with custom certificates, follow the instructions given below.
```sh
kubectl create -n Your-Application-Namespace secret generic elastic-tls-secret \
  --from-file=root-ca.crt=/path/to/tls/ca-cert \
  --from-file=root-ca.key=/path/to/tls/ca-key \
  --from-file=root-ca.pem=/path/to/tls/ca-pem
```


## Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm install --repo https://sysdiglabs.github.io/integrations-charts elasticsearch-exporter elasticsearch-exporter
```