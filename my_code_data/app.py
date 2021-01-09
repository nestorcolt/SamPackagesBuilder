import requests
import json


def lambda_handler(event, context):
    try:
        ip = requests.get("http://checkip.amazonaws.com/")
        print(f"Request Module working:\n{ip.conten}")
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip.text.replace("\n", "")
        }),
    }
