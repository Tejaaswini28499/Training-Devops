

  note: once the storage class is created as standard(default storage class) you cannot able to resize as it is statically provisioned.If your PVC is statically provisioned or the StorageClass does not support resizing, 
you'll need to delete the existing PVC and create a new one with the dHere’s your **PVC YAML** with detailed **inline comments** explaining each line 👇

```yaml
apiVersion: v1                      # API version for PersistentVolumeClaim resources
kind: PersistentVolumeClaim         # Defines the resource type as a PVC
metadata:
  name: my-pvc                      # Name of the PVC (used by pods to reference this claim)
spec:
  accessModes:
    - ReadWriteOnce                 # The volume can be mounted as read-write by only one node
  resources:
    requests:
      storage: 1Gi                  # The amount of storage requested (1 Gigabyte)
  storageClassName: standard        # Uses the 'standard' StorageClass for dynamic provisioning
```

---

### 💡 **What Happens When You Apply This:**

1. Kubernetes checks for a **StorageClass named `standard`**.
2. The provisioner in that StorageClass (e.g., `kubernetes.io/aws-ebs` or `kubernetes.io/gce-pd`)
   automatically **creates a PersistentVolume (PV)** that matches this claim.
3. The new PV of size **1Gi** is **bound** to this PVC.
4. When a **Pod** uses this PVC, it gets a **dedicated storage volume** of 1Gi.

---

Would you like me to add a **Pod example** that uses this PVC so you can see how it connects?
esired size. or while creating it self give the name for storage class as : fast-storage

  we can also resolve by Resize by Deleting and Re-Creating PVC
  To safely resize:

Backup your data.
Delete the old PVC (if it's safe to do so).

Create a new PVC with the desired size.

