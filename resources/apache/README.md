# Apache
The [Apache HTTP Server Project](https://httpd.apache.org/) aims to develop and maintain an open-source HTTP server for modern operating systems including UNIX and Windows.

# Metrics
The Apache metrics are extracted in two different ways:
* From the [apache exporter](https://github.com/Lusitaniae/apache_exporter)
* Parsing the logs via [Grok exporter](https://hub.docker.com/r/palobo/grok_exporter).

## Metrics gathered with Apache exporter
- apache_accesses_total: The latest value of the total number of apache accesses
- apache_connections: The Apache connection statuses
- apache_cpuload: The current percentage of CPU used by each worker and in total by all workers combined
- apache_duration_total: The total duration of all registered requests
- apache_exporter_build_info: A metric with a constant '1' value labeled by version, revision, branch, and goversion from which apache_exporter was built.
- apache_scoreboard: The Apache scoreboard statuses
- apache_sent_kilobytes_total: The latest value of total kbytes sent
- apache_up: Indicates whether the Apache server can be reached or not
- apache_uptime_seconds_total: The current uptime in seconds
- apache_version: The Apache server version
- apache_workers: The Apache worker statuses

## Metrics gathered with Apache exporter
- apache_http_response_codes_total
- apache_http_response_bytes_total
- apache_http_last_request_seconds

> More metrics can be customized through the Grok exporter.
The metrics configured here are based on the [blog post of Robust Percepction](https://www.robustperception.io/getting-metrics-from-apache-logs-using-the-grok-exporter).

# Number of time series generated
Each Apache instance generates approximately 25 time series.

For further information, see [Apache documentation](https://httpd.apache.org/).

# Attributions
The configuration files and dashboards maintained by [Sysdig team](https://sysdig.com/).

Exporter [Apache_exporter](https://github.com/Lusitaniae/apache_exporter) MIT License.
