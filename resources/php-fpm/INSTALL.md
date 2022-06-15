# Prerequisites

In addition to having PHP-FPM desployed in Kubernetes, a Prometheus exporter is also necessary. The exporter can be installed as a sidecar of the pod with the PHP-FPM server. In order to get a metrics endpoint for the php-fpm service, you need to enable the status endpoint in the PHP-FPM service configuration.

```
apiVersion: v1
kind: ConfigMap
metadata:
    labels:
      app: php-fpm
    name: php-fpm-config
    namespace: php-fpm
data:
  www.conf: |
    ...
    pm.status_path=/status
    ...
```


You can find a deployment below with the exporter as a sidecar and the ConfigMap with the configuration required to scrape metrics from the server.
