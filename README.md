📚 BookVerse – Scalable Cloud-Native Book Discovery Platform on AWS

A scalable, cloud-native book discovery and ordering platform built on Amazon Web Services (AWS), demonstrating Infrastructure as Code (IaC), serverless workflows, secure cloud networking, and real-world AWS operations.

AWS | Terraform | CloudFormation | EC2 | RDS | S3 | Lambda | API Gateway | Step Functions | Python | Boto3

🎯 Overview

BookVerse is a cloud-based application designed to showcase how a modern, scalable web platform can be architected and deployed on AWS using Infrastructure as Code and managed services.

Conceptually, BookVerse represents an online book discovery platform where users can:

Browse books by genre

View book details (author, summary, genre)

Place book orders

Trigger backend workflows for order validation and processing

While the web interface is intentionally kept lightweight (static HTML/JS), the backend architecture is fully production-aligned, scalable, secure, and extensible.

This project prioritizes cloud architecture, automation, security, and operational validation over UI complexity.

🌟 Key Highlights

✅ Infrastructure provisioned using Terraform and AWS CloudFormation

✅ Highly available EC2 instances behind an Application Load Balancer

✅ Auto Scaling Group for web tier scalability

✅ Secure MySQL database hosted on Amazon RDS

✅ Amazon S3 for object storage and static assets

✅ Event-driven AWS Lambda for S3 upload logging

✅ API Gateway + Lambda for HTTP-based backend API

✅ AWS Step Functions for order workflow automation

✅ Secure access using a Bastion Host

✅ AWS interaction via Console, CLI, and Boto3

✅ Fully version-controlled using GitHub

🏗️ High-Level Architecture
┌───────────────────────────────────────────────────────────────┐
│                            Internet                           │
└───────────────────────────────┬──────────────────────────────┘
                                │
                                ▼
                    ┌────────────────────────────┐
                    │   Application Load Balancer │
                    │     (Internet-facing)       │
                    └───────────────┬────────────┘
                                    │
                                    ▼
                ┌────────────────────────────────────┐
                │        Auto Scaling Group            │
                │   EC2 Web Servers (Private Subnets)  │
                └───────────────┬────────────────────┘
                                │
                   ┌────────────┼────────────┐
                   ▼            ▼            ▼
          ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐
          │    Amazon    │  │   AWS Lambda │  │  API Gateway    │
          │     RDS      │  │  (S3 Logger) │  │  + Lambda API   │
          │   (MySQL)    │  └──────┬──────┘  └─────────────────┘
          └─────────────┘         │
                                  ▼
                            ┌──────────────┐
                            │ CloudWatch   │
                            │     Logs     │
                            └──────────────┘

🏗️ Architecture Components
1️⃣ Networking (Amazon VPC)
Component	Details
VPC CIDR	Custom VPC
Public Subnets	2 (ALB, Bastion Host)
Private Subnets	2 (EC2, RDS)
Availability Zones	us-east-1a, us-east-1b
Internet Gateway	Enabled
Routing	Public & private route tables

✅ Provisioned using Terraform

2️⃣ Compute (EC2)
Component	Configuration
Instance Type	t3.micro
OS	Amazon Linux 2023
Scaling	Auto Scaling Group
Placement	Private subnets
Access	Via ALB only

✅ Deployed using CloudFormation

3️⃣ Load Balancing (ALB)
Feature	Configuration
Type	Application Load Balancer
Scheme	Internet-facing
Listener	HTTP (80)
Health Checks	/
Target	EC2 instances
4️⃣ Database (Amazon RDS – MySQL)
Feature	Configuration
Engine	MySQL
Instance Class	db.t3.micro
Storage	20 GB (gp2)
Network	Private subnets only
Public Access	Disabled
Security	SG-restricted

✅ Database connectivity validated from within the VPC

5️⃣ Storage (Amazon S3)
Feature	Purpose
Bucket	Object storage & uploads
Access	Private
Encryption	SSE-S3
Integration	Lambda triggers on upload
6️⃣ Serverless (AWS Lambda)
🔹 S3 Upload Logger

Triggered on ObjectCreated

Logs upload metadata into CloudWatch

Demonstrates event-driven architecture

🔹 API Lambda (Bonus)

Exposed via API Gateway

Returns real-time JSON response

Invoked using curl and browser

7️⃣ API Gateway (Bonus)
Feature	Configuration
API Type	HTTP API
Route	/hello
Integration	Lambda proxy
CORS	Enabled
8️⃣ Workflow Automation (AWS Step Functions – Bonus)

BookVerse Order Workflow

Validate Order

Process Payment (simulated)

Complete Order

Each step is:

A separate Lambda function

JSON-based input/output

Fully traceable via execution logs

✅ Workflow executed successfully end-to-end

9️⃣ Bastion Host (Security)
Purpose	Description
Access	SSH gateway
Location	Public subnet
Usage	RDS validation & admin tasks

✅ Demonstrates secure access to private resources

🧪 Backend Validation

Even though BookVerse’s UI is static, the backend is fully functional:

Python script connects to RDS

Queries real book data

Prints results successfully

Confirms database + network correctness

🐍 Boto3 Scripts
Script	Purpose
Create S3 bucket + upload	Storage validation
List running EC2	Compute inspection
Retrieve EC2 metadata	IMDS validation
Invoke Lambda	Serverless test

All scripts executed successfully.

📁 Project Structure
bookverse-aws-project/
├── terraform/                   # VPC, subnets, security groups
├── cloudformation/              # EC2, ALB, RDS, Lambda, ASG
├── lambda/
│   ├── s3_logger_lambda.py
│   ├── api_hello_lambda.py
│   ├── validate_order.py
│   ├── process_payment.py
│   └── complete_order.py
├── bastion-scripts/
│   ├── get_instance_metadata.py
│   ├── db_check.py
│   └── requirements.txt
├── step-functions/
│   └── bookverse-order-workflow.asl.json
├── frontend/
│   └── index.html
└── README.md

🔁 Data Flow
User Request
Browser → ALB → EC2 → Response

File Upload
Upload → S3 → Lambda → CloudWatch

API Call
Client → API Gateway → Lambda → JSON Response

Workflow
Order → Step Functions → Lambdas → Completion

💰 Cost Optimization

Free-tier eligible instance sizes

RDS Single-AZ

No always-on serverless compute

Event-driven Lambda execution only

Auto Scaling avoids overprovisioning

🚀 Future Enhancements

✅ HTTPS via ACM

✅ CloudFront CDN

✅ CI/CD with GitHub Actions

✅ User authentication (Cognito)

✅ UI-to-DB integration

✅ Monitoring dashboards

✅ Payment gateway integration

Project Outcome

BookVerse successfully demonstrates:

✅ Secure cloud networking
✅ Scalable compute architecture
✅ Database backend configuration
✅ Serverless automation
✅ Workflow orchestration
✅ Infrastructure as Code mastery
✅ End-to-end validation



