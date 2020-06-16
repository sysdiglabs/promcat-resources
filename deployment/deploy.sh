#!/bin/bash
kubectl version --client
kubectl -n staging get po
kubectl -n staging delete jobs.batch dbimport
kubectl -n staging get po
kubectl apply -f deployment/dbimport-job.yaml
kubectl -n staging get po