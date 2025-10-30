In Kubernetes (**K8s**), **Ingress** is an API object that manages **external access to services** inside the cluster, typically **HTTP and HTTPS traffic**.

👉 Think of it as a **smart router** that sits at the edge of your Kubernetes cluster and decides how requests from outside (users, browsers, APIs) get routed to your internal services (Pods).

---

### 🔹 Why Ingress?

* By default, services in Kubernetes are only accessible **inside the cluster**.
* If you want them to be accessed externally, you usually expose them using:

  * **NodePort** → Opens a port on every node.
  * **LoadBalancer** → Creates a cloud load balancer.
* But if you have many services, managing multiple LoadBalancers/NodePorts becomes messy.
  **Ingress solves this problem** by providing a central entry point.

---

### 🔹 Ingress Components

1. **Ingress Resource**

   * A YAML configuration that defines routing rules (hostnames, paths, TLS, etc.).

2. **Ingress Controller**

   * The actual implementation (software) that reads the Ingress rules and does the routing.
   * Examples: **NGINX Ingress Controller, HAProxy, Traefik, AWS ALB Ingress Controller, GCP Load Balancer Controller.**

---

### 🔹 Features of Ingress

* Route traffic based on **hostnames** (e.g., `app.example.com`).
* Route traffic based on **paths** (e.g., `/api`, `/shop`).
* Supports **SSL/TLS termination** (HTTPS).
* Can provide **load balancing**, **redirects**, and **rewrites**.
* Centralized traffic management instead of multiple LoadBalancers.

---

