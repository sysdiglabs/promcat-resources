import pypromcat
import argparse
import json
import os
import re

def generateFileName(resource,configuration):
  if resource["kind"] == "SetupGuide":
    return configuration["name"]
  elif resource["kind"] == "Dashboard":
    fileName = "dashboard"
    fileName = fileName + "-" + configuration["kind"]
    dashboardName = re.sub(r'\s+', '-', configuration["name"])
    dashboardName = re.sub(r'\/+', '-', dashboardName)
    fileName = fileName + "-" + re.sub(r'\s+', '-', dashboardName)
    fileName = fileName + "-" + resource["appVersion"][0]
    fileName += ".json"
    return fileName
  else:
    print("Kind not supported to create filename")
    exit(1)
    

parser = argparse.ArgumentParser(description='Extract the fields data to an external file in configurations.')
parser.add_argument('-f',
                    '--file',
                    required=True,
                    dest='file',
                    help='Original file with data in thefile')
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


yamlFile = pypromcat.loadRawYamlFile(args.file)

if yamlFile["kind"] not in ["SetupGuide","Dashboard"]:
  print("This is not an supported file: " + args.file)
  exit (1)

changed = False
filesDirectory = os.path.dirname(args.file) + "/include"

for configuration in yamlFile["configurations"]:
  if "data" in configuration and configuration["data"] != "":
    if "file" not in configuration:
      if not os.path.isdir(filesDirectory):
        os.makedirs(filesDirectory)
      fileName = generateFileName(yamlFile,configuration)
      with open(filesDirectory + "/" + fileName, "w") as f:
        f.write(configuration["data"])
      configuration["file"] = "include/" + fileName
      del configuration["data"]
      changed = True
    else:
      print("Warning: Found file and data fields in: " + args.file)  


if changed:
  outputformatted = pypromcat.dict2BeautyYaml(yamlFile)
  if args.outputFile is None:
    print(outputformatted)
  else:
    with open(args.outputFile, "w") as f:
      f.write(outputformatted)