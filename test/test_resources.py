import pytest
import yaml
import os
import json

apps_names = []
apps_versions = {}

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
resources_with_description = [exporterConfigs, alerts, recordingRules]
resources_with_data = [descriptions, exporterConfigs, recordingRules]
resources_with_configurations = [dashboards, alerts]

compulsory_fields_all = ["apiVersion", "kind", "app", "version", "appVersion", 
                      "maintainers" ]

def loadYaml(input):
  return yaml.full_load(input)
  
@pytest.fixture(scope="session", autouse=True)
def loadResources():
  for root, dirs, files in os.walk('apps'):
     for file in files:
       if file.endswith(".yaml"):
          with open(os.path.join(root, file), "r") as appFile:
            try:
              appYaml = loadYaml(appFile)
              if appYaml["available"] == True:
                apps_names.append(appYaml["name"])
                apps_versions[appYaml["name"]] = appYaml["availableVersions"]
            except:
              print("*** Error loading file: " + os.path.join(root, file))
              exit(1)
              
  for root, dirs, files in os.walk('resources'):
    for file in files:
       if file.endswith(".yaml"):
          with open(os.path.join(root, file), "r") as resourceFile:
            try:
              resourceYaml = loadYaml(resourceFile)
              if (resourceYaml["kind"] == "Description"):
                descriptions.append(resourceYaml)
              elif (resourceYaml["kind"] == "Dashboard"): 
                dashboards.append(resourceYaml)
              elif (resourceYaml["kind"] == "ExporterConfig"): 
                exporterConfigs.append(resourceYaml)
              elif (resourceYaml["kind"] == "Alert"): 
                alerts.append(resourceYaml)
              elif (resourceYaml["kind"] == "RecordingRule"): 
                recordingRules.append(resourceYaml)
              else: 
                print("File: " + os.path.join(root, file) + " kind: " + resourceYaml["kind"] + " not supported.")
                raise ValueError("File not supported.")
            except:
              print("*** Error loading file: " + os.path.join(root, file))
              exit(1)

# General tests
# Checks that a resource name does not exists in a list
def checkDuplicatedResourceInApp(res,names):
  assert (res['app'] != "") and (type(res['app']) == str) and (not res['app']  in names)
  names.append(res['app'])

# Check that an element is string not empty
def checkStringNotEmpty(res,element):
  assert (res['app'] != "") and (res['kind'] != "") and (type(element) == str) \
        and (element != "") and (element != None)

def checkListNotEmpty(res,element):
  assert (res['app'] != "") and (res['kind'] != "") and (type(element) == list) \
        and (len(element) > 0)

def checkValidJSON(element):
  try:
    json.loads(element)
    return True
  except:
    return False

def checkValidYAML(element):
  try:
    loadYaml(element)
    return True
  except:
    return False

# Only 1 description per app
def testDuplicatedDescriptions(): 
  for res in descriptions:
    checkDuplicatedResourceInApp(res,descriptions_names)

# Only 1 dashboard per app
def testDuplicatedDashboards(): 
  for res in dashboards:
    checkDuplicatedResourceInApp(res,dashboards_names)

# Only 1 Exporter Config per app
def testDuplicatedExporterConfigs(): 
  for res in exporterConfigs:
    checkDuplicatedResourceInApp(res,exporterConfigs_names)

# Only 1 alert per app
def testDuplicatedAlerts(): 
  for res in alerts:
    checkDuplicatedResourceInApp(res,alerts_name)

# Only 1 recording rule per app
def testDuplicatedRecordingRules(): 
  for res in recordingRules:
    checkDuplicatedResourceInApp(res,recordingRules_names)

def testCompulsaryFields():
  for kind in all_resources:
    for res in kind:
      for field in compulsory_fields_all:
        assert (field in res)

# API Version 
# - is string, not empty
# - is v1
def testVersion():
  for kind in all_resources:
    for res in kind:
      checkStringNotEmpty(res,res['apiVersion'])
      assert (res['apiVersion'] == "v1")

# The app
# - is a string, not empty
# - the app asset exists
def testExistsApp():
  for kind in all_resources:
    for res in kind:
      checkStringNotEmpty(res,res['app'])
      assert (res['app'] in apps_names)

# The AppVersion:
# - is a list, not empty
# - exists in the available versions of the App
def testAppVersion():
  for kind in all_resources:
    for res in kind:
      checkListNotEmpty(res,res['appVersion'])
      for appversion in res['appVersion']:
        assert ((res['app'] != "") and (res['kind'] != "") \
          and (appversion in apps_versions[res['app']]))
      
# Maintainers 
# - Is a list, not empty
# - has name (string, not empty)
# - has link (string, not empty)
def testMaintainers():
  for kind in all_resources:
    for res in kind:
      checkListNotEmpty(res,res['maintainers'])
      for maintainer in res['maintainers']:
        checkStringNotEmpty(res,maintainer['name'])
        checkStringNotEmpty(res,maintainer['link'])

# Descriptions elements
# For the resources with description:
# - Is string, not empty
def testDescriptionElement():
  for kind in resources_with_description:
    for res in kind:
      checkStringNotEmpty(res, res['description'])
      
# Tests for data elements
# For the resources with data
# - Is string, not empty
def testDataElement():
  for kind in resources_with_data:
    for res in kind:
      checkStringNotEmpty(res, res['data'])

# Tests for configurations elements
# For the resources with configurations:
# Is list not empty
def testConfigurationsElement():
  for kind in resources_with_configurations:
    for res in kind:
      checkListNotEmpty(res,res['configurations'])
      for config in res['configurations']:
        checkStringNotEmpty(res, config['data'])

# Test in dashboards:
# - in configurations: 
#   - name is string, not empty
#   - kind = grafana|sysdig
#   - image is string, not empty
#   - description is string, not empty
#   - data 
#       - is string, not empty
#       - is valid json  
def testDashboards():
  for res in dashboards:
    for config in res['configurations']:
      checkStringNotEmpty(res,config['name'])
      checkStringNotEmpty(res,config['kind'])
      assert ((res['app'] != "") and (res['kind'] != "") \
        and ((config['kind'] == 'Grafana') or (config['kind'] == 'Sysdig')))
      checkStringNotEmpty(res,config['image'])
      checkStringNotEmpty(res,config['description'])
      checkStringNotEmpty(res,config['data'])
      assert ((res['app'] != "") and (config['name'] != "") and (config['kind'] != "") \
        and (checkValidJSON(config['data']) == True))

# Test in alerts
# - in configurations:
#   - kind = Prometheus|Sysdig
#   - data is string, not empty
#   - data if Prometheus
#       - is valid yaml
#   - data if Sysdig
#       - is valid json
def testAlerts():
  for res in alerts:
    for config in res['configurations']:
      checkStringNotEmpty(res,config['kind'])
      assert ((res['app'] != "") and (res['kind'] != "") \
        and ((config['kind'] == 'Prometheus') or (config['kind'] == 'Sysdig')))
      checkStringNotEmpty(res,config['data'])
      if (config['kind'] == 'Sysdig'):
        assert ((res['app'] != "") and (config['kind'] != "") \
          and (checkValidJSON(config['data']) == True))
      if (config['kind'] == 'Prometheus'):
        assert ((res['app'] != "") and (config['kind'] != "") \
          and (checkValidYAML(config['data']) == True))
