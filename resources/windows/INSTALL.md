# Installing the exporter
You can use the installer as a standalone application or install it in your system.

To install the Windows exporter download the `msi` binary file from the [release page](https://github.com/prometheus-community/windows_exporter/releases) of the Windows exporter repository.
Run the installer to install the exporter. This will configure the Windows Exporter as a Windows service and create an exception in the Windows firewall.

To execute it as a standalone application download the exe file from the [release page](https://github.com/prometheus-community/windows_exporter/releases) of the Windows exporter and execute it.

To disable the process collector to prevent high cardinality problems, you can install or execute the exporter with the following options.
```
# Installer:
msiexec /i windows_exporter.msi --collectors.enabled "cpu,cs,logical_disk,os,system,net"

# Stand alone:
.\windows_exporter.exe --collectors.enabled "cpu,cs,logical_disk,os,system,net"
```
