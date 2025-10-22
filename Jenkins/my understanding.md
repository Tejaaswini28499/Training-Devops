Installation of Jenkins 
Installation of Docker 
Installtion of kubectl
Installtion of terraform 
maven version 



Jenkins - 
configure systems - is where you will configure other server url 
global configuration we configure the JAVA jdk version , Maven, Ant , sonar tools configuration will be done here
plugins - want to use any tech we need to install those plugins
Node is like a machine on which you execute our code, if you want new node you can configure that also


What is Jenkins
Jenkins is an open-source automation server used mainly for Continuous Integration (CI) and Continuous Delivery/Deployment (CD).

In simple words — Jenkins helps automate the process of building, testing, and deploying applications so developers don’t have to do these steps manually every time code changes.

| Stage                           | Description                                                           | Example                               |
| ------------------------------- | --------------------------------------------------------------------- | ------------------------------------- |
| **Continuous Integration (CI)** | Automatically build and test code whenever developers push changes    | Jenkins builds a Java app using Maven |
| **Continuous Delivery (CD)**    | Automatically prepare and deploy tested code to staging or production | Jenkins deploys to Kubernetes cluster |

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean compile -DskipTests=true'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}



diff btw continous delivery and continous deployment 
Great question 👏 — this is one of the most common interview topics in DevOps!

Let’s break it down clearly 👇

---

### 🔹 **Continuous Delivery (CD)**

**Goal:**
Automatically build, test, and prepare code for release — but **deployment to production is a manual decision**.

✅ Code is always **ready to deploy**,
❌ But an engineer or manager **approves and triggers** the deployment.

**Example:**

* Jenkins automatically builds and tests your app.
* It deploys the latest version to a **staging environment**.
* A release manager reviews it and **clicks “Deploy to Production”** manually.

**So:**

> In Continuous Delivery → The code is ready for production anytime, but the release is **manual**.

---

### 🔹 **Continuous Deployment**

**Goal:**
Automatically build, test, and **deploy code to production** — with **no manual approval** needed.

✅ Every change that passes tests automatically goes live.

**Example:**

* A developer pushes code → Jenkins builds → tests pass → app is automatically deployed to production.

**So:**

> In Continuous Deployment → The release to production is **fully automated**.

---

### 🔹 Comparison Table

| Feature                   | Continuous Delivery                | Continuous Deployment                            |
| ------------------------- | ---------------------------------- | ------------------------------------------------ |
| **Automation Level**      | Build, test, staging automated     | Build, test, **and production deploy** automated |
| **Production Deployment** | Manual approval required           | Fully automatic                                  |
| **Risk**                  | Lower (human review before deploy) | Higher (needs strong test automation)            |
| **Speed**                 | Slightly slower                    | Fastest — every commit can go live               |
| **Example Tools**         | Jenkins, GitHub Actions, Argo CD   | Jenkins, Spinnaker, Argo CD, FluxCD              |

---

### 🔹 Simple Analogy

Imagine a **restaurant kitchen** 🍳

* **Continuous Delivery:** The chef prepares the dish and keeps it ready — waiter decides when to serve.
* **Continuous Deployment:** As soon as the dish is ready, it’s automatically served to the customer — no waiter approval.

---

What are the advantages of using Jenkins?
“Jenkins automates CI/CD, integrates easily with many tools, supports distributed builds, and is open-source with strong community support — helping deliver code faster and more reliably.”

what are the types of Jenkins pipeline
Excellent question 👏 — this one is **frequently asked in Jenkins/DevOps interviews**!

Let’s go step by step 👇

---

## 🔹 **Types of Jenkins Pipelines**

Jenkins supports **three main types** of pipelines:

| Type                                         | Description                                                                                                  | Defined Using                                    |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| **1. Declarative Pipeline**                  | A simpler and more structured syntax. It uses predefined blocks like `pipeline`, `agent`, `stages`, `steps`. | `Jenkinsfile` (Groovy syntax but easier to read) |
| **2. Scripted Pipeline**                     | More powerful and flexible; written entirely in Groovy code. Used when you need complex logic.               | `Jenkinsfile` (pure Groovy script)               |
| **3. Declarative + Scripted Mixed Pipeline** | Combines both styles — mostly declarative with small scripted sections where extra control is needed.        | `Jenkinsfile`                                    |

---

### 🔸 1️⃣ **Declarative Pipeline (Most Common)**

**Example:**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean compile -DskipTests=true'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}
```

✅ **Features:**

* Simple syntax (easy to read/write)
* Built-in error handling (`post` block for success/failure)
* Best for most CI/CD pipelines

---

### 🔸 2️⃣ **Scripted Pipeline**

**Example:**

```groovy
node {
    stage('Build') {
        sh 'mvn clean compile -DskipTests=true'
    }
    stage('Test') {
        sh 'mvn test'
    }
    stage('Deploy') {
        sh 'kubectl apply -f deployment.yaml'
    }
}
```

✅ **Features:**

* Fully written in Groovy — more flexible and programmable
* Suitable for complex logic (loops, conditions, shared libraries)
* Harder to read but powerful

---

### 🔸 3️⃣ **Declarative + Scripted Mixed**

**Example:**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Scripted block inside Declarative
                    def version = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    echo "Building version ${version}"
                }
            }
        }
    }
}
```

