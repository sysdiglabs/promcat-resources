# Windows exporter
The [Windows exporter](https://github.com/prometheus-community/windows_exporter) (former WMI exporter) offers metrics for instances running Windows operative systems.

It has a series of different collectors that offer different metrics of the system.
It can be used as a stand alone application or a Windows service and exposes the metrics in the port 9182 by default.

# Metrics
The Windows exporter provides metrics on the following collectors:
* CPU: Metrics about CPU usage
* CS: Hardware of the computer system
* Logical Disk: Metrics about logical disks
* Memory: Metrics about system memory usage
* Net: Metrics about network interfaces
* OS: Metrics about the operating system
* System: Metrics about the system

For further information, consult the [documentation of the Windows exporter](https://github.com/prometheus-community/windows_exporter/blob/master/docs/README.md).

# Attributions
Configuration files, dashboards and alerts maintained by [Sysdig team](https://sysdig.com/).

Using [Windows Exporter](https://github.com/prometheus-community/windows_exporter) with MIT license.