### 🔹 Example Ingress YAML

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /shop
        pathType: Prefix
        backend:
          service:
            name: shop-service
            port:
              number: 80
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80
```

➡️ Here:

* Traffic to **`myapp.example.com/shop`** goes to **shop-service**.
* Traffic to **`myapp.example.com/api`** goes to **api-service**.

---

### 🔹 Analogy

Imagine you have a **mall (K8s cluster)** with multiple **shops (services)**:

* Without Ingress → Every shop has its own door facing outside (LoadBalancer for each).
* With Ingress → The mall has **one main entrance (Ingress Controller)**, and a **reception desk (Ingress rules)** directs you to the correct shop.

---

Do you want me to also explain **Ingress vs Service** (NodePort, ClusterIP, LoadBalancer) with a comparison table?



Nice one 👍 — for **4 years of Kubernetes experience**, interviewers usually expect you to go beyond “what is Ingress” and demonstrate **hands-on experience**, **troubleshooting skills**, and **production use cases**.

Here’s a tailored set of **Ingress interview questions** (beyond basics), suitable for someone with 4 years in K8s:

---

## 🔹 **Intermediate-Level Ingress Questions**

1. How does Ingress differ from LoadBalancer and NodePort?
2. Explain host-based vs path-based routing with examples.
3. How do you configure TLS/HTTPS in Ingress?
Create a TLS Secret with your certificate and key:
Reference the Secret in your Ingress YAML:
The Ingress Controller (e.g., NGINX) terminates HTTPS using the certificate in the secret.
5. What are some common NGINX Ingress annotations you have used?

* `nginx.ingress.kubernetes.io/rewrite-target` → rewrites request paths
* `nginx.ingress.kubernetes.io/ssl-redirect` → forces HTTPS
* `nginx.ingress.kubernetes.io/proxy-body-size` → limits upload size
* `nginx.ingress.kubernetes.io/proxy-read-timeout` → sets backend timeout

5. How do you implement HTTP → HTTPS redirection in Ingress?-> annotations and tls section of ingress
6. Can multiple services use port 80 behind the same Ingress? Why is it not a conflict?
7. How do you handle URL rewrites in Ingress (e.g., `/shop` → `/`)?

---

## 🔹 **Advanced Ingress Questions**

8. What are some challenges you faced while configuring Ingress in production? How did you fix them?
9. What’s the difference between **Ingress resource** and **Ingress Controller**? Can you have multiple Ingress controllers in one cluster?
10. How does Ingress work with external DNS? (e.g., cert-manager + external-dns setup)
11. How do you secure Ingress with authentication and IP whitelisting?
nginx.ingress.kubernetes.io/auth-type: basic
nginx.ingress.kubernetes.io/auth-secret: basic-auth
nginx.ingress.kubernetes.io/auth-realm: "Authentication Required"

nginx.ingress.kubernetes.io/whitelist-source-range: "10.0.0.0/24,192.168.1.0/24"
Allow access only from specific IP ranges
✅ Only clients from these IPs can reach the service; others are blocked with 403 Forbidden

12. Have you implemented **rate limiting, WAF, or ModSecurity** with Ingress? How?
13. How do you troubleshoot when an Ingress route is not working? Walk through your debugging steps.
14. Can Ingress handle TCP/UDP traffic? If yes, how?
15. What happens if two Ingress resources define conflicting rules for the same host/path?

---

## 🔹 **Scenario-Based Ingress Questions**

16. You have 10 microservices. How would you expose them externally with one Ingress?
17. How do you configure Ingress for multi-tenant apps where each tenant has its own subdomain?
18. Suppose your company wants to enable HTTPS for all services with **Let’s Encrypt** — how would you automate it?
19. How would you set up canary deployments or A/B testing using Ingress?
20. Imagine your Ingress is working, but users complain of **high latency** — how would you debug and optimize?

---

## 🔹 **Very Advanced / Senior-Level Questions (for 4+ years)**

21. How does the NGINX Ingress Controller translate Ingress rules into NGINX config?
22. What is the **Kubernetes Gateway API**, and how does it compare with Ingress?
23. In production, would you use a **cloud-native Ingress controller (AWS ALB/GCP LB)** or **NGINX/Traefik**? Why?
24. How do you manage **Ingress in multi-cluster or hybrid-cloud environments**?
25. Explain how you integrated Ingress with a Service Mesh (Istio/Linkerd).

---
Get ans for above
---
different

# ✅ **Kubernetes Ingress Interview Q\&A**

---

## 🔹 **Basic Questions**

**1. What is an Ingress in Kubernetes?**
👉 Ingress is a Kubernetes API object that manages external access (HTTP/HTTPS) to services in a cluster. It provides routing rules to expose multiple services via a single entry point.

---

**2. Why do we need Ingress when we already have NodePort and LoadBalancer services?**
👉

* **NodePort** → Exposes each service on a node’s IP & port → limited, hard to manage.
* **LoadBalancer** → Creates one load balancer per service → costly.
* **Ingress** → Single entry point + smart routing + TLS support → efficient & scalable.

---

**3. What are the main components of Ingress?**
👉

* **Ingress Resource** → YAML object with routing rules.
* **Ingress Controller** → Actual implementation that processes those rules (NGINX, Traefik, ALB, etc.).

---

**4. How do you expose an application using Ingress?**
👉 Steps:

1. Create **Deployment + Service (ClusterIP)**.
2. Deploy an **Ingress Controller**.
3. Create an **Ingress resource** with rules.
4. Access via hostname/path.

---

**5. Can multiple Services use the same port (e.g., 80) behind an Ingress? Why?**
👉 Yes. Each Service has its **own cluster IP**. Ingress routes to `ServiceIP:port`. Since IPs differ, no conflict.

---

## 🔹 **Intermediate Questions**

**6. How does Ingress handle routing based on hostnames vs paths?**
👉

* **Hostname-based**: `shop.example.com` → shop-service.
* **Path-based**: `example.com/api` → api-service.

---

**7. Explain how TLS/HTTPS is configured in Ingress.**
👉 You create a **Kubernetes Secret** with the TLS certificate and key, then reference it in the Ingress spec under `tls:`. The controller terminates SSL.

---

**8. What are common annotations used in Ingress (NGINX)?**
👉 Examples:

* `nginx.ingress.kubernetes.io/rewrite-target` → path rewrites.
* `nginx.ingress.kubernetes.io/ssl-redirect` → force HTTPS.
* `nginx.ingress.kubernetes.io/whitelist-source-range` → IP restrictions.

---

**9. What is the difference between ClusterIP, NodePort, LoadBalancer, and Ingress?**
👉

* **ClusterIP** → Internal-only access.
* **NodePort** → Exposes service on every node’s IP\:port.
* **LoadBalancer** → Exposes service externally with a cloud LB.
* **Ingress** → Smart routing, one entry point for many services.

---

**10. Can Ingress work without an Ingress Controller? Why or why not?**
👉 No. The Ingress resource is just rules; without a controller, nothing actually routes the traffic.

---

**11. How do you redirect HTTP to HTTPS using Ingress?**
👉 Use annotation:
`nginx.ingress.kubernetes.io/ssl-redirect: "true"` or configure a TLS block in Ingress.

---

**12. How would you configure URL rewrites (e.g., `/shop` → `/` in the backend)?**
👉 With annotation:

```yaml
nginx.ingress.kubernetes.io/rewrite-target: /
```

---

## 🔹 **Advanced Questions**

**13. What are some Ingress Controllers you have used, and how do they differ?**
👉

* **NGINX** → Most common, flexible, community-driven.
* **Traefik** → Lightweight, good for dynamic routing.
* **AWS ALB** → Integrates with AWS Load Balancer.
* **HAProxy** → High performance, enterprise features.

---

**14. How do you handle authentication/authorization in Ingress?**
👉 Using annotations or sidecar:

* Basic auth via `nginx.ingress.kubernetes.io/auth-type`.
* OIDC with external plugins.
* External auth provider (e.g., Keycloak, OAuth2 proxy).

---

**15. How does Ingress support rate limiting, IP whitelisting, or WAF?**
👉 Ingress Controller provides annotations for these (NGINX has built-in rate limiting, whitelisting, and can integrate with ModSecurity WAF).

---

**16. What happens when you have conflicting Ingress rules?**
👉 The controller resolves conflicts:

* **Most specific rule wins** (e.g., `/shop/details` overrides `/shop`).
* Otherwise, rule order is controller-specific.

---

**17. How does Ingress integrate with external DNS providers?**
👉 DNS resolves the domain (e.g., `app.example.com`) to the external IP of the Ingress Controller LoadBalancer. Tools like **external-dns** can automate DNS record updates.

---

**18. How do you troubleshoot if an Ingress route is not working?**
👉 Steps:

1. Check Ingress resource with `kubectl describe ingress`.
2. Ensure DNS points to Ingress controller’s external IP.
3. Verify Service is healthy (`kubectl get svc`).
4. Check Ingress Controller logs (`kubectl logs`).

---

**19. What’s the difference between Ingress and a Service Mesh Gateway (Istio)?**
👉

* **Ingress** → Basic HTTP routing, TLS, path-based rules.
* **Service Mesh Gateway** → Advanced L7 features (mTLS, retries, circuit breaking, observability).

---

**20. Can Ingress handle non-HTTP protocols (like TCP/UDP)?**
👉 By default, Ingress is for HTTP/HTTPS. Some controllers (like NGINX, Traefik) allow TCP/UDP forwarding via custom configuration, but it’s not standard.

---

## 🔹 **Scenario-Based Questions**

**21. Suppose you have 10 microservices — how would you expose them using Ingress without creating 10 LoadBalancers?**
👉 Create one Ingress Controller + one Ingress resource with multiple rules mapping paths/hosts → services. Single external IP.

---

**22. Your team wants to enable HTTPS for multiple apps using a single TLS certificate. How would you configure Ingress?**
👉 Use a **wildcard certificate** (`*.example.com`) or multi-SAN certificate in a TLS secret. Reference it in Ingress `tls:` section.

---

**23. Your API needs versioning (`/v1`, `/v2`). How would you route this via Ingress?**
👉 Ingress rules with path prefixes:

* `/v1` → `api-v1-service`
* `/v2` → `api-v2-service`

---

**24. How do you deploy and configure an NGINX Ingress Controller in a cluster?**
👉

* Apply official NGINX Ingress Controller manifest or Helm chart.
* It creates a DaemonSet/Deployment + Service (LoadBalancer).
* Then create Ingress resources.

---

**25. You deployed an Ingress, but it’s not routing traffic correctly. What steps will you take to debug?**
👉

1. Check DNS points to LB IP.
2. Check Ingress resource (`kubectl get ingress -o yaml`).
3. Ensure service selectors match pods.
4. Look at Ingress Controller logs.
5. Curl service internally (`kubectl exec -it pod -- curl service:port`).

---

✅ That covers **all 25 questions with concise answers**.

Would you like me to also prepare a **cheat sheet diagram** (Ingress vs Service vs LoadBalancer) so you can explain visually in interviews?

My understanding:

what is sticky session in kubernetes : 

what are enterprise loadbalancer support? - exposing one specific ip address 

 Ingress is powerful because you can route multiple backend services with a single Ip address and do path based routing, host based routing, TLS terminatation

 Ingress controller : Evaluate all the rules defined in you cluster, manages redirection, entrypoint to cluster to the domain subdomain that we have defined in Ingress.yml 

why Ingress ??
enterprise and TLS load balancing capabalities 
service of type lb the cloud provider will charge for static public ip address as each and every lb was creating static public ip

service in k8 was doing very simple loadbalanicing but enterprise loadbalancer support was giving very good feature which k8 was not providing

exposes using loadbalancer mode in service in cloud was charging more as it was static public IP address as each and every lb having public ip 


what is Ingress?? - its just lb sometimes lb + API gateway
will allow k8 users to use lb, user will create resource called Ingress in k8 it will tell lb providers to create something called Ingress controller 


what if you need path based routing bcz service wont provide as its just have round robbin type of lb
The lb provided Ingress controller needs to be installed on the k8 cluster you can deploy this using helm or yaml manifest once deploy devops would create ingress yml resource for k8 services this ingress controller will watch for ingress resource and it will provide you the path based routing. as a just we need to create ingress resource as well as deploy ingress controller to deploy we need to go to there official website and there they will tell how can we install ingress controller on our cluster. it is upto organization which ingress controller needs to be used. 

note: you can create one ingress and handle 100's of services using paths if path is A go to service 1 if path is B go to service 2
<img width="674" height="385" alt="image" src="https://github.com/user-attachments/assets/538d04c6-2490-44d3-a866-6d2cdc7c2234" />

TLS
<img width="669" height="319" alt="image" src="https://github.com/user-attachments/assets/64bd1469-3927-4ad9-94d1-0768343c403e" />
<img width="669" height="321" alt="image" src="https://github.com/user-attachments/assets/04515399-30b8-46b4-bee5-04bf7be5bbd8" />


Ingress annotations
URL rewrites(learn all 3 topics and others in interview questions)


what is add on in Ingress
Good question 👍

In **Kubernetes Ingress**, an **add-on** usually refers to an **additional component or feature** that extends the **Ingress Controller’s core functionality** — it’s *not* part of the native Kubernetes API but is integrated to provide more advanced capabilities.

Let’s break it down 👇

---

### 🔹 **1. Ingress Controller = Core**

The **Ingress Controller** (like NGINX, Traefik, HAProxy, AWS ALB, etc.) is the engine that interprets Ingress rules and routes HTTP/S traffic.

---

### 🔹 **2. Add-ons = Extra Capabilities**

Add-ons are **optional integrations or plugins** added to Ingress to provide:

| Purpose                            | Common Add-on / Feature                                                          |
| ---------------------------------- | -------------------------------------------------------------------------------- |
| **SSL/TLS automation**             | `cert-manager` → automatically issues and renews TLS certs (e.g. Let’s Encrypt). |
| **External DNS updates**           | `external-dns` → automatically creates/updates DNS records for your hosts.       |
| **Web Application Firewall (WAF)** | `ModSecurity` or OWASP CRS with NGINX Ingress.                                   |
| **Rate limiting / throttling**     | NGINX annotations or custom plugins.                                             |
| **Authentication / SSO**           | OIDC or OAuth2 proxy add-ons.                                                    |
| **Monitoring / Metrics**           | Prometheus exporter or NGINX VTS module.                                         |
| **Rewrite / Redirect support**     | Enabled via ingress annotations (an internal add-on feature).                    |

---

### 🔹 **3. Example Setup**

In a production environment you might have:

* NGINX Ingress Controller
* **Add-on 1:** `cert-manager` for HTTPS
* **Add-on 2:** `external-dns` for DNS automation
* **Add-on 3:** WAF for security

Together, they make your Ingress setup **automated, secure, and production-ready**.

---

### 🔹 **4. Analogy**

Think of the Ingress Controller as a **base smartphone**, and the add-ons are **apps** that add more power — SSL automation, security, monitoring, etc.

---

Would you like me to show a **diagram of a production-grade Ingress setup** with these add-ons (cert-manager, external-dns, WAF)? It’s a great visual for interview explanations.


if we have api service.yml and frondend service.yml how both can be exposed in one ingress
Excellent question 👏 — this is a **very common Kubernetes scenario** in real-world DevOps work!

Let’s break it down clearly 👇

---

## 🧩 Scenario

You have two services:

* **API Service** (`api-service.yml`) — backend microservice
* **Frontend Service** (`frontend-service.yml`) — UI (React/Angular, etc.)

And you want to expose **both under one Ingress** (one domain).

---

## 💡 Goal Example

Let’s say you want this structure:

| URL Path                         | Service  | Port |
| -------------------------------- | -------- | ---- |
| `https://myapp.example.com/`     | Frontend | 80   |
| `https://myapp.example.com/api/` | API      | 8080 |

