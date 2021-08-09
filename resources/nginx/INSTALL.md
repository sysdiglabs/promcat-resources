# Installing the exporter
The exporter can be installed as a sidecar of the pod with the Nginx server. In order to get the nginx a endpoint to scrap the metrics you have to enable the metrics endpoint.

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

You can find a deployment below with the exporter as a sidecar and the ConfigMap with the configuration required to scrape metrics from the server.

Also, be sure to add the following annotations to the deployment:

```yaml
spec:
  template:
    metadata:
      annotations:
        promcat.sysdig.com/integration_type: nginx
        promcat.sysdig.com/port: "9113"
```

# Sysdig Agent configuration
Below you can find the configuration for the sysdig agent.