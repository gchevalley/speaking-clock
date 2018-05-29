# speaking clock basic auth

## Container

`export FLASK_AUTH_PASSWORD="<user>"`

`export FLASK_AUTH_USERNAME="<password>"`

### build docker image
`docker build -t gchevalley/speaking-clock-basic-auth .`

## Kubernetes

### create a deployment
`kubectl run speaking-clock --image=gchevalley/speaking-clock-basic-auth --port=5000`

### expose service
`kubectl expose deployment speaking-clock-basic-auth --type=NodePort`

### ingress rules
`kubectl create -f ingress-speaking-clock-basic-auth.yaml`
