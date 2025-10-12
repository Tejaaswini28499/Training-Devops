Why EKS
while using EKS - control plane is fully managed by AWS only but worker node we need to control but if we use AWS Fargate worker node is also controlled by AWS only, without using EKS like if we are using KOPS machine we need to take care of certificate renewal, ETCD crash need to be fixed, API server goes down we have to check 
<img width="1009" height="271" alt="image" src="https://github.com/user-attachments/assets/f7a17d1c-d202-46f6-999e-64ced6201710" />

note: whenever the Ingress controller will find the Ingress resource the load-balancer is created if its already created then it will configure the rules accordingly mentioned in the Ingress.yml file 
user -> Ingress-> service-> pod 

Step by step configuration on EKS 
1. Install Kubectl on your machine based on Linux, Windows and MACOS
2. Install eksctl 
3. Install AWS CLI
4. create a cluster: eksctl create cluster --name demo-cluster --region us-east-1 --fargate : use fargate only unless there are some specific requirement use ec2 instance note: eksctl utility is taken care of cluster creation and VPC creation public subnet private subnets bcz our application will be deployed on private subnet and this everything is taken care by eksctl
5. The cluster will be created and now we have to attach the Identity provider so that we can if pod require to talk with s3 or any AWS resource cloud watch and others. AWS allows you to attach any Identity provider, IAM you can used, LDAP can be used many more here we are using IAM.
6. fargate profiles: will be create while the cluster is being created and you can there are namespaces created for this and you can deploy only on this two namespaces default and kubesystem if you need to deploy to other namespace you need to create additional fargate profile
7. Download kubeconfig tab instead of going to UI everytime and check installing kubeconfig we can directly check that in CLI : command to download : aws eks update-kubeconfig --name demo-cluster --region us-east-1<img width="1021" height="28" alt="image" src="https://github.com/user-attachments/assets/7bade974-e8a5-41f6-af83-4f77064a33a5" />

8. create a new name space to deploy the application create it using the command given below
9. <img width="712" height="114" alt="image" src="https://github.com/user-attachments/assets/7e0f67a3-1c44-4368-aa34-effed43142f0" />

10. Deploy the deployment, service and Ingress.yml files 
11. deploy Ingress controller, before this we need to install IAM OIDC provide because the Ingress controller to talk Appln Load Balancer the controller is again the k8 pod and that needs to talk to other resources create it using the command given below
12. <img width="1146" height="79" alt="image" src="https://github.com/user-attachments/assets/8f2c5b2a-089b-4f99-944b-c6f8e9a510b1" />

13. attach the IAM ALB policy(provided by AWS ALB only)
14. create that ALB policy
15. Attach the role to the service account of the Pod
<img width="1132" height="588" alt="image" src="https://github.com/user-attachments/assets/41b3b475-f1cf-44e7-8e09-3cc60c1f101e" />

16. using helm install Ingress controller
17. <img width="1074" height="72" alt="image" src="https://github.com/user-attachments/assets/05ca7b61-1eda-449b-abcd-7ba32a9641e0" />

18. verify if the load balancer is created and at least have 2 replicas of it using below command

