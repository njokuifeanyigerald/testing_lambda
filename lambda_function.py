import json

def lambda_handler(event, context):
    #  implement
    return {
        'statusCode': 201,
        'body': json.dumps('Hello from Lambda!')
    }
