#!/usr/bin/env python3
import requests
import boto3
from botocore.exceptions import NoCredentialsError, NoRegionError

TOKEN_URL = "http://169.254.169.254/latest/api/token"
METADATA_URL = "http://169.254.169.254/latest/meta-data"


def get_token():
    resp = requests.put(
        TOKEN_URL,
        headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
        timeout=2,
    )
    resp.raise_for_status()
    return resp.text


def get_metadata(token, path):
    resp = requests.get(
        f"{METADATA_URL}/{path}",
        headers={"X-aws-ec2-metadata-token": token},
        timeout=2,
    )
    resp.raise_for_status()
    return resp.text


def main():
    print("EC2 Instance Metadata (IMDSv2):")

    token = get_token()
    instance_id = get_metadata(token, "instance-id")
    instance_type = get_metadata(token, "instance-type")
    local_ipv4 = get_metadata(token, "local-ipv4")
    az = get_metadata(token, "placement/availability-zone")

    print(f"- Instance ID: {instance_id}")
    print(f"- Instance Type: {instance_type}")
    print(f"- Local IPv4: {local_ipv4}")
    print(f"- Availability Zone: {az}")

    # Optional: call EC2 API via boto3
    try:
        region = az[:-1]  # us-east-1a -> us-east-1
        ec2 = boto3.client("ec2", region_name=region)
        resp = ec2.describe_instances(InstanceIds=[instance_id])

        inst = resp["Reservations"][0]["Instances"][0]
        tags = inst.get("Tags", [])

        print("\nEC2 API data via boto3:")
        print(f"- State: {inst['State']['Name']}")
        print(f"- Launch time: {inst['LaunchTime']}")
        if tags:
            print("- Tags:")
            for t in tags:
                print(f"  {t['Key']} = {t['Value']}")
        else:
            print("- No tags on this instance.")
    except (NoCredentialsError, NoRegionError):
        print("\nNo AWS credentials / region configured for boto3 – skipping EC2 API call.")
    except Exception as e:
        print("\nError calling EC2 API via boto3:", e)


if __name__ == "__main__":
    main()
