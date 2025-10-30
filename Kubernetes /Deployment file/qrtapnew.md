apiVersion: apps/v1
kind: Deployment
metadata:
  name: qrtap-redirect                     # → kubectl get deployment qrtap-redirect
spec:
  replicas: 1                              # → kubectl scale deployment qrtap-redirect --replicas=1
  strategy:
    type: RollingUpdate                    # → kubectl rollout status deployment qrtap-redirect
    rollingUpdate:
      maxUnavailable: 1                    # → kubectl rollout history deployment qrtap-redirect
      maxSurge: 1
  selector:
    matchLabels:
      app: qrtap-redirect                  # → kubectl get pods -l app=qrtap-redirect
  template:
    metadata:
      labels:
        app: qrtap-redirect
    spec:
      containers:
        - name: qrtap-redirect
          image: justwicks/qrtap-redirect:latest
          imagePullPolicy: Always          # → kubectl describe pod <pod-name> | grep Image
          ports:
            - containerPort: 3000          # → kubectl get pods -o wide
          env:
            - name: MONGODB_URL
              valueFrom:
                secretKeyRef:
                  name: mongodb-secret      # → kubectl get secret mongodb-secret -o yaml
                  key: mongodb-url
            - name: NODE_ENV
              valueFrom:
                configMapKeyRef:
                  name: qrtap-config        # → kubectl get configmap qrtap-config -o yaml
                  key: NODE_ENV
            - name: REDIS_URL
              value: "redis://10.97.90.108:6379"
            - name: PATH_NAME
              valueFrom:
                configMapKeyRef:
                  name: qrtap-config        # → kubectl describe configmap qrtap-config
                  key: PATH_NAME
          volumeMounts:
            - name: my-storage
              mountPath: /app/data          # → kubectl exec -it <pod-name> -- ls /app/data
      volumes:
        - name: my-storage
          persistentVolumeClaim:
            claimName: my-pvc               # → kubectl get pvc my-pvc -o wide
      imagePullSecrets:
        - name: yogi-ass                    # → kubectl get secret yogi-ass -o yaml
      restartPolicy: Always                 # → kubectl describe pod <pod-name> | grep Restart
