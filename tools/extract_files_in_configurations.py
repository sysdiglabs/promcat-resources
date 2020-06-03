import pypromcat
import argparse
import json
import os
import re

def generateFileName(resource,configuration):
  if resource["kind"] == "ExporterConfig":
    return configuration["name"]
  elif resource["kind"] == "Dashboard":
    fileName = "dashboard"
    fileName = fileName + "-" + configuration["kind"]
    dashboardName = re.sub(r'\s+', '-', configuration["name"])
    dashboardName = re.sub(r'\/+', '-', dashboardName)
    fileName = fileName + "-" + re.sub(r'\s+', '-', dashboardName)
    fileName = fileName + "-" + resource["appVersion"][0]
    fileName = fileName + ".json"
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

if yamlFile["kind"] not in ["ExporterConfig","Dashboard"]:
  print("This is not an supported file: " + args.file)
  exit (1)

changed = False
filesDirectory = os.path.dirname(args.file) + "/include"

for configuration in yamlFile["configurations"]:
  if "data" in configuration:
    if configuration["data"] != "":
      if "file" not in configuration:
        if not os.path.isdir(filesDirectory):
          os.makedirs(filesDirectory)
        fileName = generateFileName(yamlFile,configuration)
        f = open(filesDirectory + "/" + fileName, "w")
        f.write(configuration["data"])
        f.close()
        configuration["file"] = "include/" + fileName
        del configuration["data"]
        changed = True
      else:
        print("Warning: Found file and data fields in: " + args.file)  

  
if changed == True:
  outputformatted = pypromcat.dict2BeautyYaml(yamlFile)
  if (args.outputFile == None):
    print(outputformatted)
  else:
    f = open(args.outputFile, "w")
    f.write(outputformatted)
    f.close()