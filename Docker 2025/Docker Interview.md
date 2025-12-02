Got it 👍 Since you already have **5 years of DevOps experience**, I'll prepare **Docker interview questions** that suit a **mid-senior (4+ years) level**, where interviewers expect you to know both **fundamentals and real-world scenarios**.

---

## 🔹 Docker Interview Questions (for 4 years experience)

### 1. Basics & Architecture

* What is Docker, and how is it different from a virtual machine (VM)?
* Explain Docker architecture (Docker Daemon, Docker CLI, Docker Engine, containerd).
* What is the role of namespaces and cgroups in Docker?
* Difference between Docker image and container?
* How does a Docker registry (like Docker Hub) work?

---

### 2. Images & Containers

* What happens internally when you run `docker run`?
docker run pulls the image if needed, creates a container filesystem using UnionFS, sets up namespaces and cgroups for isolation, configures networking, and finally starts the container’s main process as PID 1.
* Difference between `docker run`, `docker exec`, and `docker attach`?
docker attach connects your terminal to a running container's main process (PID 1). You see the same output and can interact with it. It does not start a new shell; for that, we use docker exec.
* Why is `docker commit` not recommended in production?
docker commit takes the current state of a container and creates a new Docker image from it by converting the container’s writable layer into a permanent image layer. It is useful for quick snapshots but not recommended for production; Dockerfile is preferred.
* How do you reduce the size of a Docker image?
* What is a multi-stage Dockerfile? Why use it?

---

### 3. Dockerfile

* Explain best practices for writing a Dockerfile.
* Why do we use `WORKDIR` and `COPY requirements.txt` before `pip install` in Python projects?
* What is the difference between `ADD` and `COPY`?
* How do you handle secrets (like passwords or API keys) in Dockerfile?
* What is the purpose of `.dockerignore`?

---

### 4. Networking

* Explain different Docker networking modes (`bridge`, `host`, `overlay`, `macvlan`, `none`).
* How do containers communicate with each other in the same network?
* What is port mapping? Example with `-p 8080:80`.
* How do you expose a container service to another host?

---

### 5. Volumes & Storage

* Difference between **Docker volumes** and **bind mounts**?
* Where are Docker volumes stored on the host?
* How do you back up and restore Docker volumes?
* What are tmpfs mounts? When do you use them?

---

### 6. Docker Compose

* What is Docker Compose? Why use it?
* Difference between `docker run` and `docker-compose up`.
* Explain this line in a `docker-compose.yml`:

  ```yaml
  volumes:
    - ./src:/usr/share/nginx/html
  ```
* How do you scale services using Docker Compose?

---

### 7. Orchestration (Docker Swarm / Kubernetes context)

* What is Docker Swarm? Difference from Kubernetes?
* Explain how service discovery works in Docker Swarm.
* How do you achieve container high availability?
* Have you deployed containers on Kubernetes? (They may switch to K8s questions here)

---

### 8. Security

* How do you scan Docker images for vulnerabilities?
* What is a distroless image, and why is it used?
* How do you prevent running containers as root?
* How do you restrict container resources (CPU, memory)?

---

### 9. Debugging & Troubleshooting

* A container keeps exiting immediately after starting. How do you troubleshoot?
* How do you check container logs?
* Difference between `docker ps -a` and `docker ps`.
* How do you monitor Docker container resource usage?
* What happens if the Docker daemon crashes?

---

### 10. Real-World / Scenario Based

* You deployed an app in Docker, but it cannot connect to the database container. How do you debug?
* A container is consuming too much memory; how do you limit it?
* How do you handle persistent data in containers across restarts?
* If you have a container running in production, how do you apply a patch without downtime?
* How do you roll back a Docker deployment?

---

✅ **Pro tip for interviews**:
At 4 years experience, they won’t just ask commands. They’ll test if you:

* Know **best practices** (small images, caching, security).
* Can **debug real issues** (network, storage, performance).
* Have **hands-on exposure** with Compose, registries, and orchestration.

---

Do you want me to also prepare a **list of practical hands-on tasks** (like “write a Dockerfile for Python app”, “fix a broken Compose file”) that interviewers might give?
