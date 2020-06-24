import pypromcat
import argparse
import os

parser = argparse.ArgumentParser(description='Generate from an alerts.yaml with Prometheus alerts a new one with sysdig alerts and description.')
parser.add_argument('-f',
                    '--file',
                    required=True,
                    dest='file',
                    help='Original file with Prometheus alerts')
parser.add_argument('-o',
                    '--output',
                    required=False,
                    dest='outputFile',
                    help='File to write the output')

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

sysdigAlertsArray = pypromcat.sysdigAlerts2PromcatConfigurations(pypromcat.createArrayOfSysdigAlerts(yamlFile))
for sysdigAlert in sysdigAlertsArray:
  newConfigurations.append(sysdigAlert)
  
yamlFile["descriptionFile"] = 'ALERTS.md'
yamlFile["configurations"] = newConfigurations

newDescription = ""
newDescription += "# Alerts\n"

for prometheusAlertElement in prometheusAlerts:
  prometheusAlertsYaml = pypromcat.loadYaml(prometheusAlertElement["data"])
  for alert in prometheusAlertsYaml:
    newDescription = newDescription + "## " + alert["alert"] + "\n"
    if "annotations" in alert:
      if "summary" in alert["annotations"]:
        newDescription = newDescription + alert["annotations"]["summary"] + "\n\n"
      if "message" in alert["annotations"]:
        newDescription = newDescription + alert["annotations"]["message"] + "\n\n"
      if "runbook_url" in alert["annotations"]:
        newDescription = newDescription \
                         + "[Runbook](" \
                         + alert["annotations"]["runbook_url"] \
                        + ")\n\n"

f = open(filesDirectory + "/ALERTS.md", "w")
f.write(newDescription)
f.close()


outputformatted = pypromcat.dict2BeautyYaml(yamlFile)
if args.outputFile is None:
    print(outputformatted)
else:
    f = open(args.outputFile, "w")
    f.write(outputformatted)
    f.close()