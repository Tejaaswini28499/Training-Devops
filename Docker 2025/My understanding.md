virtual machine: 

server which can be provided by IBM or HP upon that you will install hypervisor 
hypervisor: is a software that can install your VM's on BareMetal or physical servers

Instead of one server you are logically isolation breaking that into many and calling as VM's 

popular hypervisor : VMware, Xen 

VM's are virtual environment which function as  virtual computer systems its not depending on CPU, memory, hardware, OS from one VM to another VM

they are tightly separated

physical server - vm's (solved some problems wit Physical Servers) - containers (solved some problems wit VM's) -- check advantage and disadvantage btw this 3 

Virtual Machine has a complete OS but containers as partial and containers use resources from VM's or Physical servers(host opertating systems) they are running on 
<img width="946" height="622" alt="image" src="https://github.com/user-attachments/assets/a610b7dc-18f4-4e28-8d9e-faf1023862c2" />


<img width="957" height="625" alt="image" src="https://github.com/user-attachments/assets/e9d185d4-2ad7-4b2a-9403-71bba41bd0f7" />




Docker containers are light weight in nature as it doesn't have full OS they use recourses from host OS. 

And if you need to run 10 different containers in single VM there is something called Base image in which it contain all the dependencies, application and  Libraries will form a docker image

there should be logical isolation btw the containers and that can be provided in the system dependencies bcz if hacker hacks one container as its share the kernel and use resources from OS they can destroy the whole cluster so thats the reason we need to have logical isolation btw the containers

files and folders that our containers has and this are the once which does logical isolation: 

This files and folders are not used from the kernel if we are using we are compromising on our Security. this will be part of container or the base image

    /bin: contains binary executable files, such as the ls, cp, and ps commands.

    /sbin: contains system binary executable files, such as the init and shutdown commands.

    /etc: contains configuration files for various system services.

    /lib: contains library files that are used by the binary executables.

    /usr: contains user-related files and utilities, such as applications, libraries, and documentation.

    /var: contains variable data, such as log files, spool files, and temporary files.

    /root: is the home directory of the root user.

Files and Folders that containers use from host operating system

    The host's file system: Docker containers can access the host file system using bind mounts, which allow the container to read and write files in the host file system.

    Networking stack: The host's networking stack is used to provide network connectivity to the container. Docker containers can be connected to the host's network directly or through a virtual network.

    System calls: The host's kernel handles system calls from the container, which is how the container accesses the host's resources, such as CPU, memory, and I/O.

    Namespaces: Docker containers use Linux namespaces to create isolated environments for the container's processes. Namespaces provide isolation for resources such as the file system, process ID, and network.

    Control groups (cgroups): Docker containers use cgroups to limit and control the amount of resources, such as CPU, memory, and I/O, that a container can access.
    



Docker daemon lifecycle: you need a docker file(set of instructions) and build it on Docker engine to get the docker image and run the image on docker engine to get the docker container 

[Daemon Start] --> [Listen for Requests] --> [Manage Containers]
                                         |--> [Create]
                                         |--> [Start]
                                         |--> [Running]
                                         |--> [Stop]
                                         |--> [Remove]
                     --> [Log Events / Monitor]
                     --> [Daemon Shutdown / Restart]

<img width="1014" height="514" alt="image" src="https://github.com/user-attachments/assets/0148699a-fd3b-417a-972b-849055b6ba78" />

docker build - using docker file it will build the image 
docker run - the image will run and create a container 
docker pull - pull the image from the registry 
 
the commands will be run on docker client or docker engine and it will go to docker daemon which is heart of docker if it fails the containers will not work 
 
the commands are given in CLI it will go to docker daemon and create a image, container and push the image to registry and pull the image we need to have account in docker registry and login then we can push the image to artifactory.


 
Explain Docker file and diff btw entrypoint: you can override the values here and CMD you can override values

port mapping from container- 8000 to EC2 add inbound traffic rules allow port 8000 (tcp) to security group

-------------------------------

Commands:
docker ps - options(a,l,q)
docker rm - options(f,v,l)
docker exec - options(d,i,e)                                   
------------
docker ps
docker login
docker run -d -p <hostport:container port> <image_name>
docker build -t <image_name> . 
docker images
docker rmi <image_id/image_name>
docker rm <container_name>
docker pull <image_name>
docker container start
docker container stop
docker container restart
docker push
docker container top <container_id_or_name>

docker image prune
---------------------------
Docker:

build the docker image
run docker image
check the logs
login to conatianer
start and stop restart

---------------
Docker network:

types of networking:
1. Bridge networking: 
2. host networking: this will bind the container with the host ip that is if the host ip is 192.1.3.4 the container ip will be 192.1.3.6 it will be the same subnet range. anyone have access to host will be having access to container but this is not secure 
3. overlay networking : helpful in having multiple host on single cluster


1. make to talk with container 1 with conatiner 2
2. Isolate from container 1 with container 2
3. create container with host network

1. whenever you create a container there is virtual ethernet created which is also called as docker 0 helps to talk from one container to another and this is called bridge networking as host as different ip and container has different ip they are not able to talk that is why its called bridge networking also called veth or docker 0
if you try to delete this default network or bridge network you will be never able to talk to container again from host

2. Isolate: the bridge network allows you to create a custom bridge network
<img width="916" height="508" alt="image" src="https://github.com/user-attachments/assets/af5241ca-7c92-43a0-a133-660b3953d2f2" />

docker run -d --name login nginx:latest
docker run -d --name logout nginx:latest
docker exec -it login /bin/bash
apt update
apt-get install iputils-ping -y
docker inspect login
ping "ip" - as it's in same subnet it will ping from one container to another as it uses bridge ootb bridge networking 
docker network ls
docker network rm "name"


isolation:
docker network create secure-network 
docker run -d --name finance --network=secure-network nginx:latest
docker inspect finance

create container with host network
docker run -d --name host-demo --network=host nginx:latest 
-- ip would be different, no custom ip, binded with host ip itself, no virtual network created


Docker Volumes
Create and manage volumes
sudo docker volume create geeksforgeeks
sudo docker volume inspect geeksforgeeks
sudo docker run -it -v geeksforgeeks:/shared-volume --name my-container-01 ubuntu
ls
cd /shared-volume
echo “GeeksforGeeks” > geeksforgeeks.txt
ls
exit
sudo docker run -it -v geeksforgeeks:/shared-volume --name my-container-02 ubuntu
If you go to the shared-volume directory and list the files, you will find the geeksforgeeks.txt file that you had created in the same volume but mounted in my-container-01 earlier and it also has the same content inside it. This is so because the volume is shared among the two Containers.

docker volume create my_volume
docker run -d --name mongo -v mongovol:/data/db   -e MONGO_INITDB_ROOT_USERNAME=devdb -e MONGO_INITDB_ROOT_PASSWORD=devdb123
docker run --rm -v mongovol:/data/db   busybox ls /data/db

Differences between -v and --mount behavior
Share Data Between Machines





