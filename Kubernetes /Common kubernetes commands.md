## Cluster Management and Context

```
kubectl cluster-info – Display endpoint information about the master and services in the cluster.

kubectl version – Display the Kubernetes version running on the client and server.

kubectl config view – Get the configuration of the cluster.

kubectl config view -o jsonpath='{.users[*].name}' – Get a list of users.

kubectl config current-context – Display the current context.

kubectl config get-contexts – Display a list of contexts.

kubectl config use-context <cluster name> – Set the default context.

kubectl api-resources – List the API resources that are available.

kubectl api-versions – List the API versions that are available.

kubectl get all --all-namespaces

-A – List pods, services, daemonsets, deployments, replicasets, statefulsets, jobs, and CronJobs in all namespaces, not custom resource types. Note the alias for --all-namespaces is -A

```