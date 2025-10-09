Let’s clear this up 👇

In **Terraform**, two separate mechanisms often get confused:

| Purpose             | File / Resource       | Description                                                                                     |
| ------------------- | --------------------- | ----------------------------------------------------------------------------------------------- |
| **Dependency lock** | `.terraform.lock.hcl` | Ensures the same Terraform **provider versions** are used consistently.                         |
| **State locking**   | **DynamoDB table**    | Prevents **simultaneous writes** to the Terraform **state file** stored in S3 (remote backend). |

So, when you say *“Terraform lockfile with DynamoDB”*, you are most likely referring to **state locking using DynamoDB** (not the `.terraform.lock.hcl` file).

Let’s go step-by-step 👇

---

### 🧱 1. Why We Use DynamoDB for Terraform Locking

When multiple users or CI/CD pipelines run `terraform apply` on the same S3 backend, it can corrupt the state file.
DynamoDB is used to **lock** the state so only one operation runs at a time.

---

### ⚙️ 2. Typical Backend Configuration (S3 + DynamoDB)

Create a file `backend.tf` (or include in your main configuration):

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state-bucket"
    key            = "envs/dev/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-lock-table"
    encrypt        = true
  }
}
```

---

### 🪣 3. Create the S3 Bucket (for state)

You can create it manually or via Terraform (but usually you do this once manually):

```bash
aws s3 mb s3://my-terraform-state-bucket --region ap-south-1
aws s3api put-bucket-versioning --bucket my-terraform-state-bucket --versioning-configuration Status=Enabled
```

Versioning is recommended for rollback safety.

---

### 🧩 4. Create the DynamoDB Table (for locking)

```bash
aws dynamodb create-table \
  --table-name terraform-lock-table \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region ap-south-1
```

---

### 🧰 5. How It Works

* When you run `terraform apply`, Terraform writes a lock item in DynamoDB (LockID = state file path).
* While this lock exists, no other apply can proceed.
* Once apply completes (or fails), the lock is released.

You’ll see messages like:

```
Acquiring state lock. This may take a few moments...
```

If you need to manually remove a stuck lock:

```bash
aws dynamodb delete-item \
  --table-name terraform-lock-table \
  --key '{"LockID": {"S": "envs/dev/terraform.tfstate-md5hash"}}'
```

---

### 🧩 6. Difference Between `.terraform.lock.hcl` and DynamoDB Lock

| File / Resource       | Purpose                                                |
| --------------------- | ------------------------------------------------------ |
| `.terraform.lock.hcl` | Locks **provider plugin versions** (inside your repo). |
| `DynamoDB`            | Locks **Terraform state** (in remote backend).         |

They serve **different locking purposes**.

---

Would you like me to show an example of **creating the S3 + DynamoDB setup entirely via Terraform code**, so you don’t need to do any manual AWS CLI steps?
