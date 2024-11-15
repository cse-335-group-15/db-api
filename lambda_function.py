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
    

    if event['path'] not in endpoint_list:
        return {
                'statusCode': 404,
                'body': json.dumps({
                    'error': 'Path not found'
                }),
                'headers': {
                        'Access-Control-Allow-Origin': '*'
                }
            }    

    funcs = endpoint_list[event['path']]
    
    for func in funcs: 
        try:
            return func(json.loads(event['body']))
        except TypeError:
            continue
        
    
    
    

