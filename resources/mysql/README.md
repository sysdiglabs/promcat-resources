# MySQL
[MySQL](https://dev.mysql.com) is an open-source relational database management system (RDBMS). Also, is the base of other databases like [MariaDB](https://mariadb.org/), and [AWS-Aurora](https://aws.amazon.com/rds/aurora/).

This integration uses the the [MySQL exporter](https://github.com/prometheus/mysqld_exporter) and supports the following versions:
- MySQL: >= 5.6
- MariaDB: >= 10.2

It also support both on-prem databases and cloud managed services like AWS-RDS.


# Number of time series generated
The exporter generates ~800 time series per instance.

For further information, see [the documentations of the exporter and its different collectors](https://github.com/prometheus/mysqld_exporter).

# Attributions
The configuration files and dashboards are maintained by [Sysdig team](https://sysdig.com/) under GPL3 license.

Grafana dashboards are based on [Mysql exporter mixins](https://github.com/prometheus/mysqld_exporter) with Apache License 2.0.

Alerts are based on [Awesome Prometheus Alerts](https://github.com/samber/awesome-prometheus-alerts) under CC BY 4.0 License.

Using the [MySQL exporter](https://github.com/prometheus/mysqld_exporter) with Apache License 2.0.
