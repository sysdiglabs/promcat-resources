# OPA
Open Policy Agent, OPA in short, is a general purpose policy engine. It uses a declarative language known as Rego and can be used to answer the following:

  - Admission control: Ensure that only the container images without vulnerabilities can be deployed
  - API authorization: Can user X perform operation Y on source Z?
  - SSH & sudo authorization: Only the on-call team members can SSH into production
  - Data protection and data filtering
OPA has integrations with many cloud-native projects, including Kubernetes and Istio, or Sysdig. If you are looking at how to allow or deny scheduling pods based on image scanning results, check out our blog, performing image scanning on Admission Controller with OPA.

For further information, see [How to monitor OPA Gatekeeper with Prometheus metrics](https://sysdig.com/blog/monitor-gatekeeper-prometheus/).

# Attributions
The configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/).
