## Prerequisites

### Enable Windows Prometheus Metrics

In order to collect metrics from Windows VMs, you need to install the Windows exporter Prometheus agent, and the Prometheus Server.

#### Windows exporter

This component connects to WMI and exposes Windows metrics in Prometheus metric format.

To install this exporter: 
 1. Dowload the latest version from [Windows Exporter repository](https://github.com/prometheus-community/windows_exporter/releases)
 2. Configure the exporter
 3. Run the exporter with `$>.\exporter.exe --config.file=config.yaml`

##### Exporter configuration

You can configure Windows exporter using the `config.yaml` file as follows:

```yaml
# Configuration and more info
# https://github.com/prometheus-community/windows_exporter

collectors:
  enabled: cpu,cs,logical_disk,net,os,service,system,textfile,process
collector:
  textfile:
    directory: C:\Path\metrics\
#  service:
#    services-where: "Name='windows_exporter'"
log:
  level: warn
```

#### Prometheus Agent

This component collects metrics from the Windows exporter and forwards them to Prometheus Server Remote Write endpoint.

To install the agent:
 1. Download the latest version from [Prometheus Repository](https://github.com/prometheus/prometheus/releases)
 2. Configure the agent
 3. Run agent with `$>.\prometheus.exe --enable-feature=agent`

##### Agent Configuration

You can configure Windows exporter using the `prometheus.yaml` file as follows:
```yaml
global:
  scrape_interval: 10s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  
remote_write:
    - url: "https://api.sysdigcloud.com/prometheus/remote/write"
      bearer_token: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      proxy_url: "https://proxy.url:port" # Set the correct proxy url

scrape_configs:
  - job_name: "windows_exporter"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ["localhost:9182"]
    metric_relabel_configs:
      - source_labels: [instance]
        target_label: instance
        regex: '(.*)'
        replacement: 'windows-vm-demo'
```




## Installation

You can use our helm-charts in order to install the exporter in your cluster.