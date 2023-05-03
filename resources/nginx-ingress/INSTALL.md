# Prerequisites


### Enable NGINX Ingress metrics

To enable metric scraping, you should add the following line to the NGINX Ingress configuration file:

```
controller.metrics.enabled=true
```

This parameter should be added in the NGINX Ingress section of the values.yaml file if you're using Helm to deploy the NGINX Ingress, or in the nginx-ingress-controller configuration file if you're using a native Kubernetes installation.

Once you've enabled metric scraping with this parameter, the NGINX Ingress will automatically begin exposing its metrics on port 10254.

Another option is adding the following line to the NGINX Ingress configuration file:

```
controller.metrics.podAnnotations.prometheus.io/scrape=true
```



# Installation

The application is ready to be scraped