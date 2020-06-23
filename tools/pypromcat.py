import yaml
import json
from yaml.representer import SafeRepresenter
import re
import os.path

timeConversions = {"s": 0.0166666,
                    "m": 1,
                    "h": 60,
                    "d": 1440}

def getConfigurations(resource):
  return resource['configurations']

def filterConfigurationsPerKind(configurations,kind):
  filteredConfigurations = []
  for configuration in configurations:
    if configuration["kind"] == kind:
      filteredConfigurations.append(configuration)
  return filteredConfigurations

def loadYaml(input):
  return yaml.full_load(input)

def loadYamlFile(path):
  file = open(path)
  yamlFile = loadYaml(file)

  if 'descriptionFile' in yamlFile:
    fileToIncludePath = os.path.dirname(path) + "/" + yamlFile["descriptionFile"]
    with open(fileToIncludePath, 'r') as file:
      yamlFile["description"] =  file.read()

  if "configurations" in yamlFile:
    for configuration in yamlFile["configurations"]:
      if "file" in configuration:
        fileToIncludePath = os.path.dirname(path) + "/" + configuration["file"]
        with open(fileToIncludePath, 'r') as file:
          configuration["data"] =  file.read()

  return yamlFile

# Loads Yam File without inserting the include files inside configurations
def loadRawYamlFile(path):
  file = open(path)
  yamlFile = loadYaml(file)
  return yamlFile

def prometheusTime2Minutes(prometheusTime):
  prometheusNumber = int(prometheusTime[:-1])
  prometheusUnit = prometheusTime[-1]
  if prometheusUnit not in timeConversions:
    print("Unit conversion not supported: " + prometheusTime)
    exit(1)
  return round(prometheusNumber * timeConversions[prometheusUnit])

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
    sysdigAlert['alert']['reNotifyMinutes'] = prometheusTime2Minutes(promAlert['for'])
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

def removeTrailingSpaces(data):
  data = re.sub(' +\n','\n',data)
  data = re.sub(' +$','',data)
  return data

def removeTrailingSpacesFromAllElements(data):
  if type(data) == dict: 
    for element in data:  
      if type(data[element]) in [dict, list]:
        data[element] = removeTrailingSpacesFromAllElements(data[element])
      elif type(data[element]) == str: 
        data[element] = removeTrailingSpaces(data[element])
  if type(data) == list:
    for idx in range(len(data)):
      if type(data[idx]) in [dict, list]:
        data[idx] = removeTrailingSpacesFromAllElements(data[idx])
      elif type(data[idx]) == str: 
        data[idx] = removeTrailingSpaces(data[idx])
  return data

def dict2BeautyYaml(yaml2print):
  def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
      return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)
  yaml.add_representer(str, str_presenter)
  return(yaml.dump(removeTrailingSpacesFromAllElements(yaml2print), sort_keys=False))

def createArrayOfSysdigAlerts(alertsYaml):
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