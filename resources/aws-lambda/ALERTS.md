# Alerts
## HighFunctionErrorRate
A Lambda function can end with an error.
This alert triggers when the percentage of executions of a function excess a threshold for a certain period of time.

The recommended value for this alert is 15% of the functions ended with error for 10 minutes.

## ThrottlingFunction
Lambda has a limited number of concurrent executions per function.
When you reach this limit, the function cannot be executed. The metric 'throttled' gives information of the executions that were not executed because they reached the concurrency limit.
Constant throttling can indicate that a function is called more times that its reserved concurrency.

The recommended value for this alert is to alert when throttling for more than 10 minutes.

## DestinationDeliveryFailures
Detected destination delivery failures in a function.

## DeadLetterErrors
Detected dead-letter queue errors in a function.

## HighIteratorAge
Detected high iterator age in a function.
