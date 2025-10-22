Here’s a **comprehensive list of GitHub Actions interview questions** — grouped by **basic, intermediate, advanced, and scenario-based** — perfect for a DevOps engineer like you 👩‍💻.

---

## 🟢 **Basic Level Questions**

1. **What is GitHub Actions?**
2. **What are workflows, jobs, and steps in GitHub Actions?**
3. **Where do you define GitHub Actions workflows?**
   → (Hint: `.github/workflows/` directory)
4. **What is an event in GitHub Actions? Give examples.**
   → (e.g., `push`, `pull_request`, `schedule`, `workflow_dispatch`)
5. **What are runners? What’s the difference between GitHub-hosted and self-hosted runners?**
6. **What are artifacts and how do you upload/download them in workflows?**
7. **Can a workflow trigger another workflow?**
8. **What is the default shell used in GitHub Actions?**
9. **How do you define environment variables in GitHub Actions?**
10. **How do you pass secrets to workflows?**

---

## 🟡 **Intermediate Level Questions**

1. **Explain the difference between `runs-on` and `container` in a workflow.**
2. **How do you reuse workflows?**
   → (Hint: `workflow_call`)
3. **How do you control job dependencies?**
   → (Hint: `needs:` keyword)
4. **What are matrix builds in GitHub Actions?**
   → Example: running tests on multiple OS or Node.js versions.
5. **How do you cache dependencies between workflow runs?**
   → (Hint: `actions/cache`)
6. **Explain how concurrency and cancellation work in GitHub Actions.**
7. **What is the purpose of `if:` condition in steps or jobs?**
8. **How do you handle secrets or sensitive data securely?**
9. **How do you restrict workflows to specific branches or paths?**
10. **How do you schedule workflows to run automatically?**
    → (Hint: `on: schedule` with cron syntax)

---

## 🔵 **Advanced Level Questions**

1. **Explain the difference between `workflow_dispatch`, `repository_dispatch`, and `workflow_call`.**
2. **What are composite actions? When would you create one?**
3. **How do you use `env` vs `vars` vs `secrets` in workflows?**
4. **How can you share actions between repositories?**
5. **Explain how to handle deployment approvals or environments in GitHub Actions.**
6. **How do you debug a failed GitHub Actions run?**
7. **What is `GITHUB_TOKEN`, and how is it different from a PAT (Personal Access Token)?**
8. **How do you trigger workflows from other repositories?**
9. **How can you prevent infinite workflow trigger loops between repositories?**
10. **How can you store and use build artifacts across workflows?**

---

## 🔴 **Scenario-Based Questions**

1. **You have a CI/CD pipeline for a Node.js app. How would you build, test, and deploy it using GitHub Actions?**
2. **How do you ensure a workflow runs only when code is merged into `main`?**
3. **You want to deploy to production only after manual approval — how do you implement that?**
   → (Hint: environments with required reviewers)
4. **Your build takes too long. How would you optimize workflow performance?**
   → (Use caching, reusable workflows, concurrent jobs, etc.)
5. **How do you handle a secret rotation without updating every workflow?**
6. **If one job fails, but you want the rest to continue, how do you configure it?**
   → (Hint: `continue-on-error: true`)
7. **How do you prevent a workflow from running when only README changes?**
   → (Hint: `paths-ignore`)
8. **You have multiple microservices — how do you manage CI/CD for all using GitHub Actions efficiently?**
   → (Monorepo strategy, matrix jobs, reusable workflows)
9. **How would you integrate GitHub Actions with AWS / Azure / GCP for deployments?**
10. **You want to trigger a workflow only when a tag like `v*` is pushed — how do you write that?**

---

## ⚙️ **DevOps-Oriented Questions**

1. **How do you integrate GitHub Actions with Terraform / Docker / Kubernetes?**
2. **How do you store and manage build artifacts between jobs and workflows?**
3. **What are the best practices for writing GitHub Actions workflows for CI/CD?**
4. **Have you ever created a custom GitHub Action? Explain the process.**
5. **How would you handle versioning for GitHub Actions?**
6. **Explain how you can use GitHub Actions for Infrastructure as Code pipelines.**

---

## 🧠 **Bonus Tips for Interviews**

* Be ready to explain **how GitHub Actions compares to Jenkins / GitLab CI / CircleCI.**
* Interviewers love to ask about **security best practices** (secrets, tokens, permissions).
* Keep one or two **real-life examples** from your work — e.g., how you used Actions to deploy to EKS or automate testing.

---

Would you like me to create a **one-page GitHub Actions interview cheat sheet** (with YAML syntax examples + answers)?
That’s great for last-minute revision before interviews.
