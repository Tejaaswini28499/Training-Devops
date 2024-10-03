## Creating a Target Group and then LB

Before creating the LB we need to create a Target groups
While creating the Target groups choose a Target type(Instance,Lambda or IP)
Give a Target Group Name
The Protocal Port should be 80(Note: Tried with 443 but it's not working)
IP address type- IPV4
Protocal version - HTTP1    
health check HTTP - As the IP address launch in HTTP we need to provide the health check in HTTP only
Select the registered Instance for a Target group and mention the port as 80 and "Include as Pending below" this is a Mandatory step then only you can include the Instances 
Note: For Target group the Instance can be anywhere like one in HYB and another in Mumbai but for volumes it should be in the same region as the Instance.
Then create a Target Group.

## Create a LB
create a Load balancer
select the type- Application Load balancer
Give the LB name 
Scheme internet facing
IPv4
vpc- given as default
select all 3 availability zones
select the security group 
Select the listerner port- HTTP:80 and select the created Target Group
create a lb

now load the DNS link in browser with "http://_____" wait for few minutes for Target group to be healthy and active then it will load the website best on the fashion which is given 
eg: roundrobbin and other two, you can change this settings once you generated the Target group and then edit you can edit the settings.
