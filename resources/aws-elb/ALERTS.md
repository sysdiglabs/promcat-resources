# Alerts
## High4XXErrorsFromLoadBalancer and High5XXErrorsFromLoadBalancer
A request to a load balancer can end in an error triggered directly by the load balancer with codes stating by either by 4 or 5.
For a list of possible error codes and their causes you can read the [load balancers error codes documentation](https://docs.aws.amazon.com/elasticloadbalancing/atest/application/load-balancer-troubleshooting.html).

This alert triggers when the percentage of requests with each error code excess a threshold for a certain period of time.
The recommended value for this alert is 15% of the requests ended with error for 10 minutes.

## High4XXErrorsFromBackend and High5XXErrorsFromBackend
A request to a load balancer can end in an error triggered by the backend with codes stating by either by 4 or 5.
For a list of possible error codes and their causes you can read the [load balancers error codes documentation](https://docs.aws.amazon.com/elasticloadbalancing/atest/application/load-balancer-troubleshooting.html).

This alert triggers when the percentage of requests with each error code excess a threshold for a certain period of time.
The recommended value for this alert is 15% of the requests ended with error for 10 minutes.

## UnhealthyHostInLoadBalancer
This alerts triggers when there is one or more unhealthy hosts in a load balancer.

## QueueSpilloverRejections
This alert triggers when there are continuos rejected connections due to saturation in teh queue in a load balancer for more than 10 minutes.

## RejectedConnectionsInLoadBalancer
This alert triggers when there are continuos rejected connections in a load balancer for more than 10 minutes.

## HighLatencyInLoadBalancer
The latency time is the time elapsed, in seconds, after the request leaves the load balancer until a response from the backend is received.

This alerts triggers when the percentile 95 of a load balancer is over 250ms for 10 minutes.
