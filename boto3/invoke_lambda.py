import boto3
import json

REGION = "us-east-1"
FUNCTION_NAME = "bookverse-log-s3-uploads"  # change if your function name is different

def main():
    client = boto3.client("lambda", region_name=REGION)

    payload = {"message": "Hello from Boto3 invoke_lambda.py"}
    print(f"Invoking Lambda: {FUNCTION_NAME}")

    response = client.invoke(
        FunctionName=FUNCTION_NAME,
        InvocationType="RequestResponse",
        Payload=json.dumps(payload).encode("utf-8"),
    )

    print("StatusCode:", response["StatusCode"])
    body = response["Payload"].read().decode("utf-8")
    print("Response payload:", body)

if __name__ == "__main__":
    main()
