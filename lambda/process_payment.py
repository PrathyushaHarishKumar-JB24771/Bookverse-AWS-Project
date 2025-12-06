import json
import uuid

def lambda_handler(event, context):
    """
    Second step in the Step Functions workflow.
    Simulates payment processing and returns a paymentId.
    """
    print("ProcessPayment input:", json.dumps(event))

    book = event.get("book")
    user = event.get("user")

    payment_id = str(uuid.uuid4())

    result = {
        "step": "ProcessPayment",
        "result": "Payment processed",
        "book": book,
        "user": user,
        "paymentId": payment_id,
    }

    print("ProcessPayment output:", json.dumps(result))
    return result
