import json


def function1(event, context):
    body = {
        "message": "This is function1",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
