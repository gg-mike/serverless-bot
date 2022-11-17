import requests


def get_effect(token):
    response = requests.get(f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={token.split(' ')[1]}")
    if response.status_code == 200:
        return "Allow"
    return "Deny"


def handler(event, context):
    effect = "Deny"
    routeArn = "placeholder"
    try:
        effect = get_effect(event["headers"]["authorization"])
        routeArn = event["routeArn"]
    except Exception as e:
        print(e)
    
    response = {
        "principalId": "xyz",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": routeArn
                }
            ]
        }
    }
    return response
