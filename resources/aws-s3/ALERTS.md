# Alerts
## High4XXErrorRate and High5XXErrorRate
A request to a resource in a S3 bucket can end in an error with a code with 3 digits starting either by 4 or 5.
For a list of possible error codes and their causes you can read the [S3 error codes documentation](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html).
This alert triggers when the percentage of requests with each error code excess a threshold for a certain period of time.
The recommended value for this alert is 15% of the requests ended with error for 10 minutes.

## HighFirstByteLatency
The first byte latency is the time that pass since S3 receives a request of a resource and serves the first byte.
A high latency in the first byte can be caused a high number of petitions in a single bucket, making it slowing down the petitions.
This alert triggers when the P95 of the latency of the first byte excess a threshold for a certain period of time.
The recommended value for this alert is a latency over 250ms for 10 minutes.
