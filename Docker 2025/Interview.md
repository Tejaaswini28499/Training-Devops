Here’s a detailed set of **Docker interview questions** organized by **basic, intermediate, and advanced levels** along with brief explanations/answers where necessary. This will help you prepare thoroughly.

---

## **Basic Docker Questions**

1. **What is Docker?**

   * Docker is a platform that allows you to develop, ship, and run applications in **containers**. Containers are lightweight, portable, and include everything needed to run the app.

2. **Difference between a container and a virtual machine (VM)**

   | Feature        | Container             | VM             |
   | -------------- | --------------------- | -------------- |
   | OS             | Shares host OS kernel | Full OS per VM |
   | Boot time      | Seconds               | Minutes        |
   | Resource usage | Lightweight           | Heavy          |
   | Isolation      | Process-level         | Hardware-level |

3. **What is a Docker image?**

   * A read-only template used to create containers. It contains the application and dependencies.

4. **What is a Docker container?**

   * A running instance of a Docker image. It is isolated and lightweight.

5. **What is Docker Hub?**

   * A public registry for Docker images, like GitHub for code.

6. **Difference between `docker run` and `docker create`**

   * `docker create` creates a container but doesn’t start it.
   * `docker run` creates **and starts** the container.

7. **Basic Docker commands**

   * `docker ps` – list running containers
   * `docker ps -a` – list all containers
   * `docker images` – list images
   * `docker rm <container>` – remove container
   * `docker rmi <image>` – remove image

---

## **Intermediate Docker Questions**

1. **What is Dockerfile?**

   * A text file with instructions to build a Docker image. Example instructions: `FROM`, `RUN`, `COPY`, `CMD`.

2. **Explain the difference between `CMD` and `ENTRYPOINT`**

   * `CMD` – default command, can be overridden during `docker run`.
   * `ENTRYPOINT` – fixed command, not easily overridden.

3. **What is Docker Compose?**

   * A tool to define and run multi-container Docker applications using a YAML file (`docker-compose.yml`).

4. **What is the difference between a volume and a bind mount?**

   | Feature     | Volume                  | Bind Mount     |
   | ----------- | ----------------------- | -------------- |
   | Managed by  | Docker                  | Host OS        |
   | Path        | Docker decides location | User-specified |
   | Portability | High                    | Low            |

5. **How do you share data between containers?**

   * Use **volumes**, **bind mounts**, or **Docker networks** for communication.

6. **What is a Docker network?**

   * Allows containers to communicate with each other. Types:

     * `bridge` (default)
     * `host`
     * `overlay`
     * `macvlan`

7. **How do you check logs of a container?**

   ```bash
   docker logs <container_name_or_id>
   ```

8. **How do you access a running container’s shell?**

   ```bash
   docker exec -it <container_name> /bin/bash
   ```

9. **How to build an image from Dockerfile?**

   ```bash
   docker build -t <image_name>:<tag> .
   ```

10. **How do you remove all stopped containers and dangling images?**

    ```bash
    docker system prune -a
    ```

---

## **Advanced Docker Questions**

1. **What is a multi-stage Docker build?**

   * Used to reduce image size by using one stage for building the app and another for running it.

2. **How do you handle environment variables in Docker?**

   * Use `ENV` in Dockerfile or `-e` during `docker run`, or `.env` files with Docker Compose.

3. **What is the difference between Docker Swarm and Kubernetes?**

   | Feature   | Docker Swarm | Kubernetes     |
   | --------- | ------------ | -------------- |
   | Setup     | Easy         | Complex        |
   | Scaling   | Limited      | Advanced       |
   | Community | Smaller      | Large & Active |

4. **Explain Docker image layering**

   * Each instruction in a Dockerfile creates a **layer**. Layers are cached and reused to speed up builds.

5. **How to optimize Docker images?**

   * Use smaller base images (`alpine`)
   * Remove unnecessary files (`rm -rf /var/cache`)
   * Combine `RUN` commands to reduce layers

6. **What are some common Docker security best practices?**

   * Run as non-root user
   * Limit container capabilities
   * Use trusted images
   * Regularly scan images

7. **Explain the difference between `COPY` and `ADD` in Dockerfile**

   * `COPY` – simple copy files/directories.
   * `ADD` – can copy **and extract tar files** or download from URLs.

8. **How to pass secrets to Docker containers?**

   * Use Docker **secrets** in Swarm mode, environment variables, or `.env` files.

---

1. real time docker challenges you face - abhi video Interview of docker 11th question 
2. how to secure docker container - abhi video Interview of docker 12th question 
