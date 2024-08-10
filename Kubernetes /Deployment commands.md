## Deployment commands
```
kubectl get deployment – List one or more deployments.

kubectl describe deployment <deployment_name> – Display the detailed state of one or more deployments.

kubectl edit deployment <deployment_name> – Edit and update the definition of one or more deployments on the server.

kubectl create deployment <deployment_name> – Create a new deployment.

kubectl delete deployment <deployment_name> – Delete deployments.

kubectl rollout status deployment <deployment_name> – See the rollout status of a deployment.

kubectl set image deployment/<deployment name> <container name>=image:<new image version> – Perform a rolling update (K8S default), set the image of the container to a new version for a particular deployment.

kubectl rollout undo deployment/<deployment name> – Rollback a previous deployment.

kubectl replace --force -f <configuration file> – Perform a replace deployment — Force replace, delete and then re-create the resource.
```