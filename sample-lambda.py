import json

def lambda_handler(event, context):
    print('My first lambda with python')
    return{
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda')
    }