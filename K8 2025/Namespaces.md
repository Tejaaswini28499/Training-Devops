In **Kubernetes (K8s)**, a **namespace** is a way to divide cluster resources between multiple users, teams, or applications.

👉 Think of it like **separate folders in the same cluster** — each namespace provides isolation for resources (like Pods, Services, ConfigMaps, Secrets, etc.) so that they don’t clash with each other.

### Key Points:

* **Default namespace**: If you don’t specify, Kubernetes uses the `default` namespace.
* **Other built-in namespaces**:

  * `kube-system` → for system components (like kube-dns).
  * `kube-public` → public info (readable by all).
  * `kube-node-lease` → for node heartbeat tracking.
* **Custom namespaces**: You can create your own for dev, staging, prod, etc.

### Use Cases:

* Organizing resources by **environment** (e.g., dev, test, prod).
* **Multi-tenancy** → Different teams/projects share the same cluster but stay isolated.
* Applying **RBAC policies** at namespace level.
* Limiting resource usage (via **ResourceQuotas** and **LimitRanges**).

### Example: Creating a namespace

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dev
```

### Checking namespaces:

```bash
kubectl get namespaces
```

### Deploying into a specific namespace:

```bash
kubectl apply -f app.yaml -n dev
```

---

⚡ In short: A namespace is a **logical partition inside a Kubernetes cluster** that helps organize and isolate workloads.

Do you want me to also give you **common namespace-related interview questions**?