✅ **Features:**

* Declarative for readability
* Scripted for flexibility when needed

---

### 🔸 Bonus (Conceptual Types)

Sometimes people also mention **other types** based on usage:

| Concept                     | Meaning                                                                    |
| --------------------------- | -------------------------------------------------------------------------- |
| **Multibranch Pipeline**    | Automatically creates pipelines for each Git branch.                       |
| **Pipeline as Code**        | Pipeline defined in a `Jenkinsfile` inside source control (best practice). |
| **Shared Library Pipeline** | Reusable pipeline logic shared across multiple projects.                   |

---

### 💡 Interview Tip:

If the interviewer asks:

> “What type of pipeline do you use?”

You can say:

> “We mainly use **Declarative Pipelines** defined in `.pipeline/config.yml` or `Jenkinsfile`.
> They’re cleaner, easier to maintain, and integrate well with SAP Project Piper for automated CI/CD.”

---
What is a Jenkinsfile? Why is it important?
A Jenkinsfile tells Jenkins what to do when new code is pushed — step by step.
“A Jenkinsfile defines the CI/CD pipeline as code.
It ensures version control, consistency, and automation — making pipelines easy to reproduce, review, and modify.”

what are plugins in Jenkins and why its important
Perfect 👏 — Jenkins plugins are **a very common interview topic**. Let’s break it down clearly.

---

## 🔹 **What are Jenkins Plugins?**

**Plugins** in Jenkins are **add-ons or extensions** that enhance Jenkins’ functionality.

> They allow Jenkins to integrate with other tools, add new features, or customize workflows.

Without plugins, Jenkins is a **barebones automation server**, and you can’t connect it to version control, build tools, testing tools, or deployment platforms.

---

### 🔹 **Why Plugins are Important**

* Integrate Jenkins with **Git, GitHub, Bitbucket, SVN**.
* Connect to **build tools** like Maven, Gradle, npm.
* Add **notifications** via Slack, email, MS Teams.
* Enable **deployment** to Docker, Kubernetes, AWS, Azure, etc.
* Extend functionality (e.g., monitoring, reporting, pipelines).

In short: **Plugins make Jenkins a powerful CI/CD orchestration tool.** ✅

---

### 🔹 **Commonly Used Jenkins Plugins**

| Plugin Name                     | Purpose                                          |
| ------------------------------- | ------------------------------------------------ |
| **Git Plugin**                  | Connect Jenkins to Git repositories.             |
| **GitHub Branch Source Plugin** | For multibranch pipelines with GitHub.           |
| **Pipeline Plugin**             | Enables Jenkins Pipeline functionality.          |
| **Maven Integration Plugin**    | Run Maven builds easily.                         |
| **Docker Plugin**               | Build and manage Docker containers.              |
| **Kubernetes Plugin**           | Deploy builds to Kubernetes clusters.            |
| **Slack Notification Plugin**   | Send build status notifications to Slack.        |
| **Email Extension Plugin**      | Send custom email alerts for builds.             |
| **JUnit Plugin**                | Publish test results and reports.                |
| **Credentials Plugin**          | Manage secrets like passwords, tokens, SSH keys. |
| **Blue Ocean Plugin**           | Modern UI for Jenkins pipelines visualization.   |

---

### 🔹 **Interview Tip**

If asked *“Why plugins?”* → you can say:

> “Plugins extend Jenkins’ capabilities, allowing it to integrate with tools for version control, build, test, deployment, notifications, and reporting, making it highly flexible for CI/CD pipelines.”

---

What is the use of mvn clean install or mvn clean compile in Jenkins?
| Command                              | What it does                                                                     | Use in Jenkins                                      |
| ------------------------------------ | -------------------------------------------------------------------------------- | --------------------------------------------------- |
| `mvn clean compile`                  | Deletes old build + compiles code                                                | Check for compilation errors                        |
| `mvn clean install`                  | Deletes old build + compiles + runs tests + packages + installs artifact locally | Full build for testing or deployment                |
| `mvn clean install -DskipTests=true` | Full build but **skips tests**                                                   | Fast build in early stages or non-prod environments |


can we use both clean and install together??

“We can use mvn clean compile first to quickly catch compilation errors, then mvn clean install to build, test, and package the artifact. This approach gives faster feedback in CI/CD pipelines.”

pipeline {
    agent any
    stages {
        stage('Compile') {
            steps {
                sh 'mvn clean compile'
            }
        }
        stage('Build & Test') {
            steps {
                sh 'mvn clean install'
            }
        }
    }
}



what are /target folder 
Perfect — this is a common Maven/Jenkins question. Let’s break it down clearly 👇

---

## 🔹 **What is the `/target` folder?**

In a **Maven project**, the `/target` folder is the **default directory where Maven stores all the build outputs**.

It is **automatically created** when you run Maven commands like `mvn compile`, `mvn package`, or `mvn install`.

---

