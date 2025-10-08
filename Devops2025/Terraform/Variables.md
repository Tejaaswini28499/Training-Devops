In **Terraform**, **variables** are used to **make your configuration dynamic, reusable, and flexible**.
They allow you to **parameterize** your `.tf` files instead of hardcoding values.

Let’s break it down 👇

---

## 🧩 Types of Variables in Terraform

### 1. **Input Variables (`variable` block)**

Used to **pass values into modules or root configurations**.

**Syntax:**

```hcl
variable "region" {
  description = "The AWS region to deploy resources"
  type        = string
  default     = "ap-south-1"
}
```

You can access it like this:

```hcl
provider "aws" {
  region = var.region
}
```

**Ways to assign values:**

1. **Default value** – set inside the variable block.
2. **Terraform CLI prompt** – Terraform will ask if not provided.
3. **`terraform.tfvars` or `.auto.tfvars` files**

   ```hcl
   region = "us-east-1"
   ```
4. **Command-line flags**

   ```bash
   terraform apply -var="region=us-west-2"
   ```
5. **Environment variables**

   ```bash
   export TF_VAR_region="us-west-1"
   ```

---

### 2. **Output Variables (`output` block)**

Used to **display values after Terraform apply** (like IP addresses, IDs, etc.).

**Example:**

```hcl
output "instance_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.my_ec2.public_ip
}
```

---

### 3. **Local Variables (`locals` block)**

Used to **simplify expressions** or avoid repetition inside your code.

**Example:**

```hcl
locals {
  common_tags = {
    Project = "Demo"
    Owner   = "Tejaaswini"
  }
}

resource "aws_s3_bucket" "example" {
  bucket = "demo-bucket-123"
  tags   = local.common_tags
}
```

---

## 🔢 Common Variable Types

| Type     | Example                                  | Description           |
| -------- | ---------------------------------------- | --------------------- |
| `string` | `"hello"`                                | Text value            |
| `number` | `10`                                     | Numeric value         |
| `bool`   | `true`                                   | True/False            |
| `list`   | `["a", "b", "c"]`                        | Ordered sequence      |
| `map`    | `{ env = "prod", region = "us-east-1" }` | Key-value pairs       |
| `object` | `{ name = string, age = number }`        | Custom structure      |
| `tuple`  | `[string, number, bool]`                 | Fixed-length sequence |

---

## 🧠 Example: Using Variables in a Complete Terraform Config

**`main.tf`**

```hcl
variable "instance_type" {
  type    = string
  default = "t2.micro"
}

provider "aws" {
  region = var.region
}

resource "aws_instance" "example" {
  ami           = var.ami_id
  instance_type = var.instance_type
}
```

**`terraform.tfvars`**

```hcl
region = "ap-south-1"
ami_id = "ami-0abcdef1234567890"
```

Run:

```bash
terraform apply
```

Terraform automatically reads `terraform.tfvars`.

---

## 💡 Tip

* Use `terraform.tfvars` for **project-specific** values.
* Use `variables.tf` for **declaring** all variables.
* Use `outputs.tf` for **exporting** results.

---

Would you like me to explain **how variable precedence works** (i.e., which value wins if multiple sources define the same variable)?

My Understanding:
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
