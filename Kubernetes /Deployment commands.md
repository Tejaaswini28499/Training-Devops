## Deployment commands
```
kubectl get deployment – List one or more deployments.

kubectl describe deployment <deployment_name> – Display the detailed state of one or more deployments.

kubectl edit deployment <deployment_name> – Edit and update the definition of one or more deployments on the server.

kubectl create deployment <deployment_name> – Create a new deployment.

kubectl delete deployment <deployment_name> – Delete deployments.

kubectl rollout status deployment <deployment_name> – See the rollout status of a deployment.

kubectl set image deployment/<deployment name> <container name>=image:<new image version> – Perform a rolling update (K8S default), set the image of the container to a new version for a particular deployment.

kubectl rollout undo deployment/<deployment name> – Rollback a previous deployment.

kubectl replace --force -f <configuration file> – Perform a replace deployment — Force replace, delete and then re-create the resource.

```
Excellent question 👏 — this is a **real DevOps interview scenario** and also a very practical Kubernetes situation.

Let’s break it down **clearly and step by step** 👇

---

## 🧠 Scenario:

You have **hundreds of deployment files** (microservices).
You applied a new version using:

```bash
kubectl apply -f deployments/
```

But after deployment, your **application started failing** 😢

Now you want to **rollback everything to the previous working version**.

---

## 🔹 Option 1: Roll back all deployments manually (with rollout undo)

Each Deployment in Kubernetes **keeps its revision history** by default.
You can check rollout history and undo.

```bash
kubectl rollout history deployment/<deployment-name>
kubectl rollout undo deployment/<deployment-name>
```

👉 To undo all deployments at once, you can loop through them:

```bash
for deploy in $(kubectl get deploy -o name); do
  kubectl rollout undo $deploy
done
```

✅ This will **rollback every deployment in the namespace** to its previous version.

---

## 🔹 Option 2: Roll back using GitOps / Version control (Recommended in real setups)

If you use **Git + CI/CD (like Jenkins, ArgoCD, or Flux)** —
you don’t manually rollback from kubectl.

Instead:

1. You revert the Git commit that changed the deployment version (image tag, etc.)

   ```bash
   git revert <commit-id>
   git push
   ```
2. Your CI/CD pipeline automatically redeploys the **previous working version**.

✅ This is **safer and auditable**, especially when you have 100s of microservices.

---

## 🔹 Option 3: Roll back using `kubectl rollout undo --to-revision`

If you want to roll back to a **specific older version**:

```bash
kubectl rollout history deployment/<deployment-name>
kubectl rollout undo deployment/<deployment-name> --to-revision=2
```

This lets you return to an older revision (not just the last one).

---

## 🔹 Option 4: Namespace-wide rollback script

If you have **multiple namespaces**, you can loop through all of them:

```bash
for ns in $(kubectl get ns --no-headers -o custom-columns=":metadata.name"); do
  for deploy in $(kubectl -n $ns get deploy -o name); do
    kubectl -n $ns rollout undo $deploy
  done
done
```

---

## 🔹 Option 5: If you use Helm

If your deployments are managed via **Helm charts**, you can rollback using:

```bash
helm rollback <release-name> <revision-number>
```

List revisions:

```bash
helm history <release-name>
```

---

## 🧩 Summary

| Method                 | When to Use                                     | Command                                                                              |
| ---------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------ |
| `kubectl rollout undo` | Quick rollback for a few deployments            | `kubectl rollout undo deployment/<name>`                                             |
| `for loop`             | Rollback all deployments in a namespace         | `for deploy in $(kubectl get deploy -o name); do kubectl rollout undo $deploy; done` |
| Git revert + pipeline  | Best for large-scale & production-safe rollback | `git revert <commit>`                                                                |
| Helm rollback          | If using Helm charts                            | `helm rollback <release> <rev>`                                                      |

---

Would you like me to show an example where 3 microservices (`frontend`, `backend`, `db`) are rolled back together — showing before & after?
