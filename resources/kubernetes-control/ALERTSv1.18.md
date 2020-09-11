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
Namespace {{ $labels.namespace }} is using {{ $value | humanizePercentage }} of its {{ $labels.resource }} quota.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubequotaexceeded)

## CPUThrottlingHigh
{{ $value | humanizePercentage }} throttling of CPU in namespace {{ $labels.namespace }} for container {{ $labels.container }} in pod {{ $labels.pod }}.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh)

## KubePersistentVolumeUsageCritical
The PersistentVolume claimed by {{ $labels.persistentvolumeclaim }} in Namespace {{ $labels.namespace }} is only {{ $value | humanizePercentage }} free.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepersistentvolumeusagecritical)

## KubePersistentVolumeFullInFourDays
Based on recent sampling, the PersistentVolume claimed by {{ $labels.persistentvolumeclaim }} in Namespace {{ $labels.namespace }} is expected to fill up within four days. Currently {{ $value | humanizePercentage }} is available.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepersistentvolumefullinfourdays)

## KubePersistentVolumeErrors
The persistent volume {{ $labels.persistentvolume }} has status {{ $labels.phase }}.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepersistentvolumeerrors)

## KubeVersionMismatch
There are {{ $value }} different semantic versions of Kubernetes components running.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeversionmismatch)

## KubeClientErrors
Kubernetes API server client '{{ $labels.job }}/{{ $labels.instance }}' is experiencing {{ $value | humanizePercentage }} errors.'

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeclienterrors)

## ErrorBudgetBurn
High requests error budget burn for job=kube-apiserver (current value: {{ $value }})

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-errorbudgetburn)

## ErrorBudgetBurn
High requests error budget burn for job=kube-apiserver (current value: {{ $value }})

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-errorbudgetburn)

## KubeAPILatencyHigh
The API server has an abnormal latency of {{ $value }} seconds for {{ $labels.verb }} {{ $labels.resource }}.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapilatencyhigh)

## KubeAPILatencyHigh
The API server has a 99th percentile latency of {{ $value }} seconds for {{ $labels.verb }} {{ $labels.resource }}.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapilatencyhigh)

## KubeAPIErrorsHigh
API server is returning errors for {{ $value | humanizePercentage }} of requests for {{ $labels.verb }} {{ $labels.resource }} {{ $labels.subresource }}.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapierrorshigh)

## KubeAPIErrorsHigh
API server is returning errors for {{ $value | humanizePercentage }} of requests for {{ $labels.verb }} {{ $labels.resource }} {{ $labels.subresource }}.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapierrorshigh)

## KubeClientCertificateExpiration
A client certificate used to authenticate to the apiserver is expiring in less than 7.0 days.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeclientcertificateexpiration)

## KubeClientCertificateExpiration
A client certificate used to authenticate to the apiserver is expiring in less than 24.0 hours.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeclientcertificateexpiration)

## AggregatedAPIErrors
An aggregated API {{ $labels.name }}/{{ $labels.namespace }} has reported errors. The number of errors have increased for it in the past five minutes. High values indicate that the availability of the service changes too often.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-aggregatedapierrors)

## AggregatedAPIDown
An aggregated API {{ $labels.name }}/{{ $labels.namespace }} is down. It has not been available at least for the past five minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-aggregatedapidown)

## KubeAPIDown
KubeAPI has disappeared from Prometheus target discovery.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeapidown)

## KubeNodeNotReady
{{ $labels.node }} has been unready for more than 15 minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubenodenotready)

## KubeNodeUnreachable
{{ $labels.node }} is unreachable and some workloads may be rescheduled.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubenodeunreachable)

## KubeletTooManyPods
Kubelet '{{ $labels.node }}' is running at {{ $value | humanizePercentage }} of its Pod capacity.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubelettoomanypods)

## KubeNodeReadinessFlapping
The readiness status of node {{ $labels.node }} has changed {{ $value }} times in the last 15 minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubenodereadinessflapping)

## KubeletPlegDurationHigh
The Kubelet Pod Lifecycle Event Generator has a 99th percentile duration of {{ $value }} seconds on node {{ $labels.node }}.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubeletplegdurationhigh)

## KubeletPodStartUpLatencyHigh
Kubelet Pod startup 99th percentile latency is {{ $value }} seconds on node {{ $labels.node }}.

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

## CoreDNSDown
CoreDNS has disappeared from Prometheus target discovery.

[Runbook](https://github.com/povilasv/coredns-mixin/tree/master/runbook.md#alert-name-corednsdown)

## CoreDNSLatencyHigh
CoreDNS has 99th percentile latency of {{ $value }} seconds for server {{ $labels.server }} zone {{ $labels.zone }} .

[Runbook](https://github.com/povilasv/coredns-mixin/tree/master/runbook.md#alert-name-corednslatencyhigh)

## CoreDNSErrorsHigh
CoreDNS is returning SERVFAIL for {{ $value | humanizePercentage }} of requests.

[Runbook](https://github.com/povilasv/coredns-mixin/tree/master/runbook.md#alert-name-corednserrorshigh)

## CoreDNSErrorsHigh
CoreDNS is returning SERVFAIL for {{ $value | humanizePercentage }} of requests.

[Runbook](https://github.com/povilasv/coredns-mixin/tree/master/runbook.md#alert-name-corednserrorshigh)

## CoreDNSForwardLatencyHigh
CoreDNS has 99th percentile latency of {{ $value }} seconds forwarding requests to {{ $labels.to }}.

[Runbook](https://github.com/povilasv/coredns-mixin/tree/master/runbook.md#alert-name-corednsforwardlatencyhigh)

## CoreDNSForwardErrorsHigh
CoreDNS is returning SERVFAIL for {{ $value | humanizePercentage }} of forward requests to {{ $labels.to }}.

[Runbook](https://github.com/povilasv/coredns-mixin/tree/master/runbook.md#alert-name-corednsforwarderrorshigh)

## CoreDNSForwardErrorsHigh
CoreDNS is returning SERVFAIL for {{ $value | humanizePercentage }} of forward requests to {{ $labels.to }}.

[Runbook](https://github.com/povilasv/coredns-mixin/tree/master/runbook.md#alert-name-corednsforwarderrorshigh)

