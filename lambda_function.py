import json
from endpoints import handle_insert, handle_complex_select, handle_delete, handle_update
from api_config import profile

def lambda_handler(event, context):
    # Route based on method and path
    if event['httpMethod'] != 'POST':
        return {
            'statusCode': 405,
            'body': json.dumps('Method not allowed')
        }

    if event['path'] == f'/{profile}/insert':
        try:
            body = json.loads(event['body'])
            return handle_insert(body)
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON format')
            }

    elif event['path'] == f'/{profile}/select':
        try:
            body = json.loads(event['body'])
            return handle_complex_select(body)
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON format')
            }
        

    elif event['httpMethod'] == 'POST' and event['path'] == f'/{profile}/Cselect':
        try:
            body = json.loads(event['body'])
            return handle_complex_select(body)
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON format')
            }
        
    elif event['httpMethod'] == 'POST' and event['path'] == f'/{profile}/delete':
        try:
            body = json.loads(event['body'])
            return handle_delete(body)
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON format')
            }
        
    elif event['httpMethod'] == 'POST' and event['path'] == f'/{profile}/update':
        try:
            body = json.loads(event['body'])
            return handle_update(body)
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
    
