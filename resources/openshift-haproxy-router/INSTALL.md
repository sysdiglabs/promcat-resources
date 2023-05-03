# Prerequisites

### Openshift 3.11

Once the Sysdig agent is deployed, check if it is running on all nodes (compute, master, and infra):

```
oc get nodes
oc get pods -n sysdig-agent -o wide
```

Apply this patch in case the Agent is not running on infra/master.

```
oc patch namespace sysdig-agent --patch-file='sysdig-agent-namespace-patch.yaml'
```

sysdig-agent-namespace-patch.yaml file
```yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    openshift.io/node-selector: ""
```

OpenShift integrates security by default. Therefore, if you want Sysdig agent to scrape HAProxy router metrics, provide it with the necessary permissions. To do so:

```
oc apply -f router-clusterrolebinding-sysdig-agent-oc3.yaml
```

router-clusterrolebinding-sysdig-agent-oc3.yaml file
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: haproxy-route-monitoring
rules:
- apiGroups:
  - route.openshift.io
  resources:
  - routers/metrics
  verbs:
  - get
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  labels:
    app: sysdig-agent
  name: sysdig-router-monitoring
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: haproxy-route-monitoring
subjects:
- kind: ServiceAccount
  name: sysdig-agent
  namespace: sysdig-agent   # Remember to change to the namespace where you have the Sysdig agents deployed
```

### Openshift 4.X

OpenShift integrates security by default. Therefore, if you want Sysdig agent to scrape HAProxy router metrics, provide it with the necessary permissions. To do so:

```
oc apply -f router-clusterrolebinding-sysdig-agent-oc4.yaml
```

router-clusterrolebinding-sysdig-agent-oc4.yaml file
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: router-monitoring-sysdig-agent
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: router-monitoring
subjects:
- kind: ServiceAccount
  name: sysdig-agent
  namespace: sysdig-agent   # Remember to change to the namespace where you have the Sysdig agents deployed
```

# Installation

The application is ready to be scraped