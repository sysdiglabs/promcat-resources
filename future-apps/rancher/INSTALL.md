# Prerequisites
## Enable monitoring
Rancher can deploy a Prometheus server. To get a default monitoring you have to enable it in the monitoring tab.

# Gather the metrics from the prometheus deployed by Rancher
For the control plane metrics, the services are not created by default. To get them in the Prometheus server you have to create new services and seviceMonitors. 

1. Apply the services:
```bash
kubectl apply -f services.yaml
```
2. Apply the serviceMonitor:
```bash
kubectl apply -f service-monitor.yaml
```
