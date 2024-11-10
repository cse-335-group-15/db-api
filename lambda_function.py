import json

import endpoints # This import is necessary to register the endpoints, don't let your IDE remove it

from utils import endpoint_list
from api_config import profile




def lambda_handler(event, context):
    # Route based on method and path
    if event['httpMethod'] != 'POST':
        return {
            'statusCode': 405,
            'body': json.dumps('Method not allowed'),
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }
    
    for path, endpoint in endpoint_list.items():
        if event['path'] == f'/{profile}/{path}':
            return endpoint(json.loads(event['body']))
        
    return {
        'statusCode': 404,
        'body': json.dumps({
            'error': 'Path not found'
        }),
        'headers': {
                'Access-Control-Allow-Origin': '*'
        }
    }    

    
    

