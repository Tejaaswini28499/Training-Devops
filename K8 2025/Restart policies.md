In Kubernetes, **Restart Policies** define **how the kubelet should handle container restarts** in a Pod when containers fail or exit.
They are always set at the **Pod level** (apply to all containers in that Pod) and are specified in the Pod spec under `spec.restartPolicy`.

---

### ✅ Types of Restart Policies in Kubernetes

Kubernetes supports **3 restart policies**:

1. **Always**

   * Default policy for **Deployments, ReplicaSets, StatefulSets, DaemonSets**.
   * Containers are restarted **no matter why they exit** (failed, completed, or killed).
   * Ensures high availability — the pod keeps running continuously.
   * Example use case: Web servers, API services, long-running apps.

   ```yaml
   restartPolicy: Always
   ```

---

2. **OnFailure**

   * Container is restarted **only if it fails** (i.e., exit code ≠ 0).
   * If the container exits successfully (exit code = 0), it will **not restart**.
   * Typical for **batch jobs** where you want retries on failure.
   * Example use case: Data processing jobs, ETL pipelines.

   ```yaml
   restartPolicy: OnFailure
   ```

---

3. **Never**

   * Container is **never restarted**, regardless of exit status.
   * Pod runs once, then stops.
   * Use case: Debugging, one-off tasks, or Jobs where you want logs from a single run.

   ```yaml
   restartPolicy: Never
   ```

---

### 📌 Relation with Workload Types

* **Pods (directly created):** You can use any of the three policies.
* **Deployments / StatefulSets / DaemonSets:** Always use `Always` (automatically enforced).
* **Jobs:** Default is `OnFailure` (can also be set to `Never`).
* **CronJobs:** Inherit from Job (so `OnFailure` or `Never`).

---

### ⚡ Example Pod Specs with Restart Policy

**Always (default)**:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: always-pod
spec:
  restartPolicy: Always
  containers:
  - name: my-app
    image: nginx
```

**OnFailure**:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: onfailure-pod
spec:
  restartPolicy: OnFailure
  containers:
  - name: batch-job
    image: busybox
    command: ["sh", "-c", "exit 1"]
```

**Never**:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: never-pod
spec:
  restartPolicy: Never
  containers:
  - name: one-time-task
    image: busybox
    command: ["echo", "Run once and exit"]
```

---

👉 Would you like me to also prepare **interview-style Q&A** on Restart Policies (with tricky scenarios, e.g., Job vs Deployment behavior), or just keep it as a conceptual explanation?
