# speaking clock

## Container

### build docker image
docker build -t gchevalley/speaking-clock .

## Kubernetes

### create a deployment
kubectl run speaking-clock --image=gchevalley/speaking-clock --port=5000

### expose service
kubectl expose deployment speaking-clock --type=NodePort

### ingress rules
kubectl create -f ingress-speaking-clock.yaml
