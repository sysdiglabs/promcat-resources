# Installing the exporter
The Istio components that are installed are the exporters with endpoints. When you install Istio with the `istioctl` tool a prometheus server is installed by default with the configuration to get all the targets.

If you want the targets in your prometheus server, do one of the following:

* Federate the prometheus (simplest method)
* Annotate all the pods and sidecars (complex method)

# Gather the metrics from the prometheus server deployed by Istio

The Prometheus server provided by Istio includes all the targets with all the associated metrics.

1. Create the rules with the only metrics you need from the `recording rules`  tab downloaded as `rules.yaml`.
  ```
  kubectl  apply -f rules.yaml
  ```

2. Mount the new rules in the Prometheus server:
  ```sh
  kubectl -n istio-system patch deploy prometheus -p '{"spec":{"template":{"spec":{"volumes":[{"name":"config-rules","configMap":{"defaultMode":420,"name":"rules"}}]}}}}'

  kubectl -n istio-system patch deploy prometheus -p '{"spec":{"template":{"spec":{"containers":[{"name":"prometheus","volumeMounts": [{"mountPath": "/opt/rules","name": "config-rules"}]}]}}}}'

  kubectl -n istio-system patch deploy prometheus -p '{"spec":{"template":{"metadata":{"annotations":{"prometheus.io/scrape": "true", "prometheus.io/path": "/federate", "prometheus.io/port": "9090"}}}}}'
  ```

3. Update the prometheus to get the new rules:
  ```
  kubectl -n istio-system edit cm prometheus
  ```

  ```yaml
  global:
    scrape_interval: 15s
  rule_files:
  - /opt/rules/rules.yaml
  ```
  As the prometheus server doesn't have any pod to reload the configuration and the API is not active, delete it in order to get the new configuration.

4. Delete the pod being xxx the id given to the pods:
  ```sh
  kubectl -n istio-system delete pods $(kubectl get pods --namespace istio-system -l "app=prometheus,release=istio" -o jsonpath="{.items[0].metadata.name}")
  ```

5. Gather the metrics with the agent adding the federation job for Istio. Given below is an example of the configmap:

  ```yaml
  - job_name: 'prometheus' # config for federation
        honor_labels: true
        metrics_path: '/federate'
        metric_relabel_configs:
        - regex: 'kubernetes_pod_name'
          action: labeldrop
        params:
          'match[]':
            - '{sysdig="true"}'
        sysdig_sd_configs:
        - tags:
            namespace: istio-system
            deployment: prometheus
  ```
  Use the file named `patch.yaml`  to patch it:
  ```
  kubectl -n sysdig-agent patch cm sysdig-agent -p "$(cat patch.yaml)"
  ```
  Alternatively, apply the `sysdig-agent` confimap provided:
  ```
  kubectl -n sysdig-agent apply -f sysdig-agent.yaml
  ```
