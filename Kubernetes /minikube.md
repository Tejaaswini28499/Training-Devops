## Minikube installation

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

```
minikube start (If you get driver error install docker according to machine like ubuntu, Linux)
minikube start --driver=docker
kubectl get po -A
minikube kubectl -- get po -A
alias kubectl="minikube kubectl --"
minikube dashboard
```
## minikube Requriement

```
t3.medium with 2CPU and 4GB memory
always use Ubuntu
adjust vloume as requried
