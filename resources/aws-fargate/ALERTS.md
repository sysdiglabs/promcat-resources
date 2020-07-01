# Alerts
## HighCpuUtilizationRate
In the definition of the Fargate tasks you can reserve the CPU units that it will be able to use. If the task demands more CPU that reserved the it can affect the performance of the services running in it.

This alert triggers when a threshold for CPU utilization is passed for a certain period of time.

The recommended value for this alert is 75% of the reserved CPU for the task for 10 minutes.

## HighMemoryUtilizationRate
In the definition of the Fargate tasks you can reserve the memory that it will be able to use. If the task demands more memory that reserved the it can affect the performance of the services running in it.

This alert triggers when a threshold for memory utilization is passed for a certain period of time.

The recommended value for this alert is 75% of the reserved memory for the task for 10 minutes.

## RecurringPendingTasks
When a task is launched in Fargate it stays in 'pending' state until it pass to 'running' state. If a task cannot be launched properly, it will stay in 'pending' state.

Errors in the definition of the task or in the code can cause some tasks to stay in 'pending' state indefinitely.

This alert triggers when there are pending tasks in the cluster for more than 10 minutes.
