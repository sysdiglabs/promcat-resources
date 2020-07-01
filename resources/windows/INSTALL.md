# Installing the exporter
You can use the installer as a stand alone application or installing it in your system.

To install the Windows exporter download the msi binary file from the [release page](https://github.com/prometheus-community/windows_exporter/releases) of the Windows exporter repository.
Execute the installer to install the exporter. This will setup the Windows Exporter as a Windows service, as well as create an exception in the Windows Firewall.

To execute it as a standalone application download the exe file from the [release page](https://github.com/prometheus-community/windows_exporter/releases) of the Windows exporter and execute it.

To disable the process collector to prevent high cardinality problems, you can install or execute the exporter with the following options.
```
# Installer:
msiexec /i windows_exporter.msi --collectors.enabled "cpu,cs,logical_disk,os,system,net"

# Stand alone:
.\windows_exporter.exe --collectors.enabled "cpu,cs,logical_disk,os,system,net"
```
# Configuring Sysdig Agent
To make the Sysdig agent to scrape a remote endpoint from just one of the agents, you have to annotate the node that will host the scraping agent:
```
kubectl annotate nodes NODEID sysdig.com/scraper=true
```

Following is the configuration of the Sysdig agent. Be sure to change this line with the IP and PORT of your windows instance:
> url: "http://IP:PORT/metrics"

To apply, save the file as dragent.yaml and apply executing:
```
kubectl apply -f dragent.yaml
```
