AWS offering- 175 fully featured services

There are 77 Availability Zones within 24 geographic regions 


In EC2 the names have to be given with respect to the environment it belongs to 
eg: dev, prod, testing, staging ans so on

Requriments to be gathered before setting up the EC2 machine
1. OS - centos, Derbian
2. Size - RAM,CPU,Network etc eg:Min
3. Storage size - 10gigs
4. Project
5. Services/Apps Running - SSH,Http,Mysql etc
6. Environment(Dev,QA, Prod, Staging)
7. Login User/Owner

note: Everytime do no create a new Security group. Use the existing group and update accordingly.

In advance setting there is User data - optional
    here you can type the commands which needs to executed as the machine starts so the commands will be executed accordingly.


## How to launch Webhosting
```
1. Install apache tomcat server on the EC2 machine
2. Steps to install- httpd(apache tomcat) 
    sudo dnf update
    sudo dnf install httpd -y
    sudo systemctl start httpd 
    sudo systemctl enable httpd
    sudo systemctl status httpd
3. wget <url.zipfile> - you can get this url for any free website templates
4. The zip folder will be downloaded and will be present in the home directory we need to move
that to /var/www/html/ path 
5. cp -r <directoryname>/*  /var/www/html/ - This command will copy the files inside the directory
but not the folder. If we want to copy whole folder then we just cannot give the Ip address but also need to provide the folder name so better copy just the files. 
6. The file contents will be copied and if you check the IP address in the browser the website will be launched.
```