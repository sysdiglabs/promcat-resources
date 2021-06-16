#!/bin/sh

FILES=$(pwd)/resources/*/include/alerts*.yaml
for f in $FILES
do
    echo "Processing $f file..."
    # take action on each file. $f store current file name
    docker run \
        -v $f:/tmp/alerts.yaml \
        artifactory.internal.sysdig.com/promtool:latest \
        check rules /tmp/alerts.yaml
done
