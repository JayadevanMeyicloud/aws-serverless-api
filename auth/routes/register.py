import json

from services.cognito_service import signup_user
from utils.response import response


def register(event):
    body = json.loads(event.get("body", "{}"))

    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        return response(
            400,
            {"message": "email and password are required"}
        )

    signup_user(email, password)

    return response(
        201,
        {
            "message": "User registered successfully",
            "email": email
        }
    )