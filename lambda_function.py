import json
from endpoints import handle_insert, handle_select
from api_config import profile

def lambda_handler(event, context):
    # Route based on method and path
    if event['httpMethod'] == 'POST' and event['path'] == f'/{profile}/insert':
        try:
            body = json.loads(event['body'])
            return handle_insert(body)
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON format')
            }

    elif event['httpMethod'] == 'POST' and event['path'] == f'/{profile}/select':
        try:
            body = json.loads(event['body'])
            return handle_select(body)
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON format')
            }

    else:
        return {
            'statusCode': 404,
            'body': json.dumps({
                'error': 'Path not found'
            })
        }