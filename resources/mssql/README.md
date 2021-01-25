# Oracle Database
[Microsoft Server SQL](https://www.microsoft.com/en-us/sql-server/sql-server-2019) is a multi-model database management system. The [MsSQL Exporter](https://github.com/free/sql_exporter) is used to generate metrics. 

# Metrics
MsSQL exporter provide metrics on:
* Deadlocks
* Kill connection
* Memory used
* Cache hit raio
* Connections
* Disk Available
* Latency
* Transactions

# Number of time series generated
The number of metrics generated for database is ~80 * db.

# Attributions
Configuration files, dashboards and alerts maintained by [Sysdig team](https://sysdig.com/).

Using the [SQL Exporter](https://github.com/free/sql_exporter). 