# PostgreSQL
[PostgreSQL](https://www.postgresql.org/) (or just _Postgres_) is a powerful, open source object-relational database system with over 30 years
of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

To extract metrics, we will use the [Postgres Exporter](https://github.com/wrouesnel/postgres_exporter).

# Metrics
The metrics available are the ones related to the modules:
* Settings
* Locks
* Activity
* Archiver
* Background writer
* Database statistics
* Replication
* User table statistics and I/O stats

# Number of time series generated
* Each instance generate ~250 metrics
* Each database generates ~25 + (30 * number of tables)

# Attributions
Configuration files, dashboards and alerts maintained by [Sysdig team](https://sysdig.com/).

Exporter, script for no-admin user creation and user queries: [Postgres Exporter](https://github.com/wrouesnel/postgres_exporter) with Apache v2 license. 
