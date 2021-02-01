# Installing the exporter
In order to expose the metrics you have to configure the docker engine with the next file like the [documentation](https://docs.docker.com/config/daemon/prometheus/) says:

To configure the Docker daemon as a Prometheus target, you need to specify the metrics-address. The best way to do this is via the daemon.json, which is located at one of the following locations by default. If the file does not exist, create it.

- **Linux**: `/etc/docker/daemon.json`
- **Windows Server**: `C:\ProgramData\docker\config\daemon.json`
- **Docker Desktop for Mac / Docker Desktop for Windows**: Click the Docker icon in the toolbar, select **Preferences**, then select **Daemon**. Click **Advanced**.

```json
{
  "metrics-addr" : "127.0.0.1:9323",
  "experimental" : true
}
```

# Sysdig Agent configuration
For the Sysdig Agent to discover and scrape it automatically, enable the promscrape option in the agent configuration. You will get an example of the sysdig agent in the section below

```yaml
  prometheus.yaml: |
    global:
      scrape_interval: 10s
    scrape_configs:
    - job_name: docker
      static_configs:
        - targets:
          - localhost:9323
  dragent.yaml: |-
    use_promscrape: true
    prometheus:
      enabled: true
      prom_service_discovery: true
```