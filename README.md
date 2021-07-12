Current design is to support the easy integration of Python functions with pyclowder to create simple extractors as described here: https://github.com/clowder-framework/pyclowder#simpleextractor.

## Running
Run the following command in the same directory as your Python code and extractor_info.json file (described below):
```
docker run -ti -v ${PWD}:/home/clowder/data hub.ncsa.illinois.edu/clowder/generator:latest
```
This will produce two files:
1. Dockerfile

This file is used to create a Docker container that includes your user code. This Docker container will be deployed to your Clowder instance enabling you to run your code as a Clowder extractor. To create the Docker container execute the following command:

```
docker build -t <your image tag> .
```
2. simple_extractor.py

This file wraps your user code enabling it to run/interact with Clowder. The Dockerfile adds this file to the Docker container and executes this file when the Docker container is run.

## Dependencies
In order to create a simple extractor using the clowder/generator, two files are needed:
1. user code

User code must be a function that returns a dictionary containing metadata and/or previews.

2. extractor manifest

A file called extractor_info.json file that contains metadata about your extractor. In order to use the generator you will need to add the following section to your extractor manifest:

```JSON
"build": {
  "language": "python",
  "base": "python:3.8",
  "dependencies": {
    "pandas":"",
    "jinja2":"3.0.1" },
  "module": "wordcount",
  "function": "wordcount"
}
```
1. Language (REQUIRED): the coding language used
2. Base (OPTIONAL): the docker image to be used. If none is specified, the default for Python is (python3-slim).
3. dependencies (OPTIONAL): any packages on which your code depends. Versions can be left empty as shown above. For Python, if a requirements.txt file is present, it will be used instead.
4. module (REQUIRED): the name of your file that contains your code. In the above example, that would be wordcount.py
5. function (REQUIRED): the function to be called. In the above example, the function wordcount() would reside within wordcount.py
