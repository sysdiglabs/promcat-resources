# Prerequisites

### Create Grok Configuration
You need to add the Grok configuration in order to parse Apache logs and get metrics from them.

### Install It Directly In Your Cluster
```sh
helm install -n Your-Application-Namespace apache-exporter --repo https://sysdiglabs.github.io/integrations-charts --set configmap=true
```

### Download and Apply 
You can download the file and execute the next command

```sh
kubectl -n Your-Application-Namespace apply -f grok-configmap.yaml
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: grok-config
data:
  config.yml: |
    global:
      config_version: 3
    input:
      type: file
      path: /tmp/logs/accesss.log
      fail_on_missing_logfile: false
      readall: true
    imports:
    - type: grok_patterns
      dir: ./patterns
    metrics:
    - type: counter
      name: apache_http_response_codes_total
      help: HTTP requests to Apache
      match: '%{COMMONAPACHELOG}'
      labels:
        code: '{{.response}}'
        method: '{{.verb}}'
    - type: gauge
      name: apache_http_response_bytes_total
      help: Size of HTTP responses
      match: '%{COMMONAPACHELOG}'
      value: '{{.bytes}}'
      cumulative: true
      labels:
        code: '{{.response}}'
        method: '{{.verb}}'
    - type: gauge
      name: apache_http_last_request_seconds
      help: Timestamp of the last HTTP request
      match: '%{COMMONAPACHELOG}'
      value: '{{timestamp "02/Jan/2006:15:04:05 -0700" .timestamp}}'
      labels:
        code: '{{.response}}'
        method: '{{.verb}}'
    server:
      protocol: http
```

### Check Apache Configuration
Apache provides metrics in its own format via its ServerStatus module. To enable this module, include (or uncomment) the following line in your apache configuration file:

```
LoadModule status_module modules/mod_status.so
<Location "/server-status">
  SetHandler server-status
</Location>
```

To configure Apache server to produce common logs, include (or uncomment) the following in your Apache configuration file:

```
<IfModule log_config_module>
       LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
       CustomLog /usr/local/apache2/logs/accesss.log common
</IfModule>
```
# Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm template apache apache-exporter --repo https://sysdiglabs.github.io/integrations-charts > patch.yaml
kubectl patch -n namespace workloadType workloadName --patch "$(cat patch.yaml)"
```