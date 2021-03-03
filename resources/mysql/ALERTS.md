# Alerts
## MysqlDown
MySQL down (instance {{ $labels.instance }})

## MysqlRestarted
MySQL restarted (instance {{ $labels.instance }})

## MysqlTooManyConnections(>80%)
MySQL too many connections (> 80%) (instance {{ $labels.instance }})

## MysqlHighThreadsRunning
MySQL high threads running (instance {{ $labels.instance }})

## MysqlHighOpenFiles
MySQL high number of open files (instance {{ $labels.instance }})

## MysqlSlowQueries
MySQL slow queries (instance {{ $labels.instance }})

## MysqlInnodbLogWaits
MySQL InnoDB log waits (instance {{ $labels.instance }})

## MysqlSlaveIoThreadNotRunning
MySQL Slave IO thread not running (instance {{ $labels.instance }})

## MysqlSlaveSqlThreadNotRunning
MySQL Slave SQL thread not running (instance {{ $labels.instance }})

## MysqlSlaveReplicationLag
MySQL Slave replication lag (instance {{ $labels.instance }})