Both routes are served from the **same domain (Ingress)** but route to **different backend services**.

---

## 🧱 Step 1 — Frontend Service (`frontend-service.yml`)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  selector:
    app: frontend
  ports:
    - port: 80
      targetPort: 80
```

---

## 🧱 Step 2 — API Service (`api-service.yml`)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  selector:
    app: api
  ports:
    - port: 8080
      targetPort: 8080
```

---

## 🧱 Step 3 — Ingress (`ingress.yml`)

Here’s how you expose both via **one Ingress**:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: frontend-service
                port:
                  number: 80
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 8080
```

### 🧠 What Happens:

* Requests to `/` or `/home` or `/about` → go to `frontend-service`.
* Requests to `/api/...` → go to `api-service`.

---

## ⚙️ Step 4 — DNS & Ingress Controller

Make sure:

1. You have an **Ingress Controller** (like **NGINX Ingress Controller**) installed in your cluster.
2. Your domain (`myapp.example.com`) points to the **Ingress Controller’s external IP** (via DNS or `/etc/hosts` for local testing).

---

## 🌍 Optional — With TLS (HTTPS)

If you use HTTPS (recommended):

```yaml
spec:
  tls:
    - hosts:
        - myapp.example.com
      secretName: myapp-tls-secret
```

This enables SSL using a TLS secret (which can be auto-managed with **cert-manager** + Let’s Encrypt).

---

## 🧩 Bonus — Folder-style Example for Clarity

```
k8s/
├── api-deployment.yml
├── api-service.yml
├── frontend-deployment.yml
├── frontend-service.yml
└── ingress.yml
```

All deployed together:

```bash
kubectl apply -f k8s/
```

---

## ✅ Summary

| Purpose            | Component                | Example                      |
| ------------------ | ------------------------ | ---------------------------- |
| Backend service    | `api-service.yml`        | `/api` route                 |
| Frontend service   | `frontend-service.yml`   | `/` route                    |
| Single entry point | `Ingress`                | routes traffic based on path |
| Ingress controller | Required                 | NGINX or Traefik             |
| TLS                | Optional but recommended | cert-manager                 |

---

Would you like me to show a **complete working example** (with both deployments + services + ingress) — ready to deploy on a Minikube or EKS cluster?

can we use same ingress file for 2 different appln
💯 Excellent and **very practical** DevOps question — and the answer is:
👉 **Yes, you *can* use the same Ingress file for multiple applications**, **but** it depends on **how and where** you deploy them.

Let’s break it down with **clear logic, examples, and best practices** 👇

---

## 🧩 What You Mean by “2 Different Applications”

Let’s define two possible cases:

| Case                                                      | Description                                                             |
| --------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Case 1:** Both apps are in the **same namespace**       | Example: `frontend` and `api` deployed together (same team/project)     |
| **Case 2:** Apps are in **different namespaces or teams** | Example: `orders` app and `inventory` app (different teams or projects) |

---

## 🧱 Case 1 — Same Namespace (✅ Common & Recommended)

If both apps are part of one product (e.g. frontend + backend of same web app),
➡️ then **one Ingress file** is perfectly fine.

### ✅ Example

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: frontend-service
                port:
                  number: 80
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 8080
```

