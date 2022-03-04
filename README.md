# pyKVStore
pyKVStore Service with Python flask for in memory KV store

### Pre-requisites

Python3 with flask
```sh
pip install -r requirements.txt
```

### How to Run

Run the program (Make sure input.csv is in same directory from where you are running below command)
```sh
$ cd pyKVStore
$ python src/app.py
```
Access Application
  - [Add keys](http://localhost:8000/set)
  - [get key](http://localhost:8000/get/test)
  - [getall keys](http://localhost:8000/getall)
  - [Search key with prefix](http://localhost:8000/search?prefix=test)
  - [Search key with suffix](http://localhost:8000/search?suffix=test)

### Kubernetes
Application is easy to install and deploy in Kubernetes cluster with [manifests file](kubernetes/app.yaml).

### Docker
Application is easy to install and deploy in a Docker container.

```sh
cd pyKVStore
docker build -t pyKVStore:1.0 .
```
This will create the pyKVStore application image and pull in the necessary dependencies. 
By default application runs on 8000 port inside container if you want to change please update src/app.py file. Application will be exposed on local 8000 port as well

```sh
docker run --name pyKVStore-dev -d -p 8000:8000 --restart="always" pyKVStore:1.0
```

### CI/CD

CI/CD is set up with Jenkins. You can refer to [Jenkinsfile](Jenkinsfile) inside repo.
Jenkins CI/CD consists of below stages automatically provided dependent stages are successful
  - Build code
  - Run Unit tests
  - Deploy Container
  - Run Smoke Tests

### Prometheus

[Prometheus Metrics](http://localhost:8000/metrics).
