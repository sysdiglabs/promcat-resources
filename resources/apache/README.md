# Apache
The [Apache HTTP Server Project](https://httpd.apache.org/) aims to develop and maintain an open-source HTTP server for modern operating systems including UNIX and Windows.

Versions supported: 2.4

# Type
This integration uses a sidecar exporter that is available in UBI or scratch base image.
The integration is using the following exporters:
- apache-exporter: https://quay.io/repository/sysdig/apache-exporter
- grok-exporter: https://quay.io/repository/sysdig/grok-exporter


# Attributions
The configuration files and dashboards maintained by [Sysdig team](https://sysdig.com/).
# License
- apache-exporter with Apache license.
- grok-exporter with GPL license.