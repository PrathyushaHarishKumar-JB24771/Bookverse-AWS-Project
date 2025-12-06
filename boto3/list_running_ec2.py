import boto3

REGION = "us-east-1"

def main():
    ec2 = boto3.client("ec2", region_name=REGION)

    response = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )

    print("Running EC2 instances in us-east-1:")
    found = False
    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            found = True
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            state = instance["State"]["Name"]
            private_ip = instance.get("PrivateIpAddress", "N/A")
            print(f"- {instance_id} | {instance_type} | {state} | {private_ip}")

    if not found:
        print("No running instances found.")

if __name__ == "__main__":
    main()
