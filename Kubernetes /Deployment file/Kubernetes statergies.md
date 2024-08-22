there are 6 types of statergies:
1. Recreate
2. Rolling Updates
3. Canary
4. Blue-Green
5. A/B testing
6. Shadow Deployment

## Rolling Update
```
Description: Gradually replaces old Pods with new ones without downtime. It ensures that a certain number of Pods are always available during the update process.
Parameters:
maxUnavailable: The maximum number of Pods that can be unavailable during the update.
maxSurge: The maximum number of Pods that can be created over the desired number of Pods.
eg:
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
```
## Recreate 
```
Description: Stops all the existing Pods before creating new ones. This strategy may cause downtime as all Pods are terminated before new ones are started.
Usage: Useful when the application cannot handle multiple versions running simultaneously or when you want a clean start.
```

## Blue Green
```
Description: Involves running two environments: a "blue" environment (current version) and a "green" environment (new version). You switch traffic from the blue to the green environment when the new version is ready.
```
## Canary
```
Introduces a new version of the application to a small subset of users before rolling it out to everyone. This helps monitor performance and stability before a full deployment.
```

## A/B
```
Similar to canary deployments, but focuses on comparing two versions (A and B) to determine which performs better based on user interactions or metrics.
```

## Shadow Deployment
```
Deploys a new version of the application alongside the current version without exposing it to users. It allows monitoring of the new version's performance under real traffic conditions.
```