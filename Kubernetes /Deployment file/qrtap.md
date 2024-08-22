apiVersion: apps/v1
kind: Deployment
metadata:
  name: qrtap-redirect
spec:
  replicas: 1
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
              value: "mongodb+srv://web3chaintechnology:k54Q3KUvmhFLxiX0@qrtap.pvf7oed.mongodb.net/?retryWrites=true&w=majority"
            - name: NODE_ENV
              value: "production"
            - name: REDIS_URL
              value: "redis://10.103.47.229:6379"
            - name: PATH_NAME
              value: 
      imagePullSecrets:
        - name: yogi-ass
      restartPolicy: Always
