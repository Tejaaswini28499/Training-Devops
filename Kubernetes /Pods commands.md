## Pod Commands

```
kubectl get pod – List one or more pods.

kubectl get pods --sort-by='.status.containerStatuses[0].restartCount' – List pods Sorted by Restart Count.

kubectl get pods --field-selector=status.phase=Running – Get all running pods in the namespace.

kubectl delete pod <pod_name> – Delete a pod.

kubectl describe pod <pod_name> – Display the detailed state of a pods.

kubectl create pod <pod_name> – Create a pod.

kubectl exec <pod_name> -c <container_name> <command> – Execute a command against a container in a pod. Read more: Using Kubectl Exec: Connect to Your Kubernetes Containers

kubectl exec -it <pod_name> /bin/sh – Get an interactive shell on a single-container pod.

kubectl top pod – Display Resource usage (CPU/Memory/Storage) for pods.

kubectl annotate pod <pod_name> <annotation> – Add or update the annotations of a pod.

kubectl label pods <pod_name> new-label=<label name> – Add or update the label of a pod.

kubectl get pods --show-labels – Get pods and show labels.

kubectl port-forward <pod name> <port number to listen on>:<port number to forward to> – Listen on a port on the local machine and forward to a port on a specified pod.

```