import pypromcat
import argparse


parser = argparse.ArgumentParser(description='Parser to change maintainers element and leave it only in the allowed resources.')
parser.add_argument('-f',
                    '--file',
                    required=True,
                    dest='file',
                    help='File to extract the alerts from')
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

kinds_with_maintainers = ['Description']

yamlFile = pypromcat.loadRawYamlFile(args.file)
if yamlFile["kind"] in kinds_with_maintainers:
  yamlFile["maintainers"] = "Configuration files and dashboards maintained by [Sysdig team](https://sysdig.com/)."
else:
  del yamlFile["maintainers"]

outputformatted = pypromcat.dict2BeautyYaml(yamlFile)
if (args.outputFile == None):
  print(outputformatted)
else:
  f = open(args.outputFile, "w")
  f.write(outputformatted)
  f.close()