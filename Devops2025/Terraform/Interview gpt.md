Here’s a comprehensive list of **Terraform interview questions**, organized from **basic → intermediate → advanced → scenario-based**, with a mix of conceptual, practical, and scenario questions you might encounter:

---

## **Basic Terraform Questions**

1. What is Terraform, and how is it different from configuration management tools like Ansible or Chef?
2. Explain the purpose of **.tf** files in Terraform.
3. What are **Providers** in Terraform? Give some examples.
4. What are **Resources** in Terraform?
5. What is the purpose of **terraform init**?
6. What does **terraform plan** do?
7. What is **terraform apply**, and how does it work?
8. Explain **terraform destroy**.
9. What is **state file (.tfstate)**? Why is it important?
10. What is **terraform fmt** and **terraform validate**?

---

## **Intermediate Terraform Questions**

1. What are **variables** in Terraform? Explain types and defaults.
2. Difference between **local variables** and **input variables**.
3. Explain **outputs** in Terraform.
4. What is a **Terraform Module**? Why is it useful?
5. Difference between **explicit dependencies** and **implicit dependencies**.
6. What is the **Terraform backend**, and why do we use it?
7. What is **remote state**? Explain S3 backend usage.
8. Difference between **terraform refresh** and **terraform plan**.
9. How do you **import existing resources** into Terraform?
10. What are **Terraform workspaces**, and why would you use them?

---

## **Advanced Terraform Questions**

1. What is **Terraform Cloud** and **Terraform Enterprise**?
2. How do **provisioners** work? Give examples of when to use them.
3. How does **Terraform handle resource dependencies**?
4. Explain **lifecycle blocks** (`create_before_destroy`, `prevent_destroy`).
5. What are **data sources** in Terraform?
6. How do you **handle secrets** in Terraform?
7. What is **Terraform Drift**, and how do you detect/fix it?
8. Difference between **for_each** and **count**.
9. What are **dynamic blocks** in Terraform?
10. How does **Terraform state locking** work?

---

## **Scenario-Based Terraform Questions**

1. Your S3 bucket is managed by Terraform, but someone manually deleted it in AWS. What happens when you run `terraform apply`? How do you fix it?
2. You need to deploy the same infrastructure in **dev, test, and prod**. How will you organize your Terraform code?
3. You have multiple teams working on the same Terraform codebase. How will you manage state files safely?
4. You want to create an **EC2 instance with a dynamic number of EBS volumes** based on environment. How would you do it?
5. You applied a Terraform configuration, and one of the resources failed midway. How do you recover?
6. Your infrastructure is growing, and Terraform apply is taking too long. How would you optimize it?
7. You need to **import an existing VPC and its resources** into Terraform without downtime. How do you do it?
8. A colleague manually modified a resource in AWS. How will you make Terraform aware of the change without destroying the resource?
9. How do you **handle sensitive data** like DB passwords or API keys in Terraform?
10. How do you implement **blue/green deployment** using Terraform for EC2 instances or containers?

---

## **Extra Tips for Interviews**

* Always mention **best practices**: using modules, version control, remote backend, workspaces for environments.
* Be ready to **write simple HCL snippets** on whiteboard or IDE.
* Understand **state management and locking**, as this is a common scenario question.
* Be prepared for **AWS + Terraform** integration questions, e.g., creating VPC, EC2, RDS, IAM roles.

---

If you want, I can also make a **ready-to-use table of 50+ Terraform questions with answers** for **basic → advanced → scenarios**, so you can revise before interviews in a structured way.

Do you want me to prepare that?
