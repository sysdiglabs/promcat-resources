import yaml
import json
from yaml.representer import SafeRepresenter

def getConfigurations(resource):
  return resource['configurations']

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
  if "for" in promAlert:
    sysdigAlert['alert']['reNotifyMinutes'] = promAlert['for']
  else:
    sysdigAlert['alert']['reNotifyMinutes'] = 0
  sysdigAlert['alert']['severity'] = 4
  sysdigAlert['alert']['severityLabel'] = "LOW"
  sysdigAlert['alert']['severityLevel'] = None
  sysdigAlert['alert']['timespan'] = 600000000
  sysdigAlert['alert']['type'] = "PROMETHEUS"
  return sysdigAlert

def dict2BeautyString(jsonToPrint):
  return json.dumps(jsonToPrint,indent=2)

def dict2BeautyYaml(yaml2print):
  def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
      return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)
  yaml.add_representer(str, str_presenter)
  return(yaml.dump(yaml2print))

def createArrayOfSysdigAlerts(file):
  alertsYaml = loadYamlFile(file)
  configurationsAlerts = getConfigurations(alertsYaml)
  sysdigAlerts = []
  for configurationAlert in configurationsAlerts:
      if configurationAlert['kind'] == "Prometheus":
        prometheusAlerts = loadYaml(configurationAlert['data'])
        for prometheusAlert in prometheusAlerts:
          sysdigAlert = prometheusAlert2SysdigAlert(prometheusAlert)
          sysdigAlerts.append(sysdigAlert)
  return sysdigAlerts

def sysdigAlerts2PromcatConfigurations(sysdigAlerts):
  promcatAlerts = []
  for sysdigAlert in sysdigAlerts:
    promcatAlert = {}
    promcatAlert["kind"] = "Sysdig"
    promcatAlert["data"] = dict2BeautyString(sysdigAlert)
    promcatAlerts.append(promcatAlert)
  return(promcatAlerts)