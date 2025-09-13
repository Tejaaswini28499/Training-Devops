Got it 👍 Let’s go step by step. I’ll explain **Docker commands in detail** with categories, syntax, usage, and examples.

---

# 🔹 1. Docker Setup & Information Commands

### 👉 `docker --version`

Shows the installed Docker version.

```bash
docker --version
# Docker version 25.0.3, build abc123
```

### 👉 `docker info`

Displays detailed information about the Docker installation, running containers, images, storage driver, etc.

```bash
docker info
```

### 👉 `docker login`

Logs into a Docker registry (default: Docker Hub).

```bash
docker login -u <username> -p <password>
```

### 👉 `docker logout`

Logs out from Docker registry.

```bash
docker logout
```

---

# 🔹 2. Docker Image Commands

### 👉 `docker pull`

Downloads an image from Docker Hub (or another registry).

```bash
docker pull nginx:latest
```

### 👉 `docker images`

Lists available images on the host.

```bash
docker images
```

### 👉 `docker build`

Builds an image from a Dockerfile.

```bash
docker build -t my-python-app .
```

* `-t` → tag name for the image.
* `.` → location of Dockerfile.

### 👉 `docker rmi`

Removes an image.

```bash
docker rmi nginx:latest
```

### 👉 `docker tag`

Tags an image for uploading to a repository.

```bash
docker tag my-python-app myrepo/my-python-app:v1
```

### 👉 `docker push`

Pushes an image to a registry.

```bash
docker push myrepo/my-python-app:v1
```

---

# 🔹 3. Docker Container Commands

### 👉 `docker run`

Creates and starts a container.

```bash
docker run -d -p 8080:80 nginx
```

* `-d` → detached mode (runs in background).
* `-p 8080:80` → maps host port `8080` → container port `80`.
* `nginx` → image name.

### 👉 `docker ps`

Lists running containers.

```bash
docker ps
```

### 👉 `docker ps -a`

Lists all containers (including stopped ones).

### 👉 `docker start` / `docker stop`

Start or stop a container by ID or name.

```bash
docker start mycontainer
docker stop mycontainer
```

### 👉 `docker restart`

Restarts a container.

### 👉 `docker rm`

Removes a container.

```bash
docker rm mycontainer
```

### 👉 `docker exec`

Runs a command inside a running container.

```bash
docker exec -it mycontainer bash
```

* `-it` → interactive + terminal.

### 👉 `docker attach`

Attaches your terminal to a running container.

### 👉 `docker logs`

Shows logs of a container.

```bash
docker logs mycontainer
docker logs -f mycontainer   # follow logs in real-time
```

---

# 🔹 4. Docker Volume & Network Commands

### 👉 `docker volume create`

Creates a new volume for persistent storage.

```bash
docker volume create mydata
```

### 👉 `docker volume ls`

Lists volumes.

### 👉 `docker volume rm`

Removes a volume.

### 👉 `docker network ls`

Lists networks.

### 👉 `docker network create`

Creates a custom network.

```bash
docker network create mynetwork
```

### 👉 `docker network connect` / `disconnect`

Connect or disconnect containers from a network.

---

# 🔹 5. Docker System Commands

### 👉 `docker system df`

Shows Docker disk usage (images, containers, volumes).

### 👉 `docker system prune`

Removes all unused containers, networks, images, and caches.

```bash
docker system prune -a -f
```

---

# 🔹 6. Docker Compose (multi-container apps)

If you’re using `docker-compose.yml`:

### 👉 `docker compose up`

Starts services.

```bash
docker compose up -d
```

### 👉 `docker compose down`

Stops and removes containers.

### 👉 `docker compose ps`

Shows containers created by Compose.

---

✅ **Tip:** To quickly clean everything:

```bash
docker stop $(docker ps -q)        # stop all containers
docker rm $(docker ps -aq)         # remove all containers
docker rmi $(docker images -q)     # remove all images
```

---

Do you want me to also prepare a **cheat sheet with diagrams (images/containers/volumes/networks relationships)** so you can revise fast before interviews?
