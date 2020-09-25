# Alerts
## HighNumberOfMessagesInQueue
High number of messages for a long time in queue.

## HighLatencyInQueue
High latency in queue. This alert uses the approximate age of the oldest message in the queue. 

## RecurringEmptyReceives
Recurring empty receives in queue.

## MessageReceivedInDeadLetterQueue
Message received in dead-letter queue. This alert uses the prefix `dead-letter-` in the name of the SQS queue to filter the dead-letter queues.  

