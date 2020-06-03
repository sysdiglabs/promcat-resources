import pypromcat
import argparse
import json


parser = argparse.ArgumentParser(description='Generate from an alerts.yaml with Prometheus alerts a new one with sysdig alerts and description.')
parser.add_argument('-f',
                    '--file',
                    required=True,
                    dest='file',
                    help='Original file with Prometheus alerts')
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

if yamlFile["kind"] != "Alert":
  print("This is not an alert file: " + args.file)
  exit (1)

changed = False

for alert in yamlFile["configurations"]:
  if alert["kind"] == "Sysdig":
    sysdigAlert = json.loads(alert["data"])
    if type(sysdigAlert["alert"]["reNotifyMinutes"]) == str:
      if sysdigAlert["alert"]["reNotifyMinutes"][-1] in pypromcat.timeConversions:
        sysdigAlert["alert"]["reNotifyMinutes"] = pypromcat.prometheusTime2Minutes(sysdigAlert["alert"]["reNotifyMinutes"])
        alert["data"] = pypromcat.dict2BeautyString(sysdigAlert)
        changed = True
  
if changed == True:
  outputformatted = pypromcat.dict2BeautyYaml(yamlFile)
  if (args.outputFile == None):
    print(outputformatted)
  else:
    f = open(args.outputFile, "w")
    f.write(outputformatted)
    f.close()