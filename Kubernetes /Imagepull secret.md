## commandline Imagepull secret
```
kubectl create secret docker-registry yogi-ass \
    --docker-server=https://index.docker.io/v1/ \
    --docker-username=justwicks \
    --docker-password=<password> \
    --docker-email=<your-email>
```
kubectl create secret docker-registry image-secret1 \
    --docker-server=https://index.docker.io/v1/ \
    --docker-username=justwicks \
    --docker-password=<password> -n qrtap-backend

## JSON Structure
```
kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=/path/to/.docker/config.json \
    --type=kubernetes.io/dockerconfigjson
```

## create of Imagepull 
```
1. JSON Structure for .dockerconfigjson:
2. Commandline(as above)
```
## types of Imagepull Policy

```
The `imagePullPolicy` field in a Kubernetes container specification determines when the kubelet should attempt to pull (download) the container image from the container registry. It can take one of the following three values:

1. `Always`
- **Description**: The image will always be pulled before the container starts. This ensures that the latest image is used, even if an image with the same tag is already present on the node.
- **Use Case**: Useful in environments where images are frequently updated and tagged with the same version (e.g., `latest`).

2. `IfNotPresent`
- **Description**: The image is pulled only if it is not already present on the node. If the image with the specified tag is already present, it will use the local copy.
- **Use Case**: This is the default behavior for images with a specific tag (not `latest`). It is useful for reducing network traffic and pulling times when you are sure that the image does not change frequently.

3. `Never`
- **Description**: The image will never be pulled, and Kubernetes will use the local image on the node. If the image is not present on the node, the pod will fail to start.
- **Use Case**: Useful in air-gapped environments or when you want to ensure that the container is only started if the image is already present on the node.

Example Usage in a Pod Specification
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: my-image:latest
    imagePullPolicy: Always   # Can be Always, IfNotPresent, or Never
```

### Default Behavior
```
- **For images with the tag `latest`**: The default `imagePullPolicy` is `Always`.
- **For images with a specific tag (e.g., `v1.0`)**: The default `imagePullPolicy` is `IfNotPresent`.
```
### Summary
```
- **`Always`**: Ensures the latest image is always pulled.
- **`IfNotPresent`**: Uses the local image if available.
- **`Never`**: Uses the local image and never pulls from the registry.
```