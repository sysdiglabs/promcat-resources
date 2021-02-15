# Redis
Redis is an open source in-memory database, cache and message broker.

Redis has an integrated statistics service that provide internal metrics.
To extract these metrics in Prometheus format, we will use he [Prometheus Redis Metrics Exporter](https://github.com/oliver006/redis_exporter).

The exporter is compatible with Redis from v2 to v6.

# Metrics
Redis generates different topics:
- Server: General information about the Redis server
- Clients: Client connections section
- Memory: Memory consumption related information
- Persistence: RDB and AOF related information
- Stats: General statistics
- Replication: Master/replica replication information
- CPU: CPU consumption statistics
- Commandstats: Redis command statistics
- Cluster: Redis Cluster section
- Keyspace: Database related statistics

# Number of time series generated
Redis generates around 100 metrics for each Redis instance.

For further information, consult [Redis documentation](https://redis.io/commands/info).

# Attributions
Configuration files, alerts and dashboards maintained by [Sysdig team](https://sysdig.com/).

Using [Prometheus Redis Metrics Exporter](https://github.com/oliver006/redis_exporter) with MIT License.