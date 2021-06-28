import os
import sys
import json
from jinja2 import Environment, FileSystemLoader

home_dir = '/home/clowder'
data_dir = '/home/clowder/data'

# Exit if extractor_info.json does not exist
if not os.path.isfile(os.path.join(data_dir,'extractor_info.json')):
    print("Must have 'extractor_info.json' file present to build extractor!")
    sys.exit(1)

# Load extractor_info.json file
with open(os.path.join(data_dir,'extractor_info.json')) as f:
  extractor_info = json.load(f)    

# Selecting subset of extractor_info related to building Dockerfile
try:
    extractor_build_info = extractor_info['build']
except:
    print("""
          Must specify build section in extractor_info.json!\n
          For example:\n
          "build": {
            "language": "python",
            "base": "python:3.8",
            "dependencies": {
              "pandas":"",
              "jinja2":"3.0.1" },
            "module": "wordcount",
            "function": "wordcount"
            }
         """)
    sys.exit(1)
            
# Set template environement for jinja2
env = Environment(loader = FileSystemLoader(
                  os.path.join(home_dir,"templates/{}".format(extractor_build_info['language']))), 
                  trim_blocks=True,
                  lstrip_blocks=True)

# Create simple_extractor.py
extractor = env.get_template('simple_extractor_template.txt')
extractor_output = extractor.render(extractor_build_info = extractor_build_info)

with open(os.path.join(data_dir,"simple_extractor.py"), "w") as fe:
    fe.write(extractor_output)

# Create Dockerfile
dockerfile = env.get_template('docker_template.txt')
dockerfile_output = dockerfile.render(extractor_build_info = extractor_build_info)

with open(os.path.join(data_dir,"Dockerfile"), "w") as fd:
    fd.write(dockerfile_output)
