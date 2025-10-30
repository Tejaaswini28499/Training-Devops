apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: standard

  note: once the storage class is created as standard(default storage class) you cannot able to resize as it is statically provisioned.If your PVC is statically provisioned or the StorageClass does not support resizing, 
you'll need to delete the existing PVC and create a new one with the desired size. or while creating it self give the name for storage class as : fast-storage

  we can also resolve by Resize by Deleting and Re-Creating PVC
  To safely resize:

Backup your data.
Delete the old PVC (if it's safe to do so).

Create a new PVC with the desired size.
