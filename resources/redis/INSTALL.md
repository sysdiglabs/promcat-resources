# Prerequisites

### Basic Authentication
Follow these steps if your Redis server requires user and password authentication

1.- Create a user and password in your Redis instance for the exporter.
```
ACL SETUSER USERNAME +client +ping +info +config|get +cluster|info +slowlog +latency +memory +select +get +scan +xinfo +type +pfcount +strlen +llen +scard +zcard +hlen +xlen +eval allkeys on >PASSWORD
```
Replace `USERNAME` and `PASSWORD` with yours for the Redis instance.

2.- Create a secret with the user and password for the exporter. Keep the following in mind:

- It has to be **in the same namespace where the exporter** will be deployed.
- Use the **same _user name_ and _password_ that you used for the api** in the previous step.
- You can change the name of the secret. If you do it, you will need to **select it in the next steps** of the integration.
```
kubectl create secret -n Your-Application-Namespace generic redis-exporter-auth \
  --from-literal=user=USER \
  --from-literal=password=PASSWORD
```
Replace `USER` and `PASSWORD` with yours for the Redis instance.
# Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm install --repo https://sysdiglabs.github.io/integrations-charts redis-exporter redis-exporter
```