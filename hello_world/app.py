from botocore.exceptions import ClientError

from routes.hello import get_user_details
from utils.response import error_response


def lambda_handler(event, context):
    try:
        return get_user_details(event)

    except ClientError as e:
        return error_response(
            400,
            e.response["Error"]["Message"]
        )

    except Exception as e:
        print(f"Unexpected Error: {str(e)}")

        return error_response(
            500,
            "Internal server error"
        )
