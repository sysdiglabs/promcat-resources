# Alerts
## HighResourceUtilization
High resource utilization of resource. It triggers only if the limit is set and higher than zero. 

## UsersTablespaceFull
Tablespace USERS almost full.

## SlowQueriesP99
Percentile 99 of time elapsed in queries higher than 10 seconds. You can edit this alert to use the `oracledb_slow_queries_p95_time_usecs` metric or change the threshold value. 

## BigQueriesP99
Percentile 99 of returned rows in queries higher than 1M.  You can edit this alert to use the `oracledb_big_queries_p95_rows` metric or change the threshold value.

