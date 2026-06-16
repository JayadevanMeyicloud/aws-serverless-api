from routes.hello import get_user_details

def lambda_handler(event, context):
    return get_user_details(event)

