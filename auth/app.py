
from routes.register import register
from routes.login import login
from routes.logout import logout
from utils.response import response

def lambda_handler(event, context):

    path = event.get("path", "")
    method = event.get("httpMethod", "")

    if path == "/auth/register" and method == "POST":
        return register(event)

    elif path == "/auth/login" and method == "POST":
        return login(event)

    elif path == "/auth/logout" and method == "POST":
        return logout(event)

    return response(
        404,
        {"message": "Route not found"}
    )