#!/bin/bash
kubectl version --client
kubectl -n promhub get po
kubectl -n promhub delete jobs.batch dbimport
kubectl -n promhub get po
kubectl apply -f deployment/master/dbimport-job.yaml
kubectl -n promhub get po