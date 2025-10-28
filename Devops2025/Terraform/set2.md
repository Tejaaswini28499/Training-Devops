Here’s a **complete list of Terraform interview questions** — from **basic to advanced**, suitable for a **DevOps Engineer with 5 years of experience** like you 👩‍💻.

---

## 🟢 **Basic Terraform Interview Questions**

1. **What is Terraform?**
   → It’s an open-source Infrastructure as Code (IaC) tool by HashiCorp used to provision and manage infrastructure across multiple cloud providers.

2. **Why do we use Terraform instead of CloudFormation/Ansible?**

   * Cloud-agnostic (works with AWS, Azure, GCP, etc.)
   * Declarative approach (you define *what* you want)
   * State management
   * Immutable infrastructure
   * Reusability with modules

3. **Explain the difference between `terraform apply` and `terraform plan`.**

   * `terraform plan` → shows what will be created/modified/destroyed.
   * `terraform apply` → executes those changes.

4. **What is Terraform state (`terraform.tfstate`)?**

   * A file that keeps track of real-world resources created by Terraform.

5. **What is a provider in Terraform?**

   * Plugin that interacts with APIs of cloud platforms (like `aws`, `azurerm`, `google`).

6. **What are Terraform resources?**

   * Blocks that define infrastructure components like EC2, S3, VPC, etc.

7. **What is a variable in Terraform?**

   * Inputs that make configuration flexible. Defined using `variable` block.

8. **What is an output in Terraform?**

   * Used to display or export values after `apply` (e.g., public IP of EC2).

9. **What is the purpose of `terraform init`?**

   * Initializes a working directory, installs provider plugins.

10. **What is the `.terraform.lock.hcl` file?**

    * Locks provider versions to ensure consistent builds.

---

## 🟡 **Intermediate Terraform Interview Questions**

1. **What is remote backend in Terraform?**

   * Stores state file remotely (e.g., in S3, GCS, or Terraform Cloud) instead of locally for team collaboration.

2. **How do you manage Terraform state in a team environment?**

   * Use **remote backend** (S3 with DynamoDB for state locking).
   * Example:

     ```hcl
     backend "s3" {
       bucket         = "my-terraform-state"
       key            = "prod/terraform.tfstate"
       region         = "us-east-1"
       dynamodb_table = "terraform-lock"
     }
     ```

3. **What is Terraform refresh?**

   * Updates the state file with the latest data from real infrastructure.

4. **What are Terraform modules? Why are they used?**

   * Reusable configurations (like a function).
   * Helps in maintaining DRY (Don’t Repeat Yourself) principles.

5. **What is `terraform import` used for?**

   * Brings existing resources into Terraform management.

6. **What is the difference between `terraform taint` and `terraform destroy`?**

   * `taint` marks a resource for recreation in next apply.
   * `destroy` deletes all resources.

7. **What are data sources in Terraform?**

   * Allow you to fetch existing information (like AMI ID or subnet ID) from your provider.

8. **How do you handle sensitive data in Terraform?**

   * Use `sensitive = true`, environment variables, or secrets managers (AWS Secrets Manager, Vault).

9. **How do you manage dependencies between resources?**

   * Terraform automatically detects dependencies using references (`depends_on` can be used manually).

10. **What is the difference between local and remote-exec provisioners?**

    * `local-exec` → runs commands locally.
    * `remote-exec` → runs commands on the created resource (like SSH into EC2).

---

## 🔵 **Advanced Terraform Interview Questions**

1. **Explain Terraform’s lifecycle meta-arguments.**

   * `create_before_destroy`, `prevent_destroy`, `ignore_changes`.

2. **How do you manage multiple environments (dev, stage, prod)?**

   * Separate workspaces or directories/modules per environment.

3. **What are Terraform Workspaces?**

   * Allow multiple state files for same configuration (used for managing environments).

4. **How do you version control Terraform code?**

   * Store in Git, lock provider versions, use Terraform Cloud or pipelines for automation.

5. **What is the use of `count` and `for_each`?**

   * To create multiple similar resources dynamically.

6. **Difference between `count` and `for_each`?**

   * `count` → index-based, uses numeric indices.
   * `for_each` → key-based, better for map or set inputs.

7. **What happens internally when you run `terraform apply`?**

   * Loads configuration → refreshes state → creates execution plan → applies changes.

8. **How do you handle drift in Terraform?**

   * Run `terraform plan` regularly, use `terraform refresh` or re-apply.

9. **What are Terraform Provisioners? Why should you avoid them?**

   * Used to run scripts on resources.
   * Avoid because they break idempotency; prefer configuration management tools.

10. **How do you perform rollback in Terraform?**

    * Use versioned state files or VCS versioning; Terraform doesn’t have a native rollback.

11. **How do you integrate Terraform with CI/CD (Jenkins/GitHub Actions)?**

    * Run `terraform fmt`, `init`, `validate`, `plan`, and `apply` stages via pipeline.

12. **What are some Terraform best practices?**

    * Keep state remote and locked
    * Use modules
    * Use variables and outputs wisely
    * Pin provider versions
    * Use `terraform fmt` and `validate`

13. **What’s the difference between `terraform destroy -target` and full destroy?**

    * `-target` destroys a specific resource, not the entire infrastructure.

14. **What is Terraform Cloud / Terraform Enterprise?**

    * Managed service for running Terraform with remote state, versioning, policies, and collaboration.

15. **Explain `depends_on` and when you use it explicitly.**

    * Used when Terraform can’t auto-detect dependencies (e.g., null resources, outputs).

---

## 🧠 **Scenario-Based Terraform Interview Questions**

1. Your `terraform apply` failed halfway. How do you recover?

   * Check the state file → fix configuration → run `terraform apply` again.

2. You deleted a resource manually in AWS but Terraform still shows it. What will you do?

   * Run `terraform plan` → re-apply to recreate → or `terraform refresh` to sync state.

3. How would you organize Terraform for a large project with multiple environments and teams?

   * Use modules + workspaces + remote state backend per environment.

4. You need to share outputs (like subnet IDs) between modules. How do you do it?

   * Use `outputs.tf` in one module and data sources to reference in another.

5. How do you manage secrets (like DB passwords) securely in Terraform pipelines?

   * Use encrypted variables, secret managers, or Terraform Cloud variable sets.

---

Would you like me to create a **Terraform Interview Q&A PDF** (with answers explained clearly in short bullet points) — suitable for **DevOps interview preparation (5 years experience)**?