✅ Both apps (frontend and backend) share **one domain** (`myapp.example.com`)
✅ Traffic is routed by path rules.
✅ Best for monolithic or tightly-coupled apps.

---

## 🧱 Case 2 — Different Applications (🟡 Possible, but Not Ideal)

If you have **two unrelated applications** like:

* `shop.example.com` → Shop app
* `blog.example.com` → Blog app

You **can still use one Ingress file**, but it becomes large and harder to maintain.

### Example:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multi-app-ingress
spec:
  rules:
    - host: shop.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: shop-service
                port:
                  number: 80
    - host: blog.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: blog-service
                port:
                  number: 80
```

✅ Works fine.
❌ But hard to manage if different teams maintain different apps.
❌ Risk of merge conflicts or misconfigurations.

---

## ⚙️ Alternative — Separate Ingress for Each App (Recommended for Multi-Team)

In larger or enterprise setups:

* Each app has **its own ingress.yml** (clean separation).
* The Ingress Controller handles all of them automatically.
* You can still use the **same hostname or domain** if rules don’t conflict.

### Example:

**frontend-ingress.yml**

```yaml
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            backend:
              service:
                name: frontend-service
                port:
                  number: 80
```

**api-ingress.yml**

```yaml
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /api
            backend:
              service:
                name: api-service
                port:
                  number: 8080
