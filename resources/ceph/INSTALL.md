# Make sure the Sysdig agent has the right configuration
Ceph instruments Prometheus metrics and annotates the manager pod with Prometheus annotations, so there is not further configuration needed.

For the Sysdig Agent to discover and scrape it automatically, enable the promscrape option in the agent configuration.

```yaml
  dragent.yaml: |-
    use_promscrape: true
    prometheus:
      enabled: true
      prom_service_discovery: true
```