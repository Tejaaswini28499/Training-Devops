apiVersion: apps/v1
kind: Deployment
metadata:
  name: qrtap-in
spec:
  replicas: 1
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  selector:
    matchLabels:
      app: qrtap-in  # Updated the label to match the new naming convention
  template:
    metadata:
      labels:
        app: qrtap-in  # Updated the label to match the new naming convention
    spec:
      containers:
        - name: qrtap-in  # Changed from "qrtap.in" to "qrtap-in"
          image: justwicks/qrtap.in:latest
          imagePullPolicy: Always
          ports:
            - containerPort: 3000
          env:
            - name: BASE_URL
              value: "https://api.qrtap.in"
            - name: STRIPE_PUBLIC_KEY
              value: "pk_test_51L1EKFSCRoWX8ryTXvu5Ae8rIgQUuKVpt9W8LNON3ClvhZnBgxRPGDgpgSviqUREGKhiMsmSQnnLI2uqWbFbu32f00PBbF6Ldc"
            - name: PAYPAL_CLIENT_ID
              value: ""
            - name: CLOUDINARY_CLOUD_NAME
              value: "demffulwc"
            - name: CURRENCY
              value: "INR"
            - name: SHIPPING_FEE
              value: "0"
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
