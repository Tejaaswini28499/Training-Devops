helm:
Its a package manager for Kubernetes which helps you to install k8 controllers or the third party applications you can install, update uninstall or package appln as helm charts and help others to download and package and use the appln
step 1: add the repo
step 2: Install helm command 
step 3: Once Helm is installed and the repo is added
step 4: Pull the NGINX chart from Bitnami’s repo
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-nginx bitnami/nginx
step 5: Create all required Kubernetes objects (Deployment, Service, etc.)
step 6: Deploy it to your cluster

using helm command we can install Grafana, argocd, Prometheus or third party appln like nginx

why helm??
don't have helm need to create scripts for each k8 controller and for multiple versions of k8 controller team A can use Argo CD 2.12 team B might want to use argo CD 2.13 for this you cannot keep creating multiple yml files 

how to Install helm?
In official document we can see and based on your OS you can Install helm


how does helm get to know on which cluster it needs to apply when it you have multiple clusters
Excellent question 👏 — this is an important concept when you start managing **multiple Kubernetes clusters** using **Helm**.

Let’s break it down clearly 👇

---

### 🧩 1. Helm doesn’t manage clusters directly

Helm **doesn’t connect to clusters by itself**.
It always uses your **current Kubernetes context**, which is configured in your local **`kubectl`** setup.

So basically:

> **Helm = a client on top of kubectl + Kubernetes API.**

Helm simply follows whatever cluster your `kubectl` is pointing to.

---

### ⚙️ 2. The link between Helm and your cluster: `kubeconfig`

Helm reads your **Kubernetes configuration file** (usually `~/.kube/config`).

That file stores:

* Cluster details (API endpoint, certificate)
* User credentials
* Contexts (cluster + user + namespace combinations)

Example:

```yaml
apiVersion: v1
kind: Config
clusters:
- name: dev-cluster
  cluster:
    server: https://dev.example.com
- name: prod-cluster
  cluster:
    server: https://prod.example.com
contexts:
- name: dev
  context:
    cluster: dev-cluster
    user: dev-user
- name: prod
  context:
    cluster: prod-cluster
    user: prod-user
current-context: dev
```

---

### 🧭 3. Helm uses the current context

When you run:

```bash
helm install myapp ./chart
```

Helm internally talks to the Kubernetes API for the **current context** in `kubectl`.

If your current context is `dev`, it will apply to the `dev` cluster.

---

### 🔄 4. Switching between clusters

You can change which cluster Helm uses in two ways:

#### Option 1: Change kubectl context

```bash
kubectl config use-context prod
helm install myapp ./chart
```

Now Helm will install it on the **prod** cluster.

#### Option 2: Use `--kube-context`

You can directly specify which context Helm should use:

```bash
helm install myapp ./chart --kube-context prod
```

---

### 🧠 5. Summary

| What decides the cluster? | How?                                   |
| ------------------------- | -------------------------------------- |
| Default context           | `kubectl config current-context`       |
| Manually set context      | `kubectl config use-context <context>` |
| Per-command override      | `--kube-context <context>`             |

---

### 🧪 Bonus: Check what cluster Helm will use

Run:

```bash
kubectl config current-context
kubectl cluster-info
```

That’s the cluster Helm will connect to by default.

---


note: Bitnami is the repo which contain every component helm charts and this the one which we will be using 
helm search repo bitnami | grep nginx
Install helm(helm install nginxv1 bitnami/nginx) nginxv1- is a release name
check in the default namespace the nginx get deployed (kubectl get pods)

release name - why we need to provide this while installing why chart - its a deployed instance of our chart 

how to install which is not a part of bitnami eg aws load balancer
go to AWS official website from there you can install 

we can also uninstall helm 
helm uninstall nginxv1 - always provide the release name 


How can our appln can be deployed as a helm charts
create a folder 
mkdir -p best-commerce/{payments,shipping}
cd payments 
helm create payments 
within payments helm would create 2 yml and one template file and another chart file for you 
1. chart.yml, 2.vaule.yml, 3.template 4. chart

template - where you will have all deployment, service ingress, PV, PVC, storage (all deployment related files)
vaule.yml - when you have different env like dev, prod, test and you want to pass different values so we need values.yml

after applying the required commands you need to package your application 
helm package shipping - this will be created as a zip file which we call it has chart
package payment also and then run below command
helm repo index .
 
