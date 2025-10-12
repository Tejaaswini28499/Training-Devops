Why EKS
while using EKS - control plane is fully managed by AWS only but worker node we need to control but if we use AWS Fargate worker node is also controlled by AWS only, without using EKS like if we are using KOPS machine we need to take care of certificate renewal, ETCD crash need to be fixed, API server goes down we have to check 

note: whenever the Ingress controller will find the Ingress resource the load-balancer is created if its already created then it will configure the rules accordingly mentioned in the Ingress.yml file 
user -> Ingress-> service-> pod 

Step by step configuration on EKS 
1. Install Kubectl on your machine based on Linux, Windows and MACOS
2. Install eksctl 
3. Install AWS CLI
4. create a cluster: eksctl create cluster --name demo-cluster --region us-east-1 --fargate : use fargate only unless there are some specific requirement use ec2 instance note: eksctl utility is taken care of cluster creation and VPC creation public subnet private subnets bcz our application will be deployed on private subnet and this everything is taken care by eksctl
5. The cluster will be created and now we have to attach the Identity provider so that we can if pod require to talk with s3 or any AWS resource cloud watch and others. AWS allows you to attach any Identity provider, IAM you can used, LDAP can be used many more here we are using IAM.
6. fargate profiles: will be create while the cluster is being created and you can there are namespaces created for this and you can deploy only on this two namespaces default and kubesystem if you need to deploy to other namespace you need to create additional fargate profile
7. Download kubeconfig tab instead of going to UI everytime and check installing kubeconfig we can directly check that in CLI : command to download : aws eks update-kubeconfig --name demo-cluster --region us-east-1
8. create a new name space to deploy the application create it using the command given below
9. Deploy the deployment, service and Ingress.yml files 
10. deploy Ingress controller, before this we need to install IAM OIDC provide because the Ingress controller to talk Appln Load Balancer the controller is again the k8 pod and that needs to talk to other resources create it using the command given below
11. attach the IAM ALB policy(provided by AWS ALB only)
12. create that ALB policy
13. Attach the role to the service account of the Pod
14. using helm install Ingress controller
15. verify if the load balancer is created and at least have 2 replicas of it using below command

