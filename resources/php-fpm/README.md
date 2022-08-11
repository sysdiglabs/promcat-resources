# PHP-FPM
PHP-FPM (FastCGI Process Manager) is an alternative PHP FastCGI implementation with some additional features useful for sites of any size, especially busier sites.

# Prometheus and exporters
Since PHP-FPM isn't instrumentalized for Prometheus, an exporter is needed. Here we're using the [php-fpm_exporter](https://github.com/hipages/php-fpm_exporter)

# Metrics

- phpfpm_accepted_connections
- phpfpm_active_processes
- phpfpm_idle_processes
- phpfpm_listen_queue
- phpfpm_listen_queue_length
- phpfpm_max_active_processes
- phpfpm_max_children_reached
- phpfpm_max_listen_queue
- phpfpm_process_last_request_cpu
- phpfpm_process_last_request_memory
- phpfpm_process_request_duration
- phpfpm_process_requests
- phpfpm_process_state
- phpfpm_scrape_failures
- phpfpm_slow_requests
- phpfpm_start_since
- phpfpm_total_processes
- phpfpm_up

# Attributions
Configuration files, dashboards and alerts are maintained by [Sysdig team](https://sysdig.com/).
