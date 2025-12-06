import json

def lambda_handler(event, context):
    """
    Triggered by S3 PUT/POST/Copy events.
    Logs basic information about uploaded objects to CloudWatch Logs.
    """
    print("Received S3 event:")
    print(json.dumps(event))

    records = event.get("Records", [])
    for record in records:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        size = record["s3"]["object"].get("size", "unknown")
        event_name = record.get("eventName", "UnknownEvent")

        print(f"New object event: {event_name}")
        print(f"Bucket: {bucket}")
        print(f"Key   : {key}")
        print(f"Size  : {size}")

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "S3 event logged"})
    }
