#!/bin/bash
kubectl version --client
kubectl -n staging get po
kubectl apply -f deployment/dbimport-job.yaml