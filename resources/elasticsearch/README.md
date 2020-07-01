# ElasticSearch
Elasticsearch is a distributed, open source search and analytics engine for all types of data, including textual, numerical, geospatial, structured,
and unstructured.

To get the metrics from elasticsearch and alert with prometheus server, you can use the [justwatchcom exporter](https://github.com/justwatchcom/elasticsearch_exporter),
with exporter we can gather the metrics from the elasticsearch api.

# Metrics
## Metrics of cluster
* ElasticSearch cluster
* Cluster health
* CPU usage Avg
* JVM memory used Avg
* Nodes
* Data Nodes
* Active shards
* Pending tasks
* Percentage disk used
* Active primary shards
* Query time
* Ingest rate
* JVM memory usage
* Ingest rate by node
* CPU usage
* Initializing shards
* Relocating shards
* Delayed shards
* Unassigned shards

## Metrics of infra
* ElasticSearch Infra
* Load average
* Cpu usage
* JVM memory usage
* JVM memory committed
* GC count
* GC time
* Disk used
* Network usage
* Query time
* Indexing time
* Merging time
* Throttle time for index store

# Attributions
Configuration files and dashboards maintained by [Sysdig team](https://sysdig.com/).

The dashboars provided are created by Sysdig team with [this](https://grafana.com/grafana/dashboards/6483) as reference

The alerts are from [Awesome Prometheus alerts] (https://github.com/samber/awesome-prometheus-alerts)