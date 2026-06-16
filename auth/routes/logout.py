from services.cognito_service import logout_user
from utils.response import response


def logout(event):
    headers = event.get("headers", {})
    auth_header = headers.get("Authorization", "")

    if not auth_header or not auth_header.startswith("Bearer "):
        return response(
            401,
            {"message": "Authorization token required"}
        )

    access_token = auth_header.split(" ")[1]

    logout_user(access_token)

    return response(
        200,
        {"message": "Logged out successfully"}
    )