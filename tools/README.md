# Alerts generator
The tool generate_alerts_file.py takes as input an alerts file with Prometheus alerts and generates another one with Sysdig alerts and description filled. 

The usage is the following:
```
# Output in console
python3 generate_alerts_file.py -f inputfile.yaml 

# Output to a file
python3 generate_alerts_file.py -f inputfile.yaml -o outputfile.yaml
```
# Files extractor
The tool extract_files_in_configurations.py takes as input a dashboards or exporter-config file and extracts
the content of the 'data' fields of the 'configurations' elements into different files under the ./files/ subdirectory.

The usage is the following:
```
# Output in console
python3 extract_files_in_configurations.py -f inputfile.yaml 

# Output to a file
python3 extract_files_in_configurations.py -f inputfile.yaml -o outputfile.yaml
```

# Script toolbox

Extract names of panels in Grafana dashboards:
```
grep "\"title\": " file_name.json | sed 's/\"title\": \"'// | sed 's/\",//' | sed -e 's/^ *//g' |  code -
```

Extract names and sentences from grafana dashboards:
```
grep "\"title\": \|\"expr\": " filename.json | sed 's/\"title\": \"'// | sed 's/\"expr\": \"'// | sed 's/\",//' | sed -e 's/^ *//g' |  code -
```

Extract names of panels in Sysdig dashboards:
```
grep "\"name\": " filename.json | sed 's/\"name\": \"'// | sed 's/\",//' | sed -e 's/^ *//g' | code -
```

Change a string in all files of a directory:
```
find . -type f -exec sed -i -e 's/STRINGA/STRINGB/g' {} \;
```

Change a string in files starting with extension ".yaml" of a directory:
```
find . -name \*.yaml -type f -exec sed -i -e 's/STRINGA/STRINGB/g' {} \;
```

Get all the names of the metrics containing "nginx" from a Prometheus server: 
```
curl http://localhost:9090/api/v1/label/__name__/values | jq '.' | grep "nginx" | sed -e "s/\"//" | sed -e "s/\",//" | sed -e 's/^ *//g' | code -
```

Extract HELP lines of exporter
```
curl -s http://localhost:9121/metrics | grep "HELP redis" | sed 's/# HELP //' | code -
```

Execute a python script in all the alert files: 
```
find . -name \*alerts*.yaml -type f -exec python3 tools/script.py -f '{}' -o '{}'_sysdig.yaml \;
```
