# Alerts
## KubePodCrashLooping
Pod is restarting X times / 5 minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodcrashlooping)

## KubePodNotReady
Pod has been in a non-ready state for longer than 15 minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodnotready)

## KubeDeploymentGenerationMismatch
Deployment generation does not match, this indicates that the Deployment has failed but has not been rolled back.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedeploymentgenerationmismatch)

## KubeDeploymentReplicasMismatch
Deployment has not matched the expected number of replicas for longer than 15 minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedeploymentreplicasmismatch)

## KubeStatefulSetReplicasMismatch
StatefulSet has not matched the expected number of replicas for longer than 15 minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubestatefulsetreplicasmismatch)

## KubeStatefulSetGenerationMismatch
StatefulSet generation does not match, this indicates that the StatefulSet has failed but has not been rolled back.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubestatefulsetgenerationmismatch)

## KubeStatefulSetUpdateNotRolledOut
StatefulSet update has not been rolled out.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubestatefulsetupdatenotrolledout)

## KubeDaemonSetRolloutStuck
Only X of the desired Pods of DaemonSet are scheduled and ready.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedaemonsetrolloutstuck)

## KubeContainerWaiting
Container has been in waiting state for longer than 1 hour.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubecontainerwaiting)

## KubeDaemonSetNotScheduled
Pods of DaemonSet are not scheduled.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedaemonsetnotscheduled)

## KubeDaemonSetMisScheduled
Pods of DaemonSet are running where they are not supposed to run.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubedaemonsetmisscheduled)

## KubeJobCompletion
Job is taking more than one hour to complete.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubejobcompletion)

## KubeJobFailed
Job failed to complete.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubejobfailed)

## KubeCPUOvercommit
Cluster has overcommitted CPU resource requests for Pods and cannot tolerate node failure.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubecpuovercommit)

## KubeMemoryOvercommit
Cluster has overcommitted memory resource requests for Pods and cannot tolerate node failure.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubememoryovercommit)

## KubeCPUQuotaOvercommit
Cluster has overcommitted CPU resource requests for Namespaces.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubecpuquotaovercommit)

## KubeMemoryQuotaOvercommit
Cluster has overcommitted memory resource requests for Namespaces.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubememoryquotaovercommit)

## KubeQuotaFullyUsed
Namespace is using X% of its resource quota.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubequotafullyused)

## CPUThrottlingHigh
X% throttling of CPU in namespace for container in pod.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-cputhrottlinghigh)

## KubeNodeNotReady
Node has been unready for more than 15 minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubenodenotready)

## KubeNodeUnreachable
Node is unreachable and some workloads may be rescheduled.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubenodeunreachable)

## KubeletTooManyPods
Kubelet in Node is running at % of its Pod capacity.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubelettoomanypods)

## KubeNodeReadinessFlapping
The readiness status of node has changed X times in the last 15 minutes.

[Runbook](https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubenodereadinessflapping)

