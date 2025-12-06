import json

def lambda_handler(event, context):
    """
    Simple Lambda behind API Gateway that returns a JSON greeting.
    Works with HTTP API / REST API proxy integration.
    """
    # HTTP API v2 style
    path = event.get("rawPath") or event.get("path", "/")
    method = (
        event.get("requestContext", {})
        .get("http", {})
        .get("method", event.get("httpMethod", "GET"))
    )

    body = {
        "message": "Hello from BookVerse API!",
        "path": path,
        "method": method,
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
