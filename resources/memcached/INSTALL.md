## Prerequisites



## Installation

You can use our helm-charts in order to install the exporter in your cluster.
```sh
helm template memcached memcached-exporter --repo https://sysdiglabs.github.io/integrations-charts > patch.yaml
kubectl patch -n namespace workloadType workloadName --patch "$(cat patch.yaml)"
```