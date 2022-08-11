# Kafka
Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.

# Prometheus and exporters
Since Kafka isn't instrumentalized for Prometheus, exporters are needed. Here we're using the [jmx_exporter](https://github.com/prometheus/jmx_exporter) and the [kafka_exporter](https://github.com/danielqsj/kafka_exporter).

# Metrics

- kafka_brokers
- kafka_consumergroup_current_offset
- kafka_consumergroup_lag
- kafka_consumergroup_members
- kafka_controller_active_controller
- kafka_controller_offline_partitions
- kafka_log_size
- kafka_network_consumer_request_time_milliseconds
- kafka_network_fetch_follower_time_milliseconds
- kafka_network_producer_request_time_milliseconds
- kafka_server_bytes_in
- kafka_server_bytes_out
- kafka_server_consumer_client_byterate
- kafka_server_consumer_client_throttle_time
- kafka_server_consumer_user_byterate
- kafka_server_consumer_user_client_byterate
- kafka_server_consumer_user_client_throttle_time
- kafka_server_consumer_user_throttle_time
- kafka_server_messages_in
- kafka_server_partition_leader_count
- kafka_server_producer_client_byterate
- kafka_server_producer_client_throttle_time
- kafka_server_producer_user_byterate
- kafka_server_producer_user_client_byterate
- kafka_server_producer_user_client_throttle_time
- kafka_server_producer_user_throttle_time
- kafka_server_under_isr_partitions
- kafka_server_under_replicated_partitions
- kafka_server_zookeeper_auth_failures
- kafka_server_zookeeper_disconnections
- kafka_server_zookeeper_expired_sessions
- kafka_server_zookeeper_read_only_connections
- kafka_server_zookeeper_sasl_authentications
- kafka_server_zookeeper_sync_connections
- kafka_topic_partition_current_offset
- kafka_topic_partition_oldest_offset

# Attributions
Configuration files, dashboards and alerts are maintained by [Sysdig team](https://sysdig.com/).
