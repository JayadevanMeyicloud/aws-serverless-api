import json

from services.cognito_service import login_user
from utils.response import response


def login(event):
    body = json.loads(event.get("body", "{}"))

    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        return response(
            400,
            {"message": "email and password are required"}
        )

    result = login_user(email, password)
    tokens = result["AuthenticationResult"]

    return response(
        200,
        {
            "message": "Login successful",
            "accessToken": tokens["AccessToken"],
            "idToken": tokens["IdToken"],
            "refreshToken": tokens["RefreshToken"],
            "expiresIn": tokens["ExpiresIn"]
        }
    )