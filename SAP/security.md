Jenkins, sonar, checkmarxOne, codeql, Blackduck cloudfoundry deployment  
GA, docker, k8
release pipeline fails what will they do - fa/rel fails

1. sonar: helps you with the codebase review and it scans the code to review the potential issues, providing the feedback that may need much attention
its helps you in detecting bugs(logical error), code smells(at present its not an error but in future it may leads to an error), helps to check with security weakness also. it also does 
static code analysis(just by seeing the syntax, structure will identify error) and 
dynamic code analysis(while running the code it will detect runtime issues, memory leaks, performance bottle necks)


2. checkmarxOne(SAST/DAST):
SAST(Static Application Security Testing): helps to analyse appln source code, binary code, bytecode to identify the security vulnerablity in early development stages allowing developers to fix this issue before it is complied and deployed 

DAST: test the application from outside by interacting with attacker sending various input and observing who the aplln reacts 

This helps organizations shift security left, meaning they can address security issues earlier in the SDLC, reducing the risk of deploying vulnerable software and lowering the cost of fixing issues


configure of checkmarx:
need to click on onboarding link 
create the application ask the application name with dev 
create the service account and ask for there DL and service account you can give an org name 
send the preset document and ask dev to choose the preset value (Preset Reference - Security Testing Documentation)
save the generate token service account id and application name is vault like given below 
add the configuration in config.yaml file and run the project will be created 



| Purpose          | **SonarQube**                 | **Checkmarx**                    |
| ---------------- | ----------------------------- | -------------------------------- |
| **Main goal**    | Code quality + light security | Deep security & compliance       |
| **Users**        | Developers                    | Security / DevSecOps teams       |
| **Integration**  | GitHub, Jenkins, PR checks    | Security gates, compliance scans |
| **Scan speed**   | Fast                          | Slower (deeper analysis)         |
| **Depth**        | Surface-level                 | Deep-level, data flow-based      |
| **Cost**         | Free or low                   | Enterprise-grade (licensed)      |
| **Output style** | Developer-friendly            | Security-risk focused            |


✅ In short:

SonarQube = Developer-focused, for code quality & basic security

Checkmarx = Security-focused, for deep vulnerability analysis

Using both = Clean code + Secure code 💪


3. GitHub Advanced Security (GHAS): is a suite of security tools made by GitHub that integrate into the GitHub portal. The suite has three main parts:

Code scanning: Includes the CodeQL tool for static application security testing (SAST)
Dependency scanning: Includes tools such as Dependabot for managing known vulnerabilities in OSS dependencies
Secret scanning: Includes tools for preventing the leaking of secret tokens into repositories


4. BlackDuck: helps you to find any vulnerabilities in your opensource that you use in your project. It helps in checking license helps you to avoid legal issues, security issues in open source, tracking the components so you know what's there and can update it when needed. In short, Black Duck makes sure you are using open-source software safely and legally. 


| Feature       | **SAST**                            | **Black Duck (SCA)**                        |
| ------------- | ----------------------------------- | ------------------------------------------- |
| **Focus**     | Your own source code                | Open-source & third-party libraries         |
| **Type**      | Static Application Security Testing | Software Composition Analysis               |
| **Scans**     | Source code                         | Dependency packages (Maven, npm, pip, etc.) |
| **Detects**   | Code-level bugs & security flaws    | Known CVEs and license risks                |
| **When used** | During code/build phase             | During dependency management/build          |
| **Examples**  | SonarQube, Checkmarx, Fortify       | Black Duck, Snyk, WhiteSource               |
| **Output**    | Security issues in your code        | Vulnerable or non-compliant libraries       |


5.PPMS:

---

## 🧩 What is **PPMS** in SAP?

> **PPMS (Product and Process Management System)** is an **SAP internal tool** that keeps track of all **software components, versions, and open-source libraries (FOSS)** used in SAP products.

It’s basically a **compliance database** where SAP teams must **declare what open-source and third-party software** they use — to ensure **legal and security compliance** before delivery.

---

### 🧠 In simple English:

> Think of **PPMS** as SAP’s **official record-keeping system** for:
>
> * what code you built,
> * what open-source libraries (OSS/FOSS) you included,
> * and whether those are legally and securely approved.

---

### ⚙️ Example Scenario:

Let’s say your SAP project uses:

* Java Spring Boot (open-source)
* Log4j (open-source)
* Jackson JSON (open-source)

When you **build and deliver** this product, SAP requires:

1. You **scan your code** using tools like **Black Duck** or **WhiteSource**
   → These tools find all OSS libraries.
2. The **PPMS step** compares those libraries against what’s declared in **PPMS**.
3. If you forgot to declare some OSS in PPMS → the step **fails** (non-compliant).
4. If automatic upload is enabled → it **updates PPMS automatically**.

So, PPMS ensures **your software delivery matches SAP’s compliance standards** for open-source usage.

---

### 🏛️ Why SAP needs PPMS

* To make sure every SAP product:

  * ✅ Legally declares all 3rd-party or open-source code
  * ✅ Is licensed correctly (MIT, Apache, GPL, etc.)
  * ✅ Has no unapproved or risky dependencies
  * ✅ Passes audits and customer deliveries safely

---

### 🔄 How PPMS connects to DevOps (Piper step)

* You use **SAP Project Piper step → `sapCheckPPMSCompliance`**
* It automatically:

  * Fetches scan results from **Black Duck / WhiteSource**
  * Fetches declared OSS list from **PPMS**
  * Compares both (checks for missing or extra items)
  * Creates or updates **build versions (BV)** and **software component versions (SCV)** in PPMS

---

### ✅ In short:

| Term                | Meaning                                                                       |
| ------------------- | ----------------------------------------------------------------------------- |
| **PPMS**            | SAP’s Product & Process Management System                                     |
| **Purpose**         | Ensures all OSS/FOSS and 3rd-party components are declared legally & securely |
| **Used by**         | All SAP teams delivering software                                             |
| **Connected tools** | Black Duck, WhiteSource, Piper                                                |
| **Main step**       | `sapCheckPPMSCompliance`                                                      |
| **Output**          | Compliance report + optional automatic update in PPMS                         |

---

### 🧩 Quick Analogy:

> 🔍 **Black Duck / WhiteSource** = Detect what open-source you used
> 🏛️ **PPMS** = Official SAP registry to declare those components

---



