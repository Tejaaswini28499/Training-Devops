1. consider e-commernce appln that will be accessible throughout the world its international appln requriment is it should be highly scalable robust and it should be highly available ypu are free to use all AWS resouces
2. why use monolathic over microservices
3. In case of observeability how would you monitor your entire ecosystem or entire appln
4. Secure appln and cloud infra what are the best measures you take- DDOS attack so we need to implement AWS Sheild can can also implement AWS FAF(expalin in detail)
5. customer is cost-sensitive as we are using lots of AWS services so what cost optimization measures you will take that doesnt affect
6. How would you connect on-premisis data to E-commerace appln which is in cloud using AWS -> VPC endpoints, VPC VPN side to side connectivitiy over Internet and private, direct connect(physical cables) connect on-prime to AWS very faster and more money and safer (lots of data better to have)
7. What is statefulset how it is different from Deployment
8. Multistage docker file
9. troublestooting - Cashloop backoff, Imagepullbackoff
10. what kind of logging used to monitor the pods
11. What is Gitops and Argo CD how it is different from traditional pipelines
12. Deployment Stategies
13. consider you have deployed the application ok EKS and it needs the access to S3 dynamodb how would you provide
14. If you have to develop an appln and deploy an appln across the k8 cluster how would you do -> helm
15. Consider multiaccount structure in an organasation there is already a setup but we need to create infrastruce and we have to deploy and appln in all these accounts what would be your ideal way to manage this entire ecosystem in terraform
16. what benefits you get when you create a custom modules in terrform and why do you create
17. have you ever worked on dynamic block if yes what is use of that and why is used
18. how would you create near perfect devsecops pipeline from init to deploy

----------------------------------
1. think 5 replica 3 is up 2 is down what may be the reason
2. can I have the encode base 64 password and store in my configmap inside of secret?
3. how do you pass output of one module to another in terraform
4. diff btw contionus delivery and continoud deployment
5. explain cloud watch alaram and cloud watch event
6. without internet how would you connect to s3
7. diff scaling groug in asg
8. cooldown period in ASG
9. can you can the private Ip address of running ec2 or once you stop can it be changed
10. if you want to assign the permanent ip address to ec2 how would you do it
11. I have to provision two infra primary and secondary in jenkins pipeline how would you ensure the secondary runs only after the primary runs
12. how would you cleanup the tempoarary file in jenkins workspace 
--------------------------------------------
1. how do you fix isssue when there is a error in production -> hotfix
2. monday to friday from 9am server will be 8 and at 6pm it will be 2 one day at 5.30 suddendly the CPU spikes and it will hit 10 servers at 6pm what will happend 
“If there’s a CPU spike at 5:30 PM, the Auto Scaling Group will detect the high load and automatically launch more instances — say, up to 10 — to handle the traffic. However, since a scheduled action is set to reduce servers to 2 at 6 PM, it will still trigger and terminate 8 instances. This can cause performance issues or dropped requests if traffic is still high. To avoid this, we should use dynamic or predictive scaling instead of fixed schedules, add connection draining, and set safe minimum instance limits to prevent sudden scale-in during peak load.”
3. how the request will flow from browser to pod where your appln is running
“When a user sends a request from the browser, it first goes to the DNS to resolve the domain name into the external IP of the Load Balancer or Ingress. The request reaches the Load Balancer, which forwards it to the Kubernetes Service (usually a ClusterIP or NodePort). The Service uses kube-proxy and iptables/ipvs rules to route the request to one of the healthy pods behind it. Inside the pod, the containerized application processes the request and sends the response back the same path through the Service, Load Balancer, and finally to the browser.”
4. How do you troubleshoot unhealthy target groups in k8
“When a target group shows unhealthy targets in Kubernetes, I first check if the pods are running and ready using kubectl get pods. Then I verify the readiness and liveness probes — misconfigured probes often cause health check failures. Next, I check if the Service and Ingress correctly map to the target port and pod labels. I also review the ALB or NLB health check settings (path, port, timeout) to ensure they match the app. Finally, I check logs in the pod (kubectl logs) and events (kubectl describe pod) to identify application or networking issues.”
5. can I delete the image out of which my container is running
6. I need to store certificate related information which to use configmap, secret or AWS secret manager
7. How would you rotate your secret id associated with AWS secret Manager or Vault
8. how do you use for each block in terrform
-----------------------------------------------------

1. Have you written any modules in terraform
2. public ip has been assiged to my instace can i chane that into private
3. what is permission boundary in IAM
4. transfer bucket from one account to another how can we achieve
5. what is the default route in your route table
