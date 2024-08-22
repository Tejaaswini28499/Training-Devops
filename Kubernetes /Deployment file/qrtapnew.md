apiVersion: apps/v1
kind: Deployment
metadata:
  name: qrtap-redirect
spec:
  replicas: 1
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1           # Specifies the maximum number of Pods that can be unavailable during the update process
      maxSurge: 1                  # Specifies the maximum number of Pods that can be created over the desired number of Pods
  selector:
    matchLabels:
      app: qrtap-redirect
  template:
    metadata:
      labels:
        app: qrtap-redirect
    spec:
      containers:
        - name: qrtap-redirect
          image: justwicks/qrtap-redirect:latest
          ports:
            - containerPort: 3000
          env:
            - name: MONGODB_URL
              valueFrom:
                secretKeyRef:
                  name: mongodb-secret
                  key: mongodb-url
            - name: NODE_ENV
              valueFrom:
                configMapKeyRef:
                  name: qrtap-config
                  key: NODE_ENV
            - name: REDIS_URL
              value: "redis://10.103.47.229:6379"
            - name: PATH_NAME
              valueFrom:
                configMapKeyRef:
                  name: qrtap-config
                  key: PATH_NAME
          volumeMounts:
            - name: my-storage
              mountPath: /app/data
      volumes:
        - name: my-storage
          persistentVolumeClaim:
            claimName: my-pvc
      imagePullSecrets:
        - name: yogi-ass
      restartPolicy: Always