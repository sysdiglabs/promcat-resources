# Make sure the Sysdig agent has the right configuration
In this case you don't need to install any exporter the pod is already annotated and with only the sysdig agent you can scrape it, just make sure to enable the promscrape and that's it.

```yaml
  dragent.yaml: |-
    use_promscrape: true
```