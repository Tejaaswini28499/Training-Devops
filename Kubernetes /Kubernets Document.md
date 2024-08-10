## How to Deploy a service

```
You have to first create a service if its not there in deployment when you do the kubectl get deployment
or else
You need to create a file eg:"deploymentnew.yaml" and pass the necessary instruction inside that like what is the kind here its Deployment
How much replicaset requried
How much Specs and so on
```

## YAML Format to create/Config the Deployment 

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21.6
        ports:
        - containerPort: 80
```

## Commands to create/Config
```
kubectl apply -f nginx-deployment.yaml
```
## Commands to Delete
```
kubectl delete -f nginx-deployment.yaml
```
## Delete by Resource Type and Name

```
kubectl delete deployment nginx-deployment
```
## Delete All Resources of a Specific Type
```
kubectl delete deployments --all
```