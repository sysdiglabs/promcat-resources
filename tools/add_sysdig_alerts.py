import yaml
import json
import argparse

def getConfigurationsAlerts(alerts):
  return alerts['configurations']

def loadYaml(input):
  return yaml.full_load(input)

def loadYamlFile(path):
  file = open(path)
  return loadYaml(file)

def prometheusAlert2SysdigAlert(promAlert):
  sysdigAlert = {}
  sysdigAlert['alert'] = {}
  sysdigAlert['alert']['condition'] = promAlert['expr']
  sysdigAlert['alert']['customNotification'] = {}
  sysdigAlert['alert']['customNotification']['titleTemplate'] = "{{__alert_name__}} is {{__alert_status__}}"
  sysdigAlert['alert']['customNotification']['useNewTemplate'] = False
  sysdigAlert['alert']['enabled'] = True
  sysdigAlert['alert']['name'] = promAlert['alert']
  sysdigAlert['alert']['rateOfChange'] = False
  sysdigAlert['alert']['reNotify'] = False
  sysdigAlert['alert']['reNotifyMinutes'] = promAlert['for']
  sysdigAlert['alert']['severity'] = 4
  sysdigAlert['alert']['severityLabel'] = "LOW"
  sysdigAlert['alert']['severityLevel'] = None
  sysdigAlert['alert']['timespan'] = 600000000
  sysdigAlert['alert']['type'] = "PROMETHEUS"
  return sysdigAlert

def dict2BeautyString(jsonToPrint):
  return json.dumps(jsonToPrint,indent=2)

def createArrayOfSysdigAlerts(file):
  alertsYaml = loadYamlFile(file)
  configurationsAlerts = getConfigurationsAlerts(alertsYaml)
  sysdigAlerts = []
  for configurationAlert in configurationsAlerts:
      if configurationAlert['kind'] == "Prometheus":
        prometheusAlerts = loadYaml(configurationAlert['data'])
        for prometheusAlert in prometheusAlerts:
          sysdigAlert = prometheusAlert2SysdigAlert(prometheusAlert)
          sysdigAlerts.append(sysdigAlert)
  return sysdigAlerts


parser = argparse.ArgumentParser(description='Parser to extract Sysdig alerts from Prometheus alerts in PromCat resources.')
parser.add_argument('-f',
                    '--file',
                    required=True,
                    dest='file',
                    help='File to extract the alerts from')

try:
    args = parser.parse_args()
except BaseException as exception:
    # parser will print either help or syntax error details
    exit(1)

sysdigAlertsArray = createArrayOfSysdigAlerts(args.file)
print(dict2BeautyString(sysdigAlertsArray))