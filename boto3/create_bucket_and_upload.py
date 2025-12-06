# boto3/create_bucket_and_upload.py

import boto3
import uuid
import os

REGION = "us-east-1"

def main():
    s3 = boto3.client("s3", region_name=REGION)

    # Make a globally unique bucket name
    bucket_name = f"bookverse-boto3-{uuid.uuid4().hex[:8]}"

    print(f"Creating bucket: {bucket_name}")

    # ✅ Special case for us-east-1 (NO LocationConstraint allowed)
    s3.create_bucket(Bucket=bucket_name)

    # Create a small local file
    filename = "boto3-test-file.txt"
    with open(filename, "w") as f:
        f.write("Hello from Boto3 and BookVerse!\n")

    print(f"Uploading {filename} to s3://{bucket_name}/")

    s3.upload_file(filename, bucket_name, filename)

    print("✅ Done.")
    print(f"✅ Bucket: {bucket_name}")
    print(f"✅ Object: {filename}")

    # Cleanup local file only (keep in S3)
    os.remove(filename)

if __name__ == "__main__":
    main()
