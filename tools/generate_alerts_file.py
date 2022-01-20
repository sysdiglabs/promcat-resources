import pypromcat
import argparse
import os

parser = argparse.ArgumentParser(description='Generate from an alerts.yaml with Prometheus alerts a new ALERTS.md with description.')
parser.add_argument('-f',
                    '--file',
                    required=True,
                    dest='file',
                    help='Original file with Prometheus alerts')

try:
    args = parser.parse_args()
except BaseException as exception:
    # parser will print either help or syntax error details
    exit(1)


yamlFile = pypromcat.loadYamlFile(args.file)
filesDirectory = os.path.dirname(args.file)
newConfigurations = []

prometheusAlerts = pypromcat.filterConfigurationsPerKind(yamlFile["configurations"],"Prometheus")
for prometheusAlert in prometheusAlerts:
  configToAppend = prometheusAlert.copy()
  if 'file' in prometheusAlert:
    del configToAppend['data']
  newConfigurations.append(configToAppend)


yamlFile["descriptionFile"] = 'ALERTS.md'
yamlFile["configurations"] = newConfigurations

newDescription = ""
newDescription += "# Alerts\n"

for prometheusAlertElement in prometheusAlerts:
  prometheusAlertsYaml = pypromcat.loadYaml(prometheusAlertElement["data"])
  for group in prometheusAlertsYaml["groups"]:
    for alert in group["rules"]:
      newDescription = newDescription + "## " + alert["alert"] + "\n"
      if "annotations" in alert:
        if "summary" in alert["annotations"]:
          newDescription = newDescription + alert["annotations"]["summary"] + "\n\n"
        if "description" in alert["annotations"]:
          newDescription = newDescription + alert["annotations"]["description"] + "\n\n"
        if "runbook_url" in alert["annotations"]:
          newDescription = newDescription \
                          + "[Runbook](" \
                          + alert["annotations"]["runbook_url"] \
                          + ")\n\n"

with open(filesDirectory + "/ALERTS.md", "w") as f:
    f.write(newDescription)
    