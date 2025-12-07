# 📚 BookVerse – Scalable Cloud-Native Book Discovery Platform on AWS

A scalable, cloud-native book discovery and ordering platform built on **Amazon Web Services (AWS)**, demonstrating Infrastructure as Code (IaC), serverless workflows, secure cloud networking, and real-world AWS operations.

**Tech Stack:**  
`AWS • Terraform • CloudFormation • EC2 • RDS • S3 • Lambda • API Gateway • Step Functions • Python • Boto3`

---

## 🎯 Overview

**BookVerse** is a cloud-based application built to showcase how a modern, scalable platform can be deployed on AWS using **Infrastructure as Code** and **managed services**.

Users can:

- 📖 Browse books by genre  
- 👀 View book details (author, summary, genre)  
- 🛒 Place book orders  
- ⚙️ Trigger backend workflows for order validation & processing  

The UI is intentionally simple—**the focus is the AWS architecture and automation**.

---

## 🌟 Key Highlights

- ✅ Infrastructure via **Terraform** + **CloudFormation**  
- ✅ Highly available **EC2 behind ALB**  
- ✅ Auto Scaling Group for web tier  
- ✅ Secure **RDS MySQL** in private subnets  
- ✅ **S3** for storage + Lambda trigger  
- ✅ **API Gateway + Lambda** backend API  
- ✅ **Step Functions** for order workflow  
- ✅ Bastion host for secure private access  
- ✅ AWS interactions via **Console, CLI, & Boto3**  
- ✅ Fully version-controlled in GitHub  

---

## 🏗️ High-Level Architecture
      # BookVerse AWS Architecture (us-east-1)

             +---------------------------+
             |       Internet Gateway    |
             +------------+--------------+
                          |
                          v
             +---------------------------+
             | Application Load Balancer |
             +------------+--------------+
                          |
                          v
      +---------------------------+     +---------------------------+
      |       Public Subnet A     |     |       Public Subnet B     |
      |   Internet Gateway / ALB  |     |  Bastion Host (EC2, SSH) |
      +---------------------------+     +---------------------------+
                          |                        |
                          +-----------+------------+
                                      |
                                      v
                      +---------------------------+  
                      |   Private Subnets A & B     |
                      |   Auto Scaling Group      |
                      |   EC2 Web Servers (t3)   |
                      +------------+--------------+
                                   |
                                   v
                           +---------------+
                           |   RDS MySQL   |
                           |   (Private)   |
                           +---------------+

      +---------------------------+     +---------------------------+
      |           S3              | --> |        AWS Lambda         |
      |     Uploads / Files       |     | Logs uploads to CloudWatch|
      +---------------------------+     +---------------------------+

      +---------------------------+     +---------------------------+
      |       API Gateway         | --> |      Step Functions       |
      |      /hello /order        |     | Validate → Process → Done |
      +---------------------------+     +---------------------------+

---

## 🏗️ Architecture Components

### 1️⃣ Networking (VPC)

| Component       | Details                       |
|-----------------|-------------------------------|
| VPC             | Custom CIDR                   |
| Public Subnets  | ALB, Bastion Host             |
| Private Subnets | EC2, RDS                      |
| AZs             | us-east-1a, us-east-1b       |
| Internet Gateway| Enabled                       |
| Routing         | Public & private route tables |
| IaC             | **Terraform**                 |

---

### 2️⃣ Compute (EC2 Web Tier)

| Component       | Configuration                |
|-----------------|------------------------------|
| Instance Type   | t3.micro                     |
| OS              | Amazon Linux 2023            |
| Scaling         | Auto Scaling Group           |
| Network         | Private subnets              |
| Access          | Via ALB only                 |
| IaC             | **CloudFormation**           |

---

### 3️⃣ Load Balancer (ALB)

| Feature   | Configuration             |
|-----------|---------------------------|
| Type      | Application Load Balancer |
| Scheme    | Internet-facing           |
| Listener  | HTTP:80                   |
| Target    | EC2 (Private)             |

---

### 4️⃣ Database (Amazon RDS – MySQL)

| Feature       | Configuration           |
|---------------|------------------------|
| Engine        | MySQL                  |
| Instance Class| db.t3.micro            |
| Storage       | 20 GB gp2              |
| Access        | Private only           |
| Public Access | Disabled               |
| Security SG   | Restricted inbound     |

---

### 5️⃣ Storage (Amazon S3)

- Private bucket  
- SSE-S3 encryption  
- Triggers Lambda on upload  

---

### 6️⃣ Serverless (AWS Lambda)

#### 🔹 S3 Upload Logger
- Triggered on **ObjectCreated**  
- Logs metadata to CloudWatch  

#### 🔹 API Lambda
- Exposed through **API Gateway**  
- Returns JSON response  

---

### 7️⃣ API Gateway

| Feature    | Details             |
|------------|-------------------|
| API Type   | HTTP API           |
| Route      | `/hello`           |
| Integration| Lambda Proxy       |
| CORS       | Enabled            |

---

### 8️⃣ Step Functions Workflow

📦 **Order Workflow Steps**  
1. Validate Order (Lambda)  
2. Process Payment (Lambda)  
3. Complete Order (Lambda)  

Execution logs fully traceable.

---

### 9️⃣ Bastion Host

- SSH gateway  
- Located in public subnet  
- Used for RDS validation & VPC access  

---

## 🧪 Backend Validation

- Python script connects to RDS  
- Retrieves book data  
- S3 uploads trigger Lambda  
- API Gateway returns JSON  
- Workflow runs end-to-end  

---

## 🐍 Boto3 Scripts

| Script                 | Purpose                       |
|------------------------|-------------------------------|
| Create S3 bucket       | Validate storage              |
| List EC2               | Inspect compute               |
| Instance metadata      | IMDS validation               |
| Invoke Lambda          | Test serverless               |

---

## 🔁 Data Flow

**Web App:**  
`Browser → ALB → EC2 → Response`

**File Upload:**  
`Client → S3 → Lambda → CloudWatch`

**API Call:**  
`Client → API Gateway → Lambda → JSON`

**Order Workflow:**  
`API → Step Functions → Lambda chain → Complete`

---

## 💰 Cost Optimization

- Free-tier eligible EC2 & RDS  
- Single-AZ database  
- Serverless on-demand  
- Auto Scaling avoids overprovisioning  

---

## 🚀 Future Enhancements

- HTTPS via ACM  
- CloudFront CDN  
- GitHub Actions CI/CD  
- Cognito authentication  
- UI-to-DB integration  
- Monitoring dashboards  
- Real payment gateway  

---

## 🎉 Project Outcome

BookVerse demonstrates:

- ✅ Secure cloud networking  
- ✅ Highly available compute  
- ✅ RDS database deployment  
- ✅ Serverless automation  
- ✅ Workflow orchestration  
- ✅ Infrastructure as Code  
- ✅ End-to-end cloud validation
