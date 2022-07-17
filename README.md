# Apollo Project Task
In this repository, we want to deploy two versions of a workflow task on the available resources. We user Docker and Apache OpenWhisk as our resources.
This Project is based on [Apollo Project](https://github.com/Apollo-Core/Tutorial)


## Dependency
### Apache OpenWhisk
You can use the [Apache Openwhisk documentation](https://openwhisk.apache.org) for installation and more use cases or you can install it by the below commands.

You will need Docker, Java and Node.js available on your machine before installation. 


```bash
$ cd ./Scripts/
$ ./ApacheOpenWhisk.sh
```

After successful installation you can use the Apache OpenWhisk by three way.

- Using WSK-CLI tool
- Rest API
- UI

The Apache OpenWhisk provide two http endpoint for users.
- UI Endpoint: [http://SERVER_ADDRESS:3232/](http://SERVER_ADDRESS:3232/)
- API Endpoint: [http://SERVER_ADDRESS:3233/api/v1/](http://SERVER_ADDRESS:3233/api/v1/)

### WSK-CLI
For installing cli tool of Apache OpenWhisk, download the binary file of WSK-CLI from [https://s.apache.org/openwhisk-cli-download](https://s.apache.org/openwhisk-cli-download) and add wsk script path into the PATH variable of your machine.

### FAAS-CLI
For installing faas-cli run the bellow command:

```bash
$ curl -sSL https://cli.openfaas.com | sudo sh
```

## Tasks
We have two version of one workflow task. In this task, we want to  search through a given text string and count the occurrences of a given string pattern in that text

### Task1
In this task we just want count the occurences of given pattern.   
The below diagram shows the workflow structure for this task.
<p align="center">
  <img src="./Media/Task1.png" />
</p>


### Task2
In this task we just want count the occurences of given pattern and remove (total occurance - threshold) numbers of the given pattern from end of the give string if (total occurance > threshold).
The below diagram shows the workflow structure for this task.
<p align="center">
  <img src="./Media/Task2.png" />
</p>

## Create Resources
In this project you can choose multiple sources for deploying your resources. In this document we consider local node and Apache OpenWhisk as our sources.

### Deploy on Local Node
For deploy on local node you must run the bellow command.

```bash
$ cd ./FunctionTask<TASK_NUMBER>/openfaas
$ ./build.sh
```

After successful installation the mentioned docker images which are mentioned in "./FunctionTask<TASK_NUMBER>/openfaas/stack.yml" file will be created and also the typeMappings.json will be updated. You can push these docker images into the your docker hub account.

### Deploy on Apache OpenWhisk
Apache OpenWhisk need authentication and its authentication process is different from AWS so for integrating the Apache OpenWhisk with the provided of demo application which is provided by Apollo project, you must create a proxy server for communicate with Apache OpenWhisk server.

#### Create Proxy Server
Firstly you must edit the configuration values in config.py file and fill it with valid values based on your Apache OpenWhisk server configurations. Then run these command for running the web server:
```bash
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP="webserver"
$ flask run --host 0.0.0.0
```
#### Create Resources
For deploy on Apache OpenWhisk you must rename wsk.config.example file into wsk.config and fill it with valid values based on your Apache OpenWhisk server configurations and your proxy server configurations. For creating the resources, you must run the bellow command.

```bash
$ cd ./FunctionTask<TASK_NUMBER>/openwhisk
$ ./deploy.sh create
$ ./deploy.sh --mapping
```

After successful installation the typeMappings.json file will be updated by valid values. You can push these docker images into the your docker hub account.


## Run Application
For running the task on demo application you must put the generated files in previous steps into ./Application folder. For update values run below commands:

```bash
$ cd ./Application
$ cp ../Workflows/Task1.yml ./task1Input/
$ cp ../FunctionTask1/openfaas/typeMappings.json ./Task1Input/typeMappingsDocker.json
$ cp ../FunctionTask1/openwhisk/typeMappings.json ./Task1Input/typeMappingsOpenWhisk.json
$ cp ../Workflows/Task2.yml ./Task2Input/
$ cp ../FunctionTask2/openfaas/typeMappings.json ./Task2Input/typeMappingsDocker.json
$ cp ../FunctionTask2/openwhisk/typeMappings.json ./Task2Input/typeMappingsOpenWhisk.json
```
Then for running tasks, run the related launch file for each tasks which is in ./Application/launches/ path.