virtual machine: 

server which can be provided by IBM or HP upon that you will install hypervisor 
hypervisor: is a software that can install your VM's on BareMetal or physical servers

Instead of one server you are logically isolation breaking that into many and calling as VM's 

popular hypervisor : VMware, Xen 

VM's are virtual environment which function as  virtual computer systems its not depending on CPU, memory, hardware, OS from one VM to another VM

they are tightly separated

physical server - vm's (solved some problems wit Physical Servers) - containers (solved some problems wit VM's) -- check advantage and disadvantage btw this 3 

Virtual Machine has a complete OS but containers as partial and containers use resources from VM's or Physical servers(host opertating systems) they are running on 






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


docker build - using docker file it will build the image 
docker run - the image will run and create a container 
docker pull - pull the image from the registry 
 
the commands will be run on docker client or docker engine and it will go to docker daemon which is heart of docker if it fails the containers will not work 
 
the commands are given in CLI it will go to docker daemon and create a image, container and push the image to registry and pull the image we need to have account in docker registry and login then we can push the image to artifactory.


 
Explain Docker file and diff btw entrypoint: you can override the values here and CMD you can override values

port mapping from container- 8000 to EC2 add inbound traffic rules allow port 8000 (tcp) to security group



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



