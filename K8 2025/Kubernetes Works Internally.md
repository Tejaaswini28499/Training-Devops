How Kubernetes Works Internally.

Explained Simply ...

What Happens When You Deploy to Kubernetes

1. You set up a Kubernetes cluster with a control plane and worker nodes.
2. You define your application using YAML files like Deployment, Service, ConfigMap, etc.
3. You apply the YAML using kubectl apply -f, and the request goes to the API Server.
4. Kubernetes checks the request to decide whether to create, update, delete, or trigger a controller.
5. The API Server stores the object spec in etcd.
6. The appropriate controller detects the new spec, such as a ReplicaSet watching for new Deployments.
7. The controller creates the required resources, such as instructing the scheduler to place new Pods.
8. The scheduler selects a suitable node for each Pod.
9. The Pod spec is sent to the Kubelet on that node.
10. The container runtime pulls the image, creates the container, and runs it inside the Pod.
11. The CNI plugin assigns a network identity and IP address to the Pod.
12. kube-proxy configures routing rules so Services can reach healthy Pods.
13. The Kubelet sends Pod status back to the API Server.
14. If a Pod crashes, the controller recreates it to maintain the desired state.
15 Kubernetes continuously watches and reconciles the cluster to keep it in sync.
