import pypromcat
import argparse
import json
import os
import re


parser = argparse.ArgumentParser(description='Extract the fields description to an external file.')
parser.add_argument('-f',
                    '--file',
                    required=True,
                    dest='file',
                    help='Original file with description field')
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

descriptionFileNames = {
  'Description': 'README.md',
  'SetupGuide': 'INSTALL.md',
  'Alert': 'ALERTS.md',
  'RecordingRule': 'RECORDING-RULES.md'
}
yamlFile = pypromcat.loadRawYamlFile(args.file)

if yamlFile["kind"] not in ["Description","SetupGuide","RecordingRule","Alert"]:
  print("This is not an supported file: " + args.file)
  exit (1)

changed = False
filesDirectory = os.path.dirname(args.file)

if 'description' in yamlFile:
  if yamlFile['description'] != '':
    if 'descriptionFile' not in yamlFile:
      content = yamlFile["description"]
      if yamlFile["kind"] == 'Description':
        content += "\n\n# Attributions\n"
        content += yamlFile['maintainers']
        del yamlFile['maintainers']
      fileName = descriptionFileNames[yamlFile['kind']]
      f = open(filesDirectory + "/" + fileName, "w")
      f.write(content)
      f.close()
      yamlFile['descriptionFile'] = fileName
      del yamlFile['description']
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