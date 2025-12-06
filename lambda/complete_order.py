import json

def lambda_handler(event, context):
    """
    Final step in the Step Functions workflow.
    Marks the order as completed.
    """
    print("CompleteOrder input:", json.dumps(event))

    book = event.get("book")
    user = event.get("user")
    payment_id = event.get("paymentId")

    result = {
        "step": "CompleteOrder",
        "result": "Order completed",
        "book": book,
        "user": user,
        "paymentId": payment_id,
    }

    print("CompleteOrder output:", json.dumps(result))
    return result
