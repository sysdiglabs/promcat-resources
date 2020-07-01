# Alerts
## HighFunctionErrorRate
A Lambda function can end with an error.
This alert triggers when the percentage of executions of a function excess a threshold for a certain period of time.

The recommended value for this alert is 15% of the functions ended with error for 10 minutes.

# HighCPUUsage
This alert triggers when the CPU usage of an instance excess a threshold value.
The recommended value for this alert is 95% over 15 minutes.

# HighPhysicalMemoryUsage
This alert triggers when the physical memory usage of an instance excess a threshold value.
The recommended value for this alert is 95% over 15 minutes.

# LogicalDiskFull
This alert triggers when the disk available in a volume of an instance is under a threshold value.
The recommended value for this alert is 95% of the volume full for more than 15 minutes.

# UpTimeLessThanOneHour
This alert triggers when the uptime of an instance is less than a certain value, meaning that the instance wa restarted.
The recommended value for this alert is one hour.

# HighInboundErrorRate and HighOutboundErrorRate
These alerts trigger when the inbound and outbound network rate error of an instance excess a threshold value.
The recommended value for this alert is 75% over 10 minutes.
