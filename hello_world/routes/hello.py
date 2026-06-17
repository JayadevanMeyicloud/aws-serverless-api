# from utils.response import success_response, error_response

# def get_user_details(event):
#     try:
#         # Cognito adds user info here after token verification
#         claims = event['requestContext']['authorizer']['claims']
#         email  = claims.get('email', 'Unknown')
#         sub    = claims.get('sub', '')

#         return success_response(200, {
#             'message': f'Hello, {email}!',
#             'userId':  sub
#         })

#     # except KeyError:
#     #     return error_response(401,'Unauthorized')
#     # except Exception:
#     #     return error_response(500,'Internal server error')

from utils.response import success_response


def get_user_details(event):
    claims = event["requestContext"]["authorizer"]["claims"]

    email = claims.get("email", "Unknown")
    sub = claims.get("sub", "")

    return success_response(
        200,
        {
            "message": f"Hello, {email}!",
            "userId": sub
        }
    )