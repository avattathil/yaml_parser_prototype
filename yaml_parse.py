from ruamel.yaml import YAML
from collections import namedtuple

yaml=YAML(typ="safe")

_raw_yaml = """
---
global:
  owner: tonynv@amazon.com
  qsname: sample-taskcat-project
  regions:
    - ap-northeast-1
    - ap-northeast-2
    - ap-southeast-1
    - ap-southeast-2
    - eu-central-1
    - eu-west-1
    - sa-east-1
    - us-east-1
    - us-west-1
    - us-west-2
tests:
  test1:
    parameter_input: debug-input.json
    template_file: debug.template
    post_hook:
      type: lambda
      role: lambda_basic_execution
      source_zip: HelloWorld.zip
    regions:
    - ap-northeast-1
    - ap-northeast-2
    - ap-southeast-1
  test2:
    parameter_input: debug-input.json
    regions:
    - ap-northeast-1
    - ap-northeast-2
    - ap-southeast-1
    template_file: debug.template
"""

from collections import namedtuple
config_dict = yaml.load(_raw_yaml)
_test = []

for cluster in config_dict:
    print (cluster)
    if cluster == 'global':
        for config_global in config_dict[cluster]:
            #print(type (config_dict[cluster][config_global]))
            print(cluster +'.'+ config_global), (config_dict[cluster][config_global])
            _test.append(((cluster +'.'+ config_global), (config_dict[cluster][config_global])))
    elif cluster == 'tests':
        for config_tests in config_dict[cluster]:
            print(config_tests)
            #print(type (config_dict[cluster][config_global]))
            #print(cluster +'.'+ config_tests), (config_dict[cluster][config_tests])
            #print(cluster +'.'+ config_tests)
            #print(cluster +'.'+ config_tests), (config_dict[cluster][config_tests])
            _test.append(((cluster +'.'+ config_global), (config_dict[cluster][config_tests])))


for _t in _test:
	print (_t)

