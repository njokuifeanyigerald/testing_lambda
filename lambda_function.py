import json

def lambda_handler(event, context):
    #  implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
