apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-commander
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis-commander
  template:
    metadata:
      labels:
        app: redis-commander
    spec:
      containers:
      - name: redis-commander
        image: rediscommander/redis-commander
        ports:
        - containerPort: 8081
        env:
        - name: REDIS_HOSTS
          value: "local:redis:6379"
        - name: HTTP_USER
          value: "justwicks"
        - name: HTTP_PASSWORD
          value: "justwicks;;99"