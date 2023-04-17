# Prerequisites


### Enable Prometheus Metrics
As seen in the Harbor documentation page [Configure the Harbor YML File](https://goharbor.io/docs/main/install-config/configure-yml-file/), to make Harbor expose an endpoint for scraping metrics, you need to set the 'metric.enabled' configuration to 'true'.

If you install Harbor with Helm, you need to use the following flag:
```
--set 'metrics.enabled=true'
```# Installation

The application is ready to be scraped