import json


def function2(event, context):
    body = {
        "message": "This is function2",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
