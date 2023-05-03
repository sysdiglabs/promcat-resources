# Prerequisites

### Enable Status Path
For the exporter to generate metrics, you need to configure some parameters in PHP-FPM to expose the status path. These configuration parameters are:
- pm.status_path
- listen

Here is an example of how to configure them in Kubernetes:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
    labels:
      app: php-fpm
    name: php-fpm-config
    namespace: php-fpm
data:
  www.conf: |
    [www]
    listen=127.0.0.1:9000
    pm.status_path=/status

apiVersion: apps/v1
kind: Deployment
metadata:
  name: php-fpm-app
  namespace: php-fpm
  labels:
    app: php-fpm
    pod: php-app
spec:
  selector:
    matchLabels:
      app: php-fpm
  replicas: 3
  template:
    metadata:
      labels:
        app: php-fpm
        pod: php-app
    spec:
      containers:
      - image: php:7.2-fpm
        imagePullPolicy: Always
        name: php-fpm
        ports:
        - containerPort: 9000
          protocol: TCP
        # Config-map include
        volumeMounts:
          - name: php-fpm-config
            mountPath: /usr/local/etc/php-fpm.d/www.conf
            subPath: www.conf
      volumes:
        - configMap:
            defaultMode: 420
            name: php-fpm-config
          name: php-fpm-config
```
# Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm template php-fpm php-fpm-exporter --repo https://sysdiglabs.github.io/integrations-charts > patch.yaml
kubectl patch -n namespace workloadType workloadName --patch "$(cat patch.yaml)"
```