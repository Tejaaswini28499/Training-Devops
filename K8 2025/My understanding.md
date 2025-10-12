why Kubernetes?? 

docker: life of container is very short --container 1 taking lot of memory container 100 will not schedule- single host one - docker is container platform and k8 id container orch platform 
auto healing 
auto scaling
docker doesn't support enterprise level support

all this problem is solving by Kubernetes

1. Kubernetes is installed as cluster - it is installed in Master node arch, In faulty appln kuberentes will have that in different instance 
2. controlling is getting damage or going down : API server container is going down it will rollout a new pod is created 
3. Deployment yaml file increase my replicas whenever there is a festival or function or there is HPA - directly load threshold of 80% increase machinces
4. docker platform cannot be on production, Kubernetes is reaching 100% towards enhancing - like advance load balancing, advance networking, security related things 
Multiple enterprise support


why Kubernetes is called K8's??

Kubernetes Arch:
control plane-master node components - api server, etcd, control manager, schedular - controlling the components 
Data Plane- worker node components - kubelet, kube proxy, container runtime - executing the components


Worker node or Data plane:

one master and one worker - request always goes to master- control plane
when you deploy pod kubelet is responsible for running a pod, in docker we have docker engine and dockerstrim 
even to run a pod we need container runtime 
only diff is in Kubernetes dockerstrim is not mandatory, you have container-d, crio, dockerstrim or any container runtimes which implement container interface but docker have only one support dockerstrim
kubelet ensure the pods needs to always run if not it will inform API server something has gone wrong so we need to reschedule 


Like bridge networking in docker we have kube proxy here every container should be having an IP address allocated and should have load balancing capabilities 
kubeproxy: provides networking uses IP table, load balancing and Ip add.


Master node or control plane 
only we the above components we can run the appln but not the enterprise level appln, should be pod create on node 1 or node 2 there can be many like this, there should be a heart or core component in Kubernetes that will be done by API server : it exposes the Kubernetes it takes request from external world.  

scheduler is responsible of scheduling the pod or resources deciding will be done by API server but scheduler will act upon this it will receive information from API server 

etcd: backing store of entire cluster, is key value store, restore the cluster information this is imp

controller manager :  to support autoscaling it has some controllers - like replica set - is maintaining state of pods, if 2 pods gets created it should ensure both are working state that is taken care by replica set controller 
so there should a component to check whether the controllers are working fine that is done by controller manager 

CCM- cloud controller manager - The Cloud Controller Manager (CCM) is responsible for integrating Kubernetes with the underlying cloud provider (AWS, Azure, GCP, OpenStack, etc.).

It makes sure that Kubernetes clusters can interact with cloud-specific resources such as:

Load balancers

Storage volumes

Networking routes

Nodes (VM lifecycle)
Why separate CCM?

Before Kubernetes v1.6, cloud-specific code was inside the kube-controller-manager.
To make Kubernetes more modular and cloud-agnostic, the CCM was separated out.

Now:

kube-controller-manager handles Kubernetes generic resources.

cloud-controller-manager handles cloud provider-specific resources.

-----------------------------------------------------------------------

Deployment file
In docker we run have container directly, but k8 we are running it as pod 
pod is single container sometime it will be 2-3 containers, more container in one pod it will shared storage communication is easy, pod is like a wrapper for container pod will be having IP not containers
kubectl: command line tool for Kubernetes cluster


pod.yml- will just create a pod but it doesn't have autohealing and auto scaling properties for his we need deployment.yml files only 

deployment.yml : here we write the deployment file and we have replicaset which is a controller and it always need to maintain the desired state in the cluster as in deployment.yml file. there are default controllers in kuberenetes but we can customise this like argo-cd and others. mainly replicaset will help with auto healing.
 
eg: in cluster we have 100 pods and one was deleted by mistake the auto healing will ensure the desired state and cluster state must be same and regenerate the deleted pod.
 <img width="880" height="517" alt="image" src="https://github.com/user-attachments/assets/db5c2b15-cbf7-4960-99ad-430dce36b8ea" />

note: whenever a change made in container in deployment.yml the new set of replica will be created when there is a new rollout the new replicset is created the old once dont get delete bcz if you want to rollback to older version by default k8 will store last 10 replicaset by default

kubectl rollout undo deployment/ngix-deployment --to revision =1 
the above command will rollback to previous version, revision =2 rollback to 2 previous version back 

commands:
kubectl get pods
kubectl get pods -o wide - will give you ip address
kubectl apply -f deployment.yml 
kubectl describe pod 
kubectl get deploy
kubectl get rs - replicaset
kubectl get pods -w - real time you can see what's happening 
kubectl get svc


Service file

Why service??
1.	load balancing 
2.	service discovery 
3.	Expose to external world

Load balancing :
service will act as a load balancer i.e., each and every pod will be having ip address and whenever the pod deleted and created a new pod the ip address will change and what this service will do is load balancing how it does is with the help of kube-proxy.
note:by default the deployment doesn't have loadbalancing only if we use service.yml or services will get to use Loadbalancing

eg: as you have 100's of users using your appln you can have a single replica there should be multiple pods running and each pods will be having different ip you cannot say 25 users use 173.2.3.4 another 25 use 173.2.3.5 other 25 use 173.2.3.6 and others 173.2.3.7 instead use service.yml so using load balancing it would help even when the pod is destroyed and generated a new pod service file will help. when creating a service you would give a name say payment.default.svc the kube-proxy will send the traffic to this link payment.default.svc

Service discovery:
even though load balancing is happening the ip mapping issue still exists in service, bcz service also try mapping to ip address only like how the user use to face like they will be sending to same ip so to resolve this issue what service said is I'll not bother about ip address itself will have something called labels and selectors
<img width="780" height="514" alt="image" src="https://github.com/user-attachments/assets/f9636c5e-1c10-4be6-817f-c15b0216a35d" />

every pod that will get created will have a label and it will be common name or label to all pods. so if the service keep track of label rather then ip address then the issue is solved with service discovery. also instead of service keeps tracks of IP address it will now keeps track on labels 

Expose to external world:
service will allow you to expose pod to outside k8 service and when you create a service this can be created a 3 types: 
1.	cluster ip - want to access inside the Kubernetes cluster this service is been used if they have container network, cluster network then only can access if you have access if you have access to EC2 ip but not container network then you can't if the service type is cluster ip
2.	node port - inside organization any one can access or within network they cannot access master but can access all worker nodes - anyone have access to worker nodes, or Ec2 ip address or VPC network traffic can access the pods 
3.	load balancer - this service will expose the pods to external world, anyone in the world can access,  


How service works eg:
<img width="810" height="109" alt="image" src="https://github.com/user-attachments/assets/8be03979-c01c-43c1-a2c5-ba0cd8fb02e1" />

always pick the selector label from template(pod templete) not from the meta data of deployment.yml
nodeport number you can use as it is which is 30007 or you can even change but keep the target port(on which our appln is exposed can find in deockerfile) as it is here in abhishek video it is 8000
clusterip(10.101.63.207) with 80 is mapped with the nodeport 300007 which means even if we do minikube ssh and go inside the cluster and do curl http://10.101.63.207.80/demo the traffic will still be able to access this is not recommended but if you are accessing ec2 instance take that ip eg:  curl http://192.168.64.5.300007/demo you will be able to access this also if 

<img width="1068" height="604" alt="image" src="https://github.com/user-attachments/assets/3fe32ffe-408d-4410-9e90-d4a3a28eb5a3" />

note: you have installed minikube on you laptop you can still be able to access the link from internet bcz the minikube ip and laptop ip are same so will be able to access
if it should be accessed world wide then give the type as load balancer for this the external ip will be added for cluster ip and Nodeport the external ip's are not allocated and in minikube the external ip would be shown pending as this is done by CCM (cloud controller manager) AWS or Azure or GCP minikube cannot have this privileges so

what is sticky session in kubernetes : 

what are enterprise loadbalancer support? - exposing one specific ip address 


why Ingress ??
enterprise and TLS load balancing capabalities 
service of type lb the cloud provider will charge for static public ip address as each and every lb was creating static public ip

service in k8 was doing very simple loadbalanicing but enterprise loadbalancer support was giving very good feature which k8 was not providing

exposes using loadbalancer mode in service in cloud was charging more as it was static public IP address as each and every lb having public ip 


what is Ingress?? - its just lb sometimes lb + API gateway
will allow k8 users to use lb, user will create resource called Ingress in k8 it will tell lb providers to create something called Ingress controller 


what if you need path based routing bcz service wont provide as its just have round robbin type of lb
The lb provided Ingress controller needs to be installed on the k8 cluster you can deploy this using helm or yaml manifest once deploy devops would create ingress yml resource for k8 services this ingress controller will watch for ingress resource and it will provide you the path based routing. as a just we need to create ingress resource as well as deploy ingress controller to deploy we need to go to there official website and there they will tell how can we install ingress controller on our cluster. it is upto organization which ingress controller needs to be used. 

Ingress is powerful because you can route multiple backend services with a single Ip address and do path based routing, host based routing, TLS terminatation

Ingress controller : Evaluate all the rules defined in you cluster, manages redirection, entrypoint to cluster to the domain subdomain that we have defined in Ingress.yml 
note: you can create one ingress and handle 100's of services using paths if path is A go to service 1 if path is B go to service 2

TLS
Ingress annotations
URL rewrites



configmap: it resolve storing the data which can we used in later point of time in your pod(non sensitive data). whenever the resource is created it will be stored in etcd if hacker hack etcd he can hack the entire DB so if this there s no proper security to resolve this problem K8 came with the concept called secrets.

secrets: sensitive datas are stored. if you create a kind as secret k8 would encrypt before saving in etcd k8 will give default encryption but even we can create our own custom encryption also
9, 10,13,14,18,23
<img width="939" height="577" alt="image" src="https://github.com/user-attachments/assets/feaa00b4-06ed-4cb4-a8f9-c248dc51fd95" />


RBAC:user management and managing the access of service account

service accounts/users
roles or cluster roles
role binding or cluster role binding

Custom resource defenation

my understanding: OOTB there are few resources available in k8 if you need your own resource or extend the your API or you need to have custom resource like argo cd, Istio or others
you can extend the API or add new API to kuberenetes using this you can ask your customers to use required resources 
to extent we have 3 components 1. Custom Resource Defination 2. Custom Resource 3. Custom controller
1. Custom Resource Defination : K8 is saying you Istio or Argo cd to define new type of API to k8. 
how are you using??---> custom resource definition(CRD template) here you define in a yml file(like a template), it as all the options that they support and this you need to submit is custom resource(CR) 
2. custom resource - its a yml file users writes here and its validated with CRD
3. Custom controller - this controller should be deployed in K8 cluster controller will watch for the CR and acts accordingly - logic behind the controller - Watches for events on your CR using Informer or client-go. Reconciles desired vs. current state. Creates, updates, or deletes Kubernetes resources based on CRD spec.





 
