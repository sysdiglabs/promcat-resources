# Installing the exporter
In order to expose metrics from Docker engine, configure the Docker daemon as a Prometheus target.

To do so, you need to specify the `metrics-address`. The best way to do this is via the `daemon.json`, which is located at one of the following locations by default. If the file does not exist, create it.

- **Linux**: `/etc/docker/daemon.json`
- **Windows Server**: `C:\ProgramData\docker\config\daemon.json`
- **Docker Desktop for Mac / Docker Desktop for Windows**: Click the Docker icon in the toolbar, select **Preferences**, then select **Daemon**. Click **Advanced**.

```json
{
  "metrics-addr" : "127.0.0.1:9323",
  "experimental" : true
}
```
For more information, see [documentation](https://docs.docker.com/config/daemon/prometheus/).