#!/bin/bash
kubectl apply -f 'https://raw.githubusercontent.com/sysdiglabs/promcat-resources/master/resources/rancher/include/service.yaml'
kubectl apply -f 'https://raw.githubusercontent.com/sysdiglabs/promcat-resources/master/resources/rancher/include/service-monitor.yaml'