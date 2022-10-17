# Alerts
## KubeCPUOvercommit
Cluster has overcommitted CPU resource requests for Pods and cannot tolerate node failure.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubecpuovercommit)

## KubeMemOvercommit
Cluster has overcommitted memory resource requests for Pods and cannot tolerate node failure.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubememovercommit)

## KubeCPUOvercommit
Cluster has overcommitted CPU resource requests for Namespaces.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubecpuovercommit)

## KubeMemOvercommit
Cluster has overcommitted memory resource requests for Namespaces.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubememovercommit)

## KubeQuotaExceeded
Namespace exceeded its quota.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubequotaexceeded)

## CPUThrottlingHigh
Throttling of CPU in namespace for container in pod.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh)

## KubePersistentVolumeUsageCritical
The PersistentVolume claimed in Namespace usage is critical.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepersistentvolumeusagecritical)

## KubePersistentVolumeFullInFourDays
Based on recent sampling, the PersistentVolume claimed in the Namespace is expected to fill up within four days

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepersistentvolumefullinfourdays)

## KubePersistentVolumeErrors
The persistent volume has bad status.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepersistentvolumeerrors)

## KubeVersionMismatch
There are different semantic versions of Kubernetes components running.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeversionmismatch)

## KubeClientErrors
Kubernetes API server client is experiencing errors.'

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeclienterrors)

## ErrorBudgetBurn
High requests error budget burn for job=kube-apiserver

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-errorbudgetburn)

## ErrorBudgetBurn
High requests error budget burn for job=kube-apiserver

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-errorbudgetburn)

## KubeAPILatencyHigh
The API server has an abnormal latency.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapilatencyhigh)

## KubeAPILatencyHigh
The API server has a 99th percentile latency.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapilatencyhigh)

## KubeAPIErrorsHigh
API server is returning high number errors.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapierrorshigh)

## KubeClientCertificateExpiration
A client certificate used to authenticate to the apiserver is expiring in less than 7.0 days.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeclientcertificateexpiration)

## KubeClientCertificateExpiration
A client certificate used to authenticate to the apiserver is expiring in less than 24.0 hours.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeclientcertificateexpiration)

## AggregatedAPIErrors
An aggregated API has reported errors. The number of errors have increased for it in the past five minutes. High values indicate that the availability of the service changes too often.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-aggregatedapierrors)

## AggregatedAPIDown
An aggregated API is down. It has not been available at least for the past five minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-aggregatedapidown)

## KubeAPIDown
KubeAPI has disappeared from Prometheus target discovery.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapidown)

## KubeNodeNotReady
One node has been unready for more than 15 minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubenodenotready)

## KubeNodeUnreachable
One node is unreachable and some workloads may be rescheduled.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubenodeunreachable)

## KubeletTooManyPods
Kubelet is running out of its Pod capacity.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubelettoomanypods)

## KubeNodeReadinessFlapping
The readiness status of node has changed the value several times in the last 15 minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubenodereadinessflapping)

## KubeletPlegDurationHigh
The Kubelet Pod Lifecycle Event Generator has a 99th percentile duration of {{ $value }} seconds on node {{ $labels.node }}.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeletplegdurationhigh)

## KubeletPodStartUpLatencyHigh
Kubelet Pod startup 99th percentile latency is high.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeletpodstartuplatencyhigh)

## KubeletDown
Kubelet has disappeared from Prometheus target discovery.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeletdown)

## KubeSchedulerDown
KubeScheduler has disappeared from Prometheus target discovery.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeschedulerdown)

## KubeControllerManagerDown
KubeControllerManager has disappeared from Prometheus target discovery.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubecontrollermanagerdown)
