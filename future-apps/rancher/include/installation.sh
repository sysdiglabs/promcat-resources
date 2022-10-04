#!/bin/bash
kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"volumes":[{"hostPath":{"path":"/etc/kubernetes/pki/etcd-manager-main","type":"DirectoryOrCreate"},"name":"etcd-certificates"}]}}}}'
kubectl -n sysdig-agent patch ds sysdig-agent -p '{"spec":{"template":{"spec":{"containers":[{"name":"sysdig-agent","volumeMounts": [{"mountPath": "/etc/kubernetes/pki/etcd-manager","name": "etcd-certificates"}]}]}}}}'
kubectl apply -f 'https://raw.githubusercontent.com/sysdiglabs/promcat-resources/master/resources/rancher/include/service.yaml'
kubectl apply -f 'https://raw.githubusercontent.com/sysdiglabs/promcat-resources/master/resources/rancher/include/service-monitor.yaml'
kubectl apply -f 'https://raw.githubusercontent.com/sysdiglabs/promcat-resources/master/resources/rancher/include/rules.yaml'