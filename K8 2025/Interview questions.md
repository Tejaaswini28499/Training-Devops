https://www.youtube.com/watch?v=Axplgxm4K3U - toughtest interview questions Abhishek

Perfect 👌 — since you already have **5 years of DevOps experience**, interviewers will expect **mid-senior level** Kubernetes (K8s) knowledge.
So we’ll cover:
✅ **Core concepts questions**
✅ **Real-world scenario-based questions**
✅ **Troubleshooting & debugging questions**
✅ **Advanced cluster administration & CI/CD integration**

---

## 🌟 **Kubernetes Interview Questions (5 Years Experience)**

### 🧩 **Core Concepts**

1. **What is a Pod in Kubernetes?**

   * Smallest deployable unit in K8s, one or more containers that share the same network namespace and storage.

2. **What’s the difference between ReplicaSet and Deployment?**

   * ReplicaSet ensures pod replicas; Deployment manages ReplicaSets (versioning, rollout, rollback).

3. **Explain the difference between StatefulSet and Deployment.**

   * StatefulSet maintains pod identity and stable storage (used for DBs).
   * Deployment is stateless (for web servers, APIs).

4. **What is the role of etcd in Kubernetes?**

   * Key-value store for all cluster state and configuration.

5. **What is the role of kube-scheduler?**

   * Decides on which node a pod should be scheduled based on resource requests, taints, affinity rules, etc.

6. **What is a Service in Kubernetes?**

   * An abstraction to expose pods as a network service.
     Types: ClusterIP, NodePort, LoadBalancer, ExternalName.

7. **Explain Persistent Volume (PV) and Persistent Volume Claim (PVC).**

   * PV: Actual storage provisioned in cluster.
   * PVC: Request for that storage by users/pods.

8. **Difference between ConfigMap and Secret.**

   * Both store configuration, but Secret is base64 encoded and used for sensitive data (passwords, tokens).

9. **Explain Namespaces in Kubernetes.**

   * Used to logically divide the cluster for isolation between teams or environments.

10. **Explain the Control Plane components.**

    * kube-apiserver, etcd, kube-controller-manager, kube-scheduler, cloud-controller-manager.

---

## ⚙️ **Scenario-Based Questions**

### **1️⃣ Pod CrashLoopBackOff**

**Scenario:** A pod is stuck in `CrashLoopBackOff`. What will you do?

**Answer:**

1. Check pod logs → `kubectl logs <pod> -p`
2. Describe pod → `kubectl describe pod <pod>`
3. Verify liveness/readiness probes misconfiguration.
4. Check image version, env variables, config files.
5. Verify if PVC or secrets are correctly mounted.

---

### **2️⃣ Node NotReady**

**Scenario:** One node is showing `NotReady`. How will you handle?

**Answer:**

1. Check node status → `kubectl describe node <node-name>`
2. Verify kubelet service → `systemctl status kubelet`
3. Check disk/memory pressure → `kubectl get nodes -o wide`
4. Review logs → `journalctl -u kubelet`
5. If cloud-managed (EKS/GKE/AKS) → check underlying VM health.

---

### **3️⃣ Pod not scheduled**

**Scenario:** Your Deployment is stuck in `Pending` state.

**Answer:**

1. Check resource availability → `kubectl describe pod <pod>`
2. Review node taints and tolerations.
3. Verify affinity/anti-affinity rules.
4. Check PVC binding status.
5. Check scheduler logs if self-managed cluster.

---

### **4️⃣ Deployment Rollout Failed**

**Scenario:** You deployed a new version and rollout failed.

**Answer:**

1. Check rollout status → `kubectl rollout status deploy/<name>`
2. View old/new ReplicaSets → `kubectl get rs`
3. Describe new pods for errors.
4. Rollback if needed → `kubectl rollout undo deploy/<name>`

---

### **5️⃣ High CPU Usage**

**Scenario:** Pods are being evicted due to resource pressure.

**Answer:**

1. Check resource requests/limits.
2. Describe pods for eviction message.
3. Scale replicas or nodes if required.
4. Use HPA (HorizontalPodAutoscaler) to auto-scale.
5. Monitor via `kubectl top pods/nodes`.

---

### **6️⃣ Debugging Networking Issue**

**Scenario:** A service is not reachable from another namespace.

**Answer:**

1. Check service endpoints → `kubectl get ep <svc>`
2. Ensure DNS is working → `kubectl exec -it <pod> -- nslookup <svc>.<ns>.svc.cluster.local`
3. Verify NetworkPolicy blocking traffic.
4. Check service type (ClusterIP vs NodePort).
5. If CNI issue → check CNI logs (Calico/Weave/Cilium).

---

### **7️⃣ Storage Issue**

**Scenario:** PVC is not getting bound to PV.

**Answer:**

1. `kubectl describe pvc <name>` → check reason.
2. Ensure `storageClassName` matches PV.
3. Verify dynamic provisioning or manually created PVs.

---

### **8️⃣ Multi-environment Deployment**

**Scenario:** You have dev, test, prod in the same cluster. How do you isolate?

**Answer:**

* Use **Namespaces**.
* Apply **ResourceQuotas**, **NetworkPolicies**, and **RBAC**.
* Maintain separate ConfigMaps and Secrets per environment.

---

## 🔍 **Troubleshooting Focused**

| Problem              | Key Command                                             | Explanation                   |
| -------------------- | ------------------------------------------------------- | ----------------------------- |
| Pod not starting     | `kubectl describe pod <pod>`                            | Check events & reasons.       |
| Check container logs | `kubectl logs <pod> [-c container]`                     | See application logs.         |
| Debug inside pod     | `kubectl exec -it <pod> -- /bin/sh`                     | Access container shell.       |
| Get cluster info     | `kubectl cluster-info`                                  | Verify API server connection. |
| Debug DNS            | `kubectl exec -it <pod> -- nslookup kubernetes.default` | Verify DNS resolver.          |

---

## 🧠 **Advanced / Architecture / CI-CD Questions**

1. How do you handle **secrets** in Jenkins pipelines deployed to K8s?

   * Store in Vault or Jenkins credentials; inject via environment variables or Kubernetes Secrets.

2. How do you **roll out zero-downtime deployments**?

   * Use RollingUpdate strategy in Deployment, set `maxUnavailable: 0` and `maxSurge: 1`.

3. How do you perform **blue-green deployments** in Kubernetes?

   * Create separate deployments (`blue`, `green`) and switch service selector.

4. How do you **integrate monitoring** in Kubernetes?

   * Use Prometheus + Grafana, or cloud-native tools (CloudWatch, Azure Monitor).

5. What’s the difference between **Ingress** and **Service of type LoadBalancer**?

   * LoadBalancer exposes one service externally.
   * Ingress manages multiple routes/domains via one load balancer.

6. How do you manage **secrets in GitOps or CI/CD pipelines**?

   * Use sealed-secrets, Vault, or external secret managers.

7. What is the use of **Pod Disruption Budget (PDB)?**

   * Ensures minimum replicas are always running during voluntary disruptions.

8. Explain **taints and tolerations**.

   * Taints prevent pods from scheduling on a node unless tolerated (used for node isolation).

9. How do you **upgrade a cluster** safely?

   * Drain nodes, upgrade control plane first, then worker nodes; validate workloads post-upgrade.

10. How to handle **node autoscaling** in EKS/GKE?

* Use Cluster Autoscaler to scale worker nodes based on pending pods.

---

## 🧪 **Hands-on / Practical Questions**

* Deploy an NGINX pod and expose it as a service.
* Create a ConfigMap and mount it to a pod.
* Create a pod that uses a Secret for DB credentials.
* Set up a Horizontal Pod Autoscaler for a deployment.
* Write a NetworkPolicy to allow traffic only from a specific namespace.

---

Would you like me to create a **PDF “Kubernetes Interview Prep Guide (5 Years Experience)”** — with questions + sample answers + command references + diagrams?
I can make it structured for **quick revision before interviews.**
