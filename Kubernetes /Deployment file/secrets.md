apiVersion: v1
kind: Secret
metadata:
  name: mongodb-secret
type: Opaque
data:
  mongodb-url: bW9uZ29kYitzcnY6Ly93ZWIzY2hhaW50ZWNobm9sb2d5Oms1NFEzS1V2bWhGTHhpWDBAcXJ0YXAucHZmN29lZC5tb25nb2RiLm5ldC8/cmV0cnlXcml0ZXM9dHJ1ZSZ3PW1ham9yaXR5

  note: mongo-db url is the encryped code in Base-64 
  
  ## encode using the command 
  ```
  echo -n 'mongodb+srv://web3chaintechnology:k54Q3KUvmhFLxiX0@qrtap.pvf7oed.mongodb.net/?retryWrites=true&w=majority' | base64
  ```
## Extract and Decode the Secret

```
kubectl get secret <secret-name> -o yaml

kubectl get secret <secret-name> -o jsonpath="{.data.mongodb-url}" | base64 --decode
```
