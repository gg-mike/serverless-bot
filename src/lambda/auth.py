import requests


def get_effect(token):
    response = requests.get(f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={token.split(' ')[1]}")
    if response.status_code == 200:
        return "Allow"
    return "Deny"


def handler(event, context):
    response = {
        "principalId": "abcdef",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": get_effect(event["headers"]["authorization"]),
                    "Resource": event["routeArn"]
                }
            ]
        }
    }
    return response
