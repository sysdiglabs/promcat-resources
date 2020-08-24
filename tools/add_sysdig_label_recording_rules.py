import pypromcat
import argparse
import os

parser = argparse.ArgumentParser(description='Adds the label sysdig: true to all the recording rules.')
parser.add_argument('-f',
                    '--file',
                    required=True,
                    dest='file',
                    help='Original file with Prometheus recording rules')
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
# filesDirectory = os.path.dirname(args.file)

for group in yamlFile["groups"]:
  for rule in group["rules"]:
    if not "labels" in rule:
      rule["labels"] = {}
    rule["labels"]["sysdig"] = True

outputformatted = pypromcat.dict2BeautyYaml(yamlFile)
if args.outputFile is None:
    print(outputformatted)
else:
    f = open(args.outputFile, "w")
    f.write(outputformatted)
    f.close()