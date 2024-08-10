## Install Docker In Amazon Linux 2023

```
sudo dnf update -y
sudo dnf install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
```

## Install Docker In Amazon Linux VM

```
sudo yum update -y 
sudo yum install docker -y
sudo service docker start
sudo usermod -aG docker ec2-user
exit
```
## Install Docker In Ubuntu VM

```
sudo apt update
curl -fsSL get.docker.com | /bin/bash
sudo usermod -aG docker ubuntu 
exit
```

## Verify docker installation

```
docker -v
```