import json

def lambda_handler(event, context):
    """
    First step in the Step Functions workflow.
    Pretends to validate an order (book + user).
    """
    print("ValidateOrder input:", json.dumps(event))

    book = event.get("book", "Unknown Book")
    user = event.get("user", "unknown@example.com")

    # In a real system you might check stock, user status, etc.
    result = {
        "step": "ValidateOrder",
        "result": "Order validated",
        "book": book,
        "user": user,
    }

    print("ValidateOrder output:", json.dumps(result))
    return result
