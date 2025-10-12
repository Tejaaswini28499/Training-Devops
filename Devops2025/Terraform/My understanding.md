Providers 

Terraform variables: instead of hardcoding the values we can write separate vaiable.tf and read values from those in main.tf file
note: defining variable will be done in variable.tf values are red from terraformtf.vars. tf.vars is used only for Input variables for Output variables we need to create output.tf
there are two types of Variable 
1. Input variable - pass some information to tf 
2.output variable - print particular value in output


if you want to completely parameterize, some one want t2.mirco and other wants t1.medium so if these is the case we can use tf.vars file if you have different tf.vars file like dev.tfvars, prod.tfvars, test.tfvars then while terraform apply we need to provide which tf.vars to be the configuration applied on 

Sensitive information can we stored in tf.vars

Conditions
condition ? true_val : false_val

Built-in functions for terraform(not used much) some examples below:
1. length
2. map

Terraform Modules: 

drawbacks of Statefile:
You cannot store the sensitive information here
if you are doing in version control system then there is a compro in your security and
everytime when you make any code changes in your local the statefile needs to be updated accordingly if not the configuration are messed up

this can be fixed using remote backend (s3, terraform cloud, Azure storage)

Remote backend: If you use your remote backend as s3 bucket it will host the statefile
1. we can completely restrict the access to s3 (no public access)
2. No making changes with the statefile when terraform apply is done the statefile will get automatically updateded

Explain to interviwer
we are a Devops group of 5-6 and we have the code in GitHub and whenever there is a change the repo will be cloned and they make changes in there repo and do terraform apply and the statefile from the remote backend will get automatically. When the PR is raised to the main branch it would get updated and the statefile in the remote backend will also be updated 

Step-by-step explaination 
1. If there is no s3 bucket we can create separate module and pass that in root main.tf
2. create a backend.tf file and pass the required parameters here eg: backend:s3 bucketname, region key(optional)
3. terraform apply the statefile will be created in the s3 bucket 

 
terraform Lockfile-  using dynamo db we can lock the file not in the local but in the cloud 
you need dynamo db to be created and after creation pass the dynamo db name in your backend.tf and do terraform apply 

Provisioners: local.exec and remote.exec

multiple varfiles like dev.tfavrs stage.tfvars if you use such tfvars the statefile will not create a required resources it would just update the existing statefile 
but for diff environment we need different instances so for all this there will be only one statefile created and it will just update to overcome this problem we came up with workspace concept 

terraform workspaces: here you need to create how many workspace you need and for each and every workspace there will be parallel statefile created

command to create the folder: terraform workspace new 'name' - name came be dev, stage prod
If we need to go inside  the dev, stage, prod: terraform workspace select 'name'


Terraform Vault Integration | Secrets Management
Installation of Vault: 
1. take any machine ubuntu or Linux any 
2. Install Hashicorp package manager and then install vault if you dont install package manager you cannot install vault
3. execute the command called vault the if its installed it would describe all the things
4. We need to start the vault server, it comes in 2 diff types one dev server and another production server 
5. when you install the vault with command (vault server -dev -dev-listen-address="0.0.0.0.:8200") you would get the an address to export your vault also the unseal key and root token
6. in security group expose 8200 with 0.0.0.0 
7. with the Instance Ip and 8200 you will get the url of the vault 
8. in Vault method you can give token there are many like LDAP, OUTH you can give Token and provide the token key here
9. secret engine - Different types of secret you can create in Vault 
10. create a KV secret and give a path 
11. to give the access to other we need to create approle id 
12. you cannot create any roles using UI you need to create via CLI
13. before roles you need to create policies
14. create Approle id and approle secretid
15. create a vault provider and mount in mount provide the path of the mount and name, which is the secret name given inside the mount eg: detect is path and token is the secret



note: If you need to create a resource go to resource in hashicorp document and resource we you want to read the data then go to data resource in hashicorp documnet

Interview scenario based question:

1. what if there was already a Infra setup done and you need to write terraform for that how would you do?- Terraform Migration 
will do using terraform import command 

step by step: 
terraform init
Create a file provider.tf: aws, azure 
Define resource placeholders eg: esource "aws_instance" "my_ec2" {}
Use terraform import to generate the state file eg:terraform import aws_instance.my_ec2 i-0123456789abcdef0 Verify your generated state :terraform state list
Write matching .tf configuration: Now Terraform knows what resources exist, but your .tf files are empty.
You need to recreate the resource configuration in code form
Validate alignment: terraform plan If everything matches, you’ll see:No changes. Infrastructure is up-to-date.
Move to remote backend (optional but recommended): terraform init -migrate-state



What happens internally:

Terraform connects to AWS.

Reads metadata for those resources (e.g., AMI, subnet, tags).

Creates a terraform.tfstate file locally if it doesn’t exist.

Writes the resource info inside that state.

Result:
A new file terraform.tfstate is created automatically.


2. Terraform drift detection 


