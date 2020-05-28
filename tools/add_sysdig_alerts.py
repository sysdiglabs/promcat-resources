import pypromcat
import argparse


parser = argparse.ArgumentParser(description='Parser to extract Sysdig alerts from Prometheus alerts in PromCat resources.')
parser.add_argument('-f',
                    '--file',
                    required=True,
                    dest='file',
                    help='File to extract the alerts from')

try:
    args = parser.parse_args()
except BaseException as exception:
    # parser will print either help or syntax error details
    exit(1)

yamlFile = pypromcat.loadYamlFile(args.file)
sysdigAlertsArray = pypromcat.createArrayOfSysdigAlerts(yamlFile)
print(pypromcat.dict2BeautyString(sysdigAlertsArray))