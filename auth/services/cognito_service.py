import boto3
import os

cognito = boto3.client("cognito-idp")

USER_POOL_ID = os.environ["USER_POOL_ID"]
CLIENT_ID = os.environ["CLIENT_ID"]


def signup_user(email, password):

    cognito.sign_up(
        ClientId=CLIENT_ID,
        Username=email,
        Password=password,
        UserAttributes=[
            {
                "Name": "email",
                "Value": email
            }
        ]
    )

    cognito.admin_confirm_sign_up(
        UserPoolId=USER_POOL_ID,
        Username=email
    )
    
def login_user(email, password):

    return cognito.initiate_auth(
        ClientId=CLIENT_ID,
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={
            "USERNAME": email,
            "PASSWORD": password
        }
    )
    
def logout_user(access_token):

    cognito.global_sign_out(
        AccessToken=access_token
    )