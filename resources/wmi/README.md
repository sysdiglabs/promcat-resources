# Obsolescence of the WMI
In June 2020 the WMI exporter was migrated to Windows exporter. This impact:
* The main repository, that is available [here](https://github.com/prometheus-community/windows_exporter)
* The prefix of the metrics changes from _wmi_ to _windows_

Here you can find resources for the legacy version of the exporter. 
For the new version check the [Windows exporter resources](https://promcat.io/apps/windows).

# Windows Management Instrumentation (WMI)
The [WMI exporter](https://github.com/martinlindhe/wmi_exporter) offers metrics for instances running Windows operative systems.

It has a series of different collectors that offer different metrics of the system.
It can be used as a stand alone application or a Windows service and exposes the metrics in the port 9182 by default.

# Metrics
The WMI exporter provides metrics on the following collectors:
* CPU: Metrics about CPU usage
* CS: Hardware of the computer system
* Logical Disk: Metrics about logical disks
* Memory: Metrics about system memory usage
* Net: Metrics about network interfaces
* OS: Metrics about the operating system
* System: Metrics about the system

For further information, consult the [documentation of the WMI exporter](https://github.com/martinlindhe/wmi_exporter/blob/master/docs/README.md).

# Attributions
Configuration files, dashboards and alerts maintained by [Sysdig team](https://sysdig.com/).

Using [Windows Exporter](https://github.com/prometheus-community/windows_exporter) with MIT license.
