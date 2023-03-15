## Prerequisites


### Enable Nginx _stub_status_ Module
The exporter can be installed as a sidecar of the pod with the Nginx server. To make Nginx expose an endpoint for scraping metrics, enable the _stub_status_ module.
If your Nginx configuration is defined inside a Kubernetes ConfigMap, add the following snippet to enable the stub_status module:

```yaml
server {
  listen       80;
  server_name  localhost;
  location /nginx_status {
    stub_status on;
    access_log  on;
    allow all;  # REPLACE with your access policy
  }
}
```

This is how the ConfigMap would look after adding this snippet:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-config
data:
  nginx.conf: |
    server {
      listen       80;
      server_name  localhost;
      location /nginx_status {
        stub_status on;
        access_log  on;
        allow all;  # REPLACE with your access policy
      }
    }
```

## Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm template nginx nginx-exporter --repo https://sysdiglabs.github.io/integrations-charts > patch.yaml
kubectl patch -n namespace workloadType workloadName --patch "$(cat patch.yaml)"
```