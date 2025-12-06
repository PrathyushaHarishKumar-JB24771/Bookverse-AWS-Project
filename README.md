# Bookverse-AWS-Project

# BookVerse – Scalable AWS Architecture with IaC

This project implements a scalable, production-style AWS architecture for a fictional book discovery app called **BookVerse**.

It uses:

- **Terraform** – VPC, public & private subnets, routing, security groups
- **CloudFormation** – EC2 Auto Scaling, Application Load Balancer (ALB), RDS MySQL, S3 uploads bucket, Lambda
- **S3 + Static Website** – Vintage-style BookVerse frontend
- **Lambda + S3 events** – log uploads to CloudWatch
- **Boto3 (Python)** – interact with S3, EC2, and Lambda from scripts
- **Bastion host + RDS** – secure DB access from inside the VPC
- **API Gateway + Lambda** – simple `/hello` HTTP endpoint
- **Step Functions** – “Book order” workflow with 3 Lambda steps

---

## 1. Architecture Overview

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

**PROJECT OVERVIEW**
┌──────────────────────────────────────────────────────────────┐
│                          GitHub                               │
│               (Terraform / CloudFormation / CI-CD)            │
│                          |                                   │
│                      GitHub Actions                           │
│                          |                                   │
│                   AWS CodeDeploy                              │
│                          |                                   │
│                      S3 (Artifacts)                           │
└──────────────────────────────────────────────────────────────┘
                                  |
                                  v
┌───────────────────────────────────────────────────────────────────────────────┐
│                                 AWS Account                                   │
│                                                                               │
│  ┌────────────────────────── VPC (bookverse-vpc) ──────────────────────────┐ │
│  │                                                                           │ │
│  │  ┌──────────── Public Subnet A ─────────────┐   ┌────────────── Public Subnet B ───────────────┐ │
│  │  │                                            │   │                                               │ │
│  │  │   Internet Gateway                         │   │                                               │ │
│  │  │        |                                  │   │                                               │ │
│  │  │   Application Load Balancer (ALB)         │   │   Bastion Host (EC2)                           │ │
│  │  │   (HTTP :80)                              │   │   SSH Access (port 22)                         │ │
│  │  │        |                                  │   │                                               │ │
│  │  └────────┬──────────────────────────────────┘   └──────────────┬────────────────────────────────┘ │
│  │           |                                                        |                                   │
│  │           v                                                        v                                   │
│  │  ┌──────────────────────── Private Subnet A ─────────────────────────────────────────────────────┐ │
│  │  │                                                                                                  │ │
│  │  │   Auto Scaling Group                                                                              │ │
│  │  │   ┌─────────────────────┐                                                                        │ │
│  │  │   │ EC2 Web Server       │                                                                        │ │
│  │  │   │ (Python HTTP Server) │                                                                        │ │
│  │  │   │ Static BookVerse UI  │                                                                        │ │
│  │  │   └─────────────────────┘                                                                        │ │
│  │  │            |                                                                                     │ │
│  │  │            v                                                                                     │ │
│  │  │      RDS MySQL Database                                                                           │ │
│  │  │      (Private, no public access)                                                                  │ │
│  │  └──────────────────────────────────────────────────────────────────────────────────────────────────┘ │
│  │                                                                                                       │
│  └───────────────────────────────────────────────────────────────────────────────────────────────────────┘
│                                                                                                           │
│   ┌─────────────── S3 Buckets ────────────────┐        ┌──────────── CloudWatch Logs ─────────────┐     │
│   │                                           │        │                                             │     │
│   │  • Uploads Bucket                         │ ─────▶│  Lambda Logs (S3 Upload Events)             │     │
│   │                                           │        │                                             │     │
│   │                                           │        └─────────────────────────────────────────────┘     │
│   └───────────────────────────────────────────┘                                                            │
│                                                                                                           │
│   ┌──────────────────── Serverless & Orchestration ────────────────────┐                                 │
│   │                                                                      │                                 │
│   │  API Gateway  ─────▶  Lambda Functions                               │                                 │
│   │                          |                                           │                                 │
│   │                     Step Functions                                   │                                 │
│   │              (Order Validation → Payment → Completion)               │                                 │
│   └──────────────────────────────────────────────────────────────────────┘                                 │
│                                                                                                           │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘

