import pytest
import yaml
import os

apps_names = []

descriptions = []
descriptions_names = []
dashboards = []
dashboards_names = []
exporterConfigs = []
exporterConfigs_names = []
alerts = []
alerts_name = []
recordingRules = []
recordingRules_names = []

all_resources = [descriptions, dashboards, exporterConfigs, alerts, recordingRules]

def loadYaml(input):
  return yaml.full_load(input)
  
@pytest.fixture(scope="session", autouse=True)
def loadResources():
  for root, dirs, files in os.walk('apps'):
     for file in files:
       if file.endswith(".yaml"):
          with open(os.path.join(root, file), "r") as appFile:
            appYaml = loadYaml(appFile)
            apps_names.append(appYaml["name"])
  for root, dirs, files in os.walk('resources'):
    for file in files:
       if file.endswith(".yaml"):
          with open(os.path.join(root, file), "r") as resourceFile:
            resourceYaml = loadYaml(resourceFile)
            if (resourceYaml["kind"] == "Description"):
              descriptions.append(resourceYaml)
            elif (resourceYaml["kind"] == "Dashboards"): 
              dashboards.append(resourceYaml)
            elif (resourceYaml["kind"] == "ExporterConfig"): 
              exporterConfigs.append(resourceYaml)
            elif (resourceYaml["kind"] == "Alerts"): 
              alerts.append(resourceYaml)
            elif (resourceYaml["kind"] == "RecordingRules"): 
              recordingRules.append(resourceYaml)
            else: 
              raise ValueError("File: " + file + " kind: " + resourceYaml["kind"] + " not supported.")

def checkDuplicated(res,names):
  assert (res['app'] != "") and (type(res['app']) == str) and (not res['app']  in names)
  names.append(res['app'])

def testDuplicatedDescriptions(): 
  for res in descriptions:
    checkDuplicated(res,descriptions_names)

def testDuplicatedDashboards(): 
  for res in dashboards:
    checkDuplicated(res,dashboards_names)

def testDuplicatedExporterConfigs(): 
  for res in exporterConfigs:
    checkDuplicated(res,exporterConfigs_names)

def testDuplicatedAlerts(): 
  for res in alerts:
    checkDuplicated(res,alerts_name)

def testDuplicatedRecordingRules(): 
  for res in recordingRules:
    checkDuplicated(res,recordingRules_names)

def testVersion():
  for kind in all_resources:
    for res in kind:
      assert (res['app'] != "") and (res['kind'] != "") and (type(res['apiVersion']) == str) \
        and (res['apiVersion'] == "v1")

def testExistsApp():
  for kind in all_resources:
    for res in kind:
      assert (res['app'] != "") and (res['kind'] != "") and (type(res['app']) == str) \
        and (res['app'] in apps_names)

def testAppVersion():
  for kind in all_resources:
    for res in kind:
      assert (res['app'] != "") and (res['kind'] != "") and (type(res['appVersion']) == list) \
        and (len(res['appVersion']) > 0)
      
def testMaintainers():
  for kind in all_resources:
    for res in kind:
      assert (res['app'] != "") and (res['kind'] != "") and (type(res['maintainers']) == list) \
        and (len(res['maintainers']) > 0)
      for maintainer in res['maintainers']:
        assert (res['app'] != "") and (res['kind'] != "") and \
           (maintainer != None) and (type(maintainer['name']) == str) and (maintainer['name'] != "")

        assert (res['app'] != "") and (res['kind'] != "") and \
           (maintainer != None) and (type(maintainer['link']) == str) and (maintainer['link'] != "")