### 🔹 **What goes inside `/target`?**

| Item                      | Description                                                                     |
| ------------------------- | ------------------------------------------------------------------------------- |
| **Compiled classes**      | `.class` files generated from your `.java` source files (from `src/main/java`). |
| **Packaged artifacts**    | JAR, WAR, or EAR files created by Maven during `mvn package` or `mvn install`.  |
| **Test reports**          | Results of unit tests (e.g., from `mvn test`).                                  |
| **Temporary build files** | Anything Maven needs during the build, like generated sources.                  |

---

### 🔹 **Example**

If your project is named `MyApp`:

```bash
MyApp/
 ├── src/
 │    ├── main/
 │    └── test/
 └── target/
       ├── classes/          # compiled .class files
       ├── test-classes/     # compiled test classes
       ├── MyApp-1.0.jar     # packaged artifact
       └── surefire-reports/ # test results
```

---

### 🔹 **Relation with Jenkins**

* When Jenkins runs `mvn clean compile` → `/target` is **created with compiled classes**.
* When Jenkins runs `mvn clean install` → `/target` contains **compiled classes + packaged artifact + test reports**.
* Usually, Jenkins **archives the artifacts from `/target`** for deployment or further stages.

---

### 🔹 **Why `mvn clean` deletes `/target`**

* `clean` ensures that **old artifacts don’t interfere** with the new build.
* It deletes `/target` before a fresh build.

---

💡 **Interview Tip:**

> “In a Maven project, `/target` is where all compiled classes, packaged artifacts, and test reports are stored. Jenkins uses it to get the build outputs and artifacts for deployment.”

---

## 🔹 **Jenkins Master-Slave Architecture** (now called **Controller-Agent**)

Jenkins uses a **distributed architecture** to **run builds efficiently**.

* **Master (Controller)** → Manages Jenkins.
* **Slave (Agent)** → Executes the jobs/builds assigned by the Master.

---

### 🔸 **1️⃣ Jenkins Master (Controller)**

**Responsibilities:**

* Hosts the **Jenkins web UI**.
* Stores **configuration, job definitions, plugins, and build history**.
* Schedules and **assigns jobs to agents**.
* Monitors build progress and reports results.

**Analogy:** Master = **Traffic Manager** 🚦

---

### 🔸 **2️⃣ Jenkins Slave (Agent)**

**Responsibilities:**

* Receives jobs from Master.
* Executes the **build, test, and deployment steps**.
* Sends build results and logs back to the Master.

**Features:**

* Can run on **different OS** (Linux, Windows, macOS).
* Can be **ephemeral** (spin up in cloud/docker for temporary jobs).
* Multiple agents can run in parallel → **faster builds**.

**Analogy:** Slave = **Worker** 👷

---

### 🔹 **Why this architecture is used**

1. **Distributed Builds:** Multiple jobs can run simultaneously on different agents.
2. **Scalability:** Add more agents as project size or team grows.
3. **OS Flexibility:** Agents can run on different OS or environments.
4. **Resource Optimization:** Heavy builds can run on powerful machines without affecting Master.

---

### 🔹 **Diagram**

```
           +--------------------+
           |    Jenkins Master   |
           | (Controller)       |
           | - UI               |
           | - Job scheduling   |
           | - Config/Plugins   |
           +----------+---------+
                      |
      +---------------+-----------------+
      |               |                 |
+-------------+  +-------------+  +-------------+
| Jenkins Agent|  | Jenkins Agent|  | Jenkins Agent|
|   (Linux)   |  |   (Windows)  |  |  (Docker)    |
+-------------+  +-------------+  +-------------+
```

---

### 🔹 **How Jobs Flow**

1. Developer pushes code → Master detects change.
2. Master decides which **agent** to run the job on.
3. Agent executes **build/test/deploy** steps.
4. Agent sends **results/logs** back to Master.
5. Master updates UI and notifies stakeholders.

---

### 🔹 **Interview Tip**

If asked *“Difference between Master-Slave and Controller-Agent?”* → you can say:

> “Controller-Agent is the modern terminology of Master-Slave. The Controller manages Jenkins, schedules jobs, and handles configuration. Agents execute jobs and send results back. This architecture allows **distributed, scalable, and parallel builds**.”

---

What is a “post” block in a declarative pipeline?
“A post block in a declarative pipeline defines actions that run after a stage or pipeline completes, such as sending notifications, cleaning up, or archiving artifacts.
It helps ensure important tasks run regardless of build success or failure.”

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
    }

    post {
        always {
            echo 'This runs always, regardless of success or failure'
        }
        success {
            echo 'This runs only if the pipeline succeeds'
        }
        failure {
            echo 'This runs only if the pipeline fails'
        }
        unstable {
            echo 'This runs if the pipeline is unstable (e.g., test failures)'
        }
        changed {
            echo 'This runs if the build status has changed compared to the previous build'
        }
    }
}

How do you use environment variables in Jenkins pipelines?

What is the use of the stash and unstash steps in pipelines?

What are Jenkins Shared Libraries?

Common Groovy scripts reused across pipelines.

How do you handle parallel execution in Jenkins?
