# Bookverse-AWS-Project

# BookVerse – Scalable AWS Architecture with IaC

This project implements a scalable, production-style AWS architecture for a fictional book discovery app called **BookVerse**.

# Project Overview

BookVerse is a cloud-based web application designed to demonstrate a scalable, secure, and automated AWS architecture using Infrastructure as Code (IaC).
The goal of this project was not to build a full-featured production application, but to design, deploy, and validate a real-world AWS infrastructure using multiple services working together.

The system was built using a combination of Terraform and AWS CloudFormation, allowing different layers of the infrastructure to be provisioned in a repeatable and controlled manner. Terraform was used to create the core networking layer (VPC, subnets, routing, and security groups), while CloudFormation was used to deploy application-level resources such as EC2, Auto Scaling, Application Load Balancer, RDS, S3, and Lambda.

The application architecture follows best practices by separating public and private resources. Public subnets host the Application Load Balancer and a bastion host for secure administrative access, while private subnets contain the EC2 web servers and the RDS MySQL database. This ensures that sensitive components like the database are never exposed to the public internet.

A static frontend for BookVerse is hosted on Amazon S3 and serves as the user interface for browsing book genres and titles. Backend functionality is demonstrated using AWS Lambda functions. One Lambda function logs file uploads from an S3 bucket into CloudWatch Logs, while another Lambda is exposed through API Gateway to provide a simple HTTP endpoint. In addition, AWS Step Functions were implemented to orchestrate a multi-step “order workflow,” showing how serverless services can be combined to model real application processes.

Interaction with AWS services was demonstrated in multiple ways:

1. Through the AWS Management Console for verification

2. Through the AWS CLI for resource management

3. Through Python Boto3 scripts for programmatic access to EC2, S3, Lambda, and instance metadata

Database connectivity was validated by securely connecting from a bastion host to the RDS MySQL instance and executing Python scripts that query real data stored in the database. This confirms that the backend database is correctly provisioned, secured, and reachable from within the VPC.

Overall, this project demonstrates a complete AWS deployment lifecycle—including design, provisioning, validation, and automation—while following cloud security and scalability best practices. It reflects how modern cloud architectures are built and managed using Infrastructure as Code and managed AWS services.#

# 1. Components Overview

- **Terraform** – VPC, public & private subnets, routing, security groups
- **CloudFormation** – EC2 Auto Scaling, Application Load Balancer (ALB), RDS MySQL, S3 uploads bucket, Lambda
- **S3 + Static Website** – Vintage-style BookVerse frontend
- **Lambda + S3 events** – log uploads to CloudWatch
- **Boto3 (Python)** – interact with S3, EC2, and Lambda from scripts
- **Bastion host + RDS** – secure DB access from inside the VPC
- **API Gateway + Lambda** – simple `/hello` HTTP endpoint
- **Step Functions** – “Book order” workflow with 3 Lambda steps

---

## 2. Architecture Overview

High-level components:

- **VPC (Terraform)**
  - 2 public subnets (A, B)
  - 2 private subnets (A, B)
  - Internet Gateway, route tables
  - Security groups for:
    - Bastion
    - Web EC2 instances
    - RDS

- **Compute (CloudFormation)**
  - Launch Template for web EC2
  - Auto Scaling Group in **private subnets**
  - Application Load Balancer in **public subnets**
  - User data script to serve the frontend

- **Database**
  - **RDS MySQL** in private subnets
  - Security group only allows MySQL from web-tier SG
  - Data loaded with sample book records (Romance/Fiction/Non-Fiction)

- **Storage & Serverless**
  - S3 bucket for uploads (CloudFormation output: `UploadBucketName`)
  - S3 → Lambda trigger for logging uploads to **CloudWatch Logs**
  - Separate S3 bucket (`bookverse-boto3-…`) used as a static website for the BookVerse UI

- **Networking / Access**
  - Bastion host EC2 in public subnet for SSH
  - From bastion → private EC2 and RDS

- **API & Workflow (Bonus)**
  - API Gateway HTTP API with `/hello` route → Lambda
  - Step Functions state machine:
    - `ValidateOrder` (Lambda)
    - `ProcessPayment` (Lambda)
    - `CompleteOrder` (Lambda)

---

