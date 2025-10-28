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
3. when an Instance is created does It have both public and private ip
5. what is permission boundary in IAM
6. transfer bucket from one account to another how can we achieve
7. what is the default route in your route table
8. how would you diff which is public and which is private instance 
9. Can we assign public ip of our choice and private ip of our choice
We can assign a private IP of our choice as long as it’s within the subnet’s CIDR range and not in use.
For public IPs, we can’t choose arbitrary ones — AWS provides them. However, we can allocate and associate an Elastic IP, which gives us control over a static public IP address.
10. I have s3 bucket I need to transfer data from acoont A to account B how would you do this
11. what is trust relationship in IAM
A trust relationship in IAM is a role’s policy that specifies which principals (users, roles, or services) are allowed to assume the role.
It defines “who can use the role,” while the role’s permission policy defines “what the role can do.”
For example, an EC2 instance role has a trust relationship with ec2.amazonaws.com, allowing EC2 to assume it.
12. I have given s3 full access in my policy but in permission boundry i have given read only access what happens
When a user has an IAM policy granting full S3 access but a permission boundary granting only read-only access, the effective permissions are limited to read-only.
This is because permission boundaries define the maximum allowed permissions, and AWS evaluates the intersection of the IAM policy and the boundary.
13. Types of Autoscaling policies
14. there is a scheduled auto scaling policy 10 am 3 servers 6pm 1 server also target policy is set CPU> 70 increase the instance one day at 5.30 cpu is more then 70 percen what will happenn
At 5:30 PM, since CPU > 70%, the target tracking policy will launch additional instances to reduce CPU.
At 6:00 PM, the scheduled scaling policy runs and sets the desired capacity to 1 instance, overriding the target tracking scale-out.
After 6 PM, if CPU spikes again, the target tracking policy may scale out again dynamically.
15. pod affinity and pod anti affinity
16. service and types of service
17. troubleshoot target group unhealthy scenario
If targets in an AWS Target Group are unhealthy, I would troubleshoot by:
a. Checking health check configuration (path, port, protocol, thresholds, timeout).
b.Verifying security groups and network ACLs allow traffic from the ALB/ELB.
c.Ensuring the application is running and responding correctly on the expected port.
d.Confirming targets are properly registered in the target group.
e.Reviewing CloudWatch metrics and ALB access logs for errors.
f.Testing the health check endpoint manually to verify connectivity and response.
18. connect the ec2 instance with the help of terrform and execute some script how will you do
19. what is muteable and inmutable in Docker 
In Docker, images are immutable, meaning their layers cannot be changed after creation. This ensures consistency and reproducibility. Containers are mutable, meaning you can modify files, install software, or change configs while the container is running. Any changes in the container do not affect the original image unless a new image is committed.
20. ADD and COPY diff
21. Major challenges you faced while devops engineer what you have learned out of this
-------------------------
1. why we get 403 error in k8 in pods-
Excellent question 💡 — a **403 Forbidden error in Kubernetes pods** usually means:

> The pod or the service account it’s using **does not have permission** to access the requested Kubernetes API or external resource.

Let’s go step by step 👇

---

## 🚨 **Meaning of 403 in Kubernetes**

`403 Forbidden` → Authentication succeeded ✅ but **authorization failed** ❌.

That means:

* The **API request reached the API server**,
* But the **user, service account, or pod doesn’t have enough RBAC permissions**.

---

## 🔹 **Common Reasons for 403 Error in Pods**

### 1️⃣ **RBAC (Role-Based Access Control) Misconfiguration**

Your pod’s **service account** might not have the correct role or role binding.

🧩 **Example:**
Pod tries to list ConfigMaps:

```bash
kubectl get configmaps
```

But the service account doesn’t have permission → returns **403 Forbidden**.

✅ **Fix:**

* Check the pod’s service account:

  ```bash
  kubectl get pod <pod-name> -o jsonpath='{.spec.serviceAccountName}'
  ```
* Then check its permissions:

  ```bash
  kubectl describe rolebinding,clusterrolebinding | grep <service-account>
  ```
* Create/attach a Role or ClusterRole:

  ```yaml
  kind: RoleBinding
  apiVersion: rbac.authorization.k8s.io/v1
  metadata:
    name: read-configmaps
    namespace: default
  subjects:
  - kind: ServiceAccount
    name: my-service-account
    namespace: default
  roleRef:
    kind: Role
    name: configmap-reader
    apiGroup: rbac.authorization.k8s.io
  ```

---

### 2️⃣ **Service Account Missing**

If your pod runs without a proper service account, it uses the **default service account**, which has limited (almost no) permissions.

✅ **Fix:**
Assign the correct service account in your deployment:

```yaml
spec:
  serviceAccountName: my-app-sa
```

---

### 3️⃣ **Accessing Kubernetes API Without Token**

If your app or pod makes calls to the Kubernetes API and doesn’t include the **Bearer token**, it will get `403 Forbidden`.

✅ **Fix:**
Include service account token automatically mounted in:

```
/var/run/secrets/kubernetes.io/serviceaccount/token
```

Use it in your API calls:

```bash
curl -sSk -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
  https://kubernetes.default.svc/api/v1/pods
```

---

### 4️⃣ **Network Policies or Admission Controllers**

Sometimes a network policy or validating webhook blocks traffic → looks like a 403.

✅ **Fix:**
Check network policy for namespace:

```bash
kubectl get networkpolicy -A
```

---

### 5️⃣ **External API Call (Outside Cluster)**

If your pod calls an **external service (like S3, API Gateway, or REST API)**, a 403 could also mean:

* Wrong IAM role / missing permissions
* Invalid authentication headers
* IP restriction at target API

✅ **Fix:**
If using IRSA (IAM Roles for Service Accounts), ensure correct role is attached.

---

## 🧠 **Quick Summary**

| Cause                 | Meaning                          | Fix                       |
| --------------------- | -------------------------------- | ------------------------- |
| RBAC missing          | Service account lacks permission | Create Role & RoleBinding |
| Wrong service account | Using default SA                 | Assign correct SA         |
| Missing token         | API call not authenticated       | Use service account token |
| Network Policy        | Blocked by cluster rules         | Allow traffic             |
| External API          | IAM or auth issue                | Update permissions        |

---

💬 **In Interview:**

> “A 403 error in a Kubernetes pod typically means the service account lacks proper RBAC permissions. I’d check the pod’s service account, verify its Role/ClusterRole bindings, and ensure any API calls include the right authentication token or IAM role.”

---


   
