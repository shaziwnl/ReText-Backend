import json
from validation import InputSchema
from marshmallow import ValidationError
from methods import rectify_handler, verbose_handler, concise_handler, formalize_handler


def lambda_handler(event, context):
    print(event)

    # Handle preflight (OPTIONS) requests
    if event['requestContext']['http']['method'] == 'OPTIONS':
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",  # Allow all origins or specify a specific one
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            "body": ""
        }

    if event['requestContext']['http']['method'] != 'POST':
        return {
            "statusCode": 405,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            "body": json.dumps({"error": "Method Not Allowed"})
        }
    
    route = event['requestContext']['http']['path'].strip("/")
    
    try:
        data = json.loads(event["body"])
        InputSchema().load(data)
    except ValidationError:
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            "body": json.dumps({"error": "Invalid input"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            "body": json.dumps({"error": f"Internal server error: {str(e)}"})
        }
    
    # Route requests to appropriate handlers
    if route == "verbose":
        response = verbose_handler(data)
    elif route == "concise":
        response = concise_handler(data)
    elif route == "rectify":
        response = rectify_handler(data)
    elif route == "formalize":
        response = formalize_handler(data)
    else:
        response = {
            "statusCode": 404,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            "body": json.dumps({"error": "Not Found"})
        }

    # Add CORS headers to the response
    response["headers"] = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
    }

    return response
