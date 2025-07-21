Infrastructure and Architecture
How many master nodes and worker nodes are in your Kubernetes cluster?
What is the total size of your Kubernetes cluster (e.g., number of nodes, memory, CPU)?
Are you using on-premises infrastructure, cloud (AWS, Azure, GCP), or hybrid?
How many regions or data centers are you operating in?
What is the load balancing mechanism in place (e.g., NGINX, HAProxy, cloud-native like ALB/ELB)?
Applications and Services
How many applications are deployed in your production environment?
What types of applications are running (e.g., microservices, monolithic, serverless)?
How many services are running across your clusters?
What percentage of your workloads are stateful vs. stateless?
How many third-party services are integrated into your environment (e.g., monitoring, logging, CI/CD)?
Kubernetes Pods and Workloads
How many pods are currently running in your production cluster?
What is the average number of pods per service or application?
Are you using Horizontal Pod Autoscalers (HPA)? If yes, what triggers scaling (CPU, memory, custom metrics)?
How are namespaces organized in your cluster (e.g., per team, per application)?
Are you using DaemonSets, StatefulSets, or Jobs? How many of each are deployed?
CI/CD Pipelines
How many builds and deployments are executed daily/weekly?
Are you using a single CI/CD pipeline or multiple pipelines for different applications/services?
What tools are used for CI/CD (e.g., Jenkins, GitHub Actions, GitLab CI/CD)?
Do you follow a blue-green deployment or canary deployment strategy?
Monitoring and Logging
What tools do you use for monitoring and logging (e.g., Prometheus, Grafana, ELK, Datadog)?
How do you track pod or application health (e.g., readiness/liveness probes, logging metrics)?
How many alerts are triggered daily/weekly? How are they categorized (critical, warning, info)?
Traffic and User Load
What is the average daily traffic (requests per second) handled by your services?
Are you using an Ingress controller? If yes, how many ingress rules are configured?
How do you handle failover and disaster recovery (e.g., multi-region deployments, backups)?
Security and Compliance
How is authentication and authorization managed (e.g., RBAC, OIDC)?
Are network policies implemented in your cluster? How many are defined?
What security tools are in place (e.g., Falco, Aqua, Trivy)?
Do you use encrypted secrets in your deployments? How many secrets are managed?
General Operations
What is your release cycle (daily, weekly, or bi-weekly)?
How many developers or teams contribute to the infrastructure?
How many incidents or outages do you encounter monthly?
What is the average time to recover (MTTR) during an incident?
These questions provide a detailed overview of the operational scale, infrastructure setup, and management processes in an organization. They can be tailored further based on specific environments or tools in use.









Infrastructure and Architecture
Master and Worker Nodes: 3 master nodes and 50 worker nodes.
Cluster Size: 50 worker nodes with 2000 vCPUs and 4 TB memory.
Infrastructure Type: Hybrid—on-premises for critical workloads and AWS for dynamic scaling.
Regions: Operating in 2 regions—US-East-1 (primary) and US-West-2 (disaster recovery).
Load Balancer: Using AWS ALB (Application Load Balancer) with auto-scaling target groups.
Applications and Services
Applications: 100+ applications deployed across dev, staging, and production.
Application Types: Mostly microservices (85%), with some serverless (10%) and monolithic (5%).
Services: ~300 services in production.
Workload Types: 75% stateless (e.g., APIs, frontends), 25% stateful (databases, caches).
Third-Party Integrations: Tools like Datadog, Sentry, and New Relic for monitoring; Jenkins for CI/CD.
Kubernetes Pods and Workloads
Running Pods: ~5,000 pods in production.
Average Pods per Service: 15–20 pods per service on average.
HPA Usage: Yes, scaling based on CPU and custom metrics using Prometheus adapters.
Namespace Organization: Per team, with separate namespaces for dev, staging, and production.
Workload Types: 20 DaemonSets, 50 StatefulSets, and ~200 CronJobs.
CI/CD Pipelines
Builds and Deployments: ~500 builds and 300 deployments daily across environments.
Pipeline Structure: Multiple pipelines based on team and application; shared libraries for common steps.
CI/CD Tools: Jenkins for CI, ArgoCD for GitOps-based deployments.
Deployment Strategies: Blue-green deployments for critical services, canary for microservices.
Monitoring and Logging
Tools Used: Prometheus and Grafana for metrics, ELK Stack for logging, and Datadog for APM.
Pod Health Tracking: Readiness and liveness probes; custom metrics exported to Prometheus.
Alerts: 100 alerts per week, categorized as 10% critical, 50% warnings, and 40% informational.
Traffic and User Load
Daily Traffic: Handles ~50,000 requests per second on average.
Ingress Controller: NGINX Ingress controller with 250 ingress rules.
Failover: Multi-region disaster recovery setup with failover DNS routing (Route 53).
Security and Compliance
Authentication and Authorization: RBAC for Kubernetes, OIDC integration with Okta for users.
Network Policies: Yes, around 200 network policies defined for pod-to-pod and external communication.
Security Tools: Using Aqua Security for container scanning, Trivy for vulnerability checks.
Secrets Management: All secrets encrypted and managed via AWS Secrets Manager (~500 secrets).
General Operations
Release Cycle: Weekly release cycle for most applications, with hotfixes as needed.
Developers and Teams: 15 teams with ~150 developers contributing to the infrastructure.
Incidents/Outages: 2–3 incidents monthly, mostly related to resource saturation or misconfigurations.
MTTR: Average recovery time is 30–45 minutes, with critical issues prioritized within 15 minutes.