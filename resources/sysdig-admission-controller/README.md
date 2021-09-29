# Sysdig Admission Controller
Kubernetes' admission controllers help you define and customize which requests are allowed on your cluster. An admission controller intercepts and processes requests to the Kubernetes API prior to persistence of the object, but after the request is authenticated and authorized.

Sysdig’s Admission Controller builds upon Kubernetes and enhances the capacity of the image scanner to check images for Common Vulnerabilities and Exposures (CVEs), misconfigurations, outdated images, etc., elevating the scan policies from detection to actual prevention. Container images that do not fulfill the configured admission policies will be rejected from the cluster before being assigned to a node and allowed to run.

# Metrics
Sysdig Admission Controller expose metrics on:
* Kubernetes Audit Events
* Image scanning
* Procession queues
* Inline image scanning metrics

# Number of time series generated
Sysdig Admission Controller generates around 150 metrics per admission controller.

# Attributions
Configuration files, alerts, and dashboards are maintained by [Sysdig team](https://sysdig.com/).
