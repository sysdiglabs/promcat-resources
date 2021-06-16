# MongoDB
[MongoDB](https://www.mongodb.com/) is a general purpose, document-based, distributed database built for modern application developers and for the cloud era.

To extract metrics you can use the [Mongo Exporter](https://github.com/percona/mongodb_exporter).

# Metrics
The metrics available are the ones related to the modules:
* Asserts, errors and locks
* Database. documents and collections
* Network, connections and latency
* Replication
* Wiredtiger

# Number of time series generated
* Each instance generates ~100 metrics
* Each database generates ~15 metrics

# Attributions
The configuration files, dashboards, and alerts maintained by [Sysdig team](https://sysdig.com/).

Using [Mongo Exporter](https://github.com/percona/mongodb_exporter) with Apache 2.0 license.
