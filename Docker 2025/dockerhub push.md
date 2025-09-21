Got it 👍 Let me give you **step-by-step commands** starting from installing Docker on your Amazon Linux EC2 instance → building & pushing image to Docker Hub (or any registry) → pulling it back → checking if it runs.

---

# 🚀 Steps to Install Docker, Push & Pull Images on Amazon Linux EC2

## 1️⃣ **Connect to your EC2 instance**

```bash
ssh -i your-key.pem ec2-user@<EC2-Public-IP>
```

---

## 2️⃣ **Update system & install Docker**

For **Amazon Linux 2**:

```bash
sudo yum update -y
sudo amazon-linux-extras enable docker
sudo yum install -y docker
```

For **Amazon Linux 2023**:

```bash
sudo dnf update -y
sudo dnf install -y docker
```

---

## 3️⃣ **Start & enable Docker service**

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

Check status:

```bash
sudo systemctl status docker
```

---

## 4️⃣ **Add your user to Docker group (so no sudo needed)**

```bash
sudo usermod -aG docker ec2-user
```

👉 Then log out & back in (or run `newgrp docker`) to apply.

---

## 5️⃣ **Verify Docker installation**

```bash
docker --version
docker ps
```

---

## 6️⃣ **Login to Docker Hub (or your registry)**

```bash
docker login
```

* Enter your Docker Hub **username** and **password/Access Token**.

---

## 7️⃣ **Create a sample Dockerfile**

```bash
mkdir myapp && cd myapp
nano Dockerfile
```

Paste:

```dockerfile
FROM alpine:latest
CMD ["echo", "Hello from Docker on EC2!"]
```

---

## 8️⃣ **Build Docker image**

```bash
docker build -t myapp:latest .
```

Check image:

```bash
docker images
```

---

## 9️⃣ **Tag the image for Docker Hub**

Replace `your-dockerhub-username` with your Docker Hub username:

```bash
docker tag myapp:latest your-dockerhub-username/myapp:latest
```

---

## 🔟 **Push image to Docker Hub**

```bash
docker push your-dockerhub-username/myapp:latest
```

---

## 1️⃣1️⃣ **Remove local image (to test pulling)**

```bash
docker rmi your-dockerhub-username/myapp:latest myapp:latest
docker images
```

---

## 1️⃣2️⃣ **Pull image from Docker Hub**

```bash
docker pull your-dockerhub-username/myapp:latest
```

---

## 1️⃣3️⃣ **Run and test container**

```bash
docker run --rm your-dockerhub-username/myapp:latest
```

Expected output:

```
Hello from Docker on EC2!
```

---

✅ Now your image is built, pushed to registry, pulled back, and verified!

Do you want me to also add the **same steps for Amazon Elastic Container Registry (ECR)** instead of Docker Hub, in case you’re planning AWS-native registry?
Good question 👍 That command is very important for convenience and security when working with Docker. Let me break it down clearly:

---

## 🔹 Command:

```bash
sudo usermod -aG docker ec2-user
```

---

## 🔹 What it does

* `usermod` → Linux command to modify a user account.
* `-aG docker` → Adds (`-a`) the user to an additional **group** (`-G`), here the **`docker` group**.
* `ec2-user` → The default login user in Amazon Linux EC2.

So, this command **adds the `ec2-user` to the `docker` group**.

---

## 🔹 Why this is needed

By default:

* The **Docker daemon** (`dockerd`) runs as **root**.
* That means every time you run a Docker command, you’d need to use `sudo`:

  ```bash
  sudo docker ps
  sudo docker build -t myapp .
  ```
* To avoid typing `sudo` all the time, Docker creates a **Linux group** called `docker`.
* Members of this group are allowed to run Docker commands **without sudo**.

---

## 🔹 After running the command

1. You must **log out and log back in** (or run `newgrp docker`) so the group change takes effect.
2. Then you can run:

   ```bash
   docker ps
   docker images
   ```

   without needing `sudo`.

---

## 🔹 Example before & after

**Before adding user to docker group:**

```bash
[ec2-user@ip-xxx ~]$ docker ps
Got permission denied while trying to connect to the Docker daemon socket
```

**After adding user to docker group:**

```bash
[ec2-user@ip-xxx ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS   NAMES
```

---

⚠️ **Security note:**
Giving a user access to the `docker` group is similar to giving **root privileges** because Docker can mount host files, run privileged containers, etc. That’s why AWS best practices recommend restricting who gets added.

---

👉 Do you want me to also explain **what happens if you don’t add `ec2-user` to the docker group** and you just keep using `sudo`?