```

Kubernetes will **merge them automatically** inside the Ingress Controller (e.g., NGINX).
✅ Easier to manage per-app changes.
✅ Supports multiple pipelines.
✅ Follows microservice ownership pattern.

---

## 🧠 Summary

| Scenario                            | Can use same Ingress? | Recommended? | Why                                           |
| ----------------------------------- | --------------------- | ------------ | --------------------------------------------- |
| Frontend + API (same app)           | ✅ Yes                 | ✅            | Shared domain & routes                        |
| Different microservices (same team) | ✅ Yes                 | ⚠️ Maybe     | Works, but YAML gets big                      |
| Different teams or projects         | ⚠️ Possible           | ❌ No         | Hard to manage, better separate Ingress files |

---

## 🧩 Bonus Tip

If you use **Helm**, you can template one Ingress file and deploy it **with variables** for each app, like:

```yaml
{{- if .Values.ingress.enabled }}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ .Release.Name }}-ingress
spec:
  rules:
    - host: {{ .Values.ingress.host }}
      http:
        paths:
          - path: {{ .Values.ingress.path }}
            backend:
              service:
                name: {{ .Release.Name }}-service
                port:
                  number: {{ .Values.service.port }}
{{- end }}
```

→ This allows you to reuse one structure cleanly for multiple apps.

---

Would you like me to show the **best practice Ingress setup** (using separate ingress files for frontend & backend but same domain), like how it’s done in real projects (EKS or GKE)?
