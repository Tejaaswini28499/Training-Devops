I have created a new usergroup called teju in our server machine 

using useradd teju and added teju to admin group as it had a sudo user permission 

other then that there were few other groups where "yogesh" user had the permission and "teju" was added to all the groups using the command "sudo usermod -aG adm,cdrom,sudo,dip,plugdev,lxd,docker teju"

So in the prod environment there were docker, nginx, installed to check wheather installed in Dev environment use the below command
"sudo systemctl status nginx" & "sudo systemctl status docker" 
if its active and running then both are installed in devenvironment.

After all this we need to create a docker-compose.yaml file in decsto directory
after creating we need to perform below commands
"docker-compose pull"
"docker-compose up -d"
Note: docker-compose pull & up should be happen where the yaml file is located if you ar edoing it from anywhere then you will get an error.

To check the services are up and running do "docker ps"

## Important Notes

```
In an application there will be 3 main parts called 
Frontend, Backend, Database
The end user will access  only the frontend but there should be a connection btw fe and be so  this will be created
Fe env file there will pass the backend url in the keyname. fe will be deployed. So fe call happens fe will go to DNS, subdomain which IP mapped will see and the request is sent to that machine, 
note: default in the end of ip address there will be 443 which is the HTTPS port  Default it will run in HTTPS(when you generate the Certbot automatically http request will turn into https) So this certbot creation will happen in nginx.conf file and nginx will be lizesing to only 443 port which is HTTPS so once its come inside the nginx based on the subdomain it will go inside the service so inside that there will be many containers like /main /storej and so on based on the link passed in the fe it will go to requried port.
```

