import pypromcat
import argparse


parser = argparse.ArgumentParser(description='Parser to extract Sysdig alerts and split in different configuration elements.')
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

sysdigAlertsArray = pypromcat.createArrayOfSysdigAlerts(args.file)
promcatAlerts = pypromcat.sysdigAlerts2PromcatConfigurations(sysdigAlertsArray)
outputformatted = pypromcat.dict2BeautyYaml(promcatAlerts) 
if (args.outputFile == None):
  print(outputformatted)
else:
  f = open(args.outputFile, "a")
  f.write(outputformatted)
  f.close()