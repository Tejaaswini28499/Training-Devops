Good question 👏 — this is a **core Kubernetes concept** that often comes up in interviews.

Here’s the simple explanation 👇

---

### 🧠 **Reason: Master node is reserved for control plane components**

The **master node** (or **control plane node**) runs critical system components like:

* `kube-apiserver`
* `kube-controller-manager`
* `kube-scheduler`
* `etcd`

These processes manage the entire cluster.
If you schedule application pods on the master node, they could:

* Consume CPU/memory meant for control plane processes.
* Cause instability or even cluster failure if resources are exhausted.

So, **Kubernetes by default “taints” the master node** to **prevent regular pods** from being scheduled on it.

---

### ⚙️ **The Default Taint**

When a cluster is created, the master node has this taint:

```bash
kubectl describe node <master-node-name> | grep Taint
```

You’ll see something like:

```
Taints: node-role.kubernetes.io/control-plane:NoSchedule
```

or in older versions:

```
Taints: node-role.kubernetes.io/master:NoSchedule
```

This means:

> “Don’t schedule any pod on this node unless it tolerates this taint.”

---

### ✅ **If you *want* to schedule pods on master**

You can **remove the taint** (not recommended for production):

```bash
kubectl taint nodes <master-node-name> node-role.kubernetes.io/control-plane:NoSchedule-
```

Or, **add a toleration** in your Pod manifest:

```yaml
tolerations:
- key: "node-role.kubernetes.io/control-plane"
  effect: "NoSchedule"
```

---

### 🚫 **In summary**

| Reason              | Explanation                                                       |
| ------------------- | ----------------------------------------------------------------- |
| Resource Protection | Master node runs cluster-critical components                      |
| Default Taint       | Prevents accidental app pods from being scheduled                 |
| Stability           | Avoids overload or crash of control plane                         |
| Override (optional) | Remove taint or add toleration (only for test/single-node setups) |

---

Would you like me to show a **real example YAML** where a pod is made to run on a master node by adding toleration + nodeSelector?
