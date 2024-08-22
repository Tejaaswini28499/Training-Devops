apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-storage
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
  fsType: ext4
reclaimPolicy: Retain
allowVolumeExpansion: True
volumeBindingMode: WaitForFirstConsumer


note: there are 14 types of storage classes based on the requriement we can use it accordingly