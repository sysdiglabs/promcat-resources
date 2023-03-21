# Alerts
## [Haproxy-Ingress] Uptime less than 1 hour
This alert detects when all of the instances of the ingress controller have an uptime of less than 1 hour.
## [Haproxy-Ingress] Frontend Down
This alert detects when a frontend has all of its instances down for more than 10 minutes.
## [Haproxy-Ingress] Backend Down
This alert detects when a backend has all of its instances down for more than 10 minutes.
## [Haproxy-Ingress] High Sessions Usage
This alert triggers when the backend sessions overpass the 85% of the sessions capacity for 10 minutes.
## [Haproxy-Ingress] High Error Rate
This alert triggers when there is an error rate over 15% for over 10 minutes in a proxy.
## [Haproxy-Ingress] High Request Denied Rate
These alerts detect when there is a denied rate of requests over 10% for over 10 minutes in a proxy.
## [Haproxy-Ingress] High Response Denied Rate
These alerts detect when there is a denied rate of responses over 10% for over 10 minutes in a proxy.
## [Haproxy-Ingress] High Response Rate
This alert triggers when a proxy has a mean response time higher than 250ms for over 10 minutes.