import pytest
import yaml
import os

apps = []
apps_names = []

def loadYaml(input):
  return yaml.full_load(input)
  
@pytest.fixture(scope="session", autouse=True)
def loadApps():
  for root, dirs, files in os.walk('apps'):
     for file in files:
       if file.endswith(".yaml"):
          with open(os.path.join(root, file), "r") as appFile:
            try:
              appYaml = loadYaml(appFile)
              apps.append(appYaml)
            except:
              print("*** Error loading file: " + os.path.join(root, file))
              exit(1)


def testDuplicatedApp(): 
  for app in apps:
    assert (app['name'] != "") and (type(app['description']) == str)
    assert (app['name'] != "") and (not app['name']  in apps_names)
    apps_names.append(app['name'])

def testVersion(): 
  for app in apps:
    assert (app['name'] != "") and (type(app['description']) == str)
    assert (app['name'] != "") and (app['apiVersion'] == "v1")

def testKind(): 
  for app in apps:
    assert (app['name'] != "") and (type(app['description']) == str)
    assert (app['name'] != "") and (app['kind'] == "App")

def testDescription(): 
  for app in apps:
    assert (app['name'] != "") and (type(app['description']) == str)
    assert (app['name'] != "") and (app['description'] != "")

def testIcon(): 
  for app in apps:
    assert (app['name'] != "") and (type(app['description']) == str)
    assert (app['name'] != "") and (app['description'] != "")
    
def testKeywords(): 
  for app in apps:
    assert (app['name'] != "") and (type(app['keywords']) == list)
    assert (app['name'] != "") and (len(app['keywords']) > 0)
    
def testAvailableVersions(): 
  for app in apps:
    assert (app['name'] != "") and (type(app['availableVersions']) == list)
    assert (app['name'] != "") and (len(app['availableVersions']) > 0)

def testAvailable(): 
  for app in apps:
    assert (app['name'] != "") and (type(app['available']) == bool)
    assert ((app['name'] != "") and 
      (((app['available']) == True and "available" in app['keywords']) or 
      (app['available']) == False and "coming soon" in app['keywords']))
