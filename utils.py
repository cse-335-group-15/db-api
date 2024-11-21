import pymysql
import json

from typing import Callable
from inspect import signature

import api_config

endpoint_list: dict[str, list[Callable]] = {}

def connect_to_db():
    try:
        connection: pymysql.Connection = pymysql.connect(**api_config.connection_info)
        return connection
    except pymysql.MySQLError as e:
        print(f"ERROR: Unable to connect to MySQL. {e}")
        return None


# Decorator for endpoint functions
def endpoint(path: str):
    def decorator(func: Callable):
        def endpoint_wrapper(body: dict):
            connection = connect_to_db()

            args = {}

            for key in body.keys():
                if key in signature(func).parameters:
                    args[key] = body[key]

            try:
                query = func(**args)
            except Exception as e:
                return {
                    'statusCode': 400,
                    'body': json.dumps({
                        'error': 'Couldn\'t generate query',
                        'msg': repr(e)
                    }),
                    'headers': {
                        'Access-Control-Allow-Origin': '*'
                    }
                }
            

            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()

                if (result == None):
                    return {
                        'statusCode': 404,
                        'body': json.dumps({
                            'error': 'No results found'
                        }),
                        'headers': {
                            'Access-Control-Allow-Origin': '*'
                        }
                    }            

                return {
                        'statusCode': 200,
                        'body': json.dumps({
                            'columns': cursor.description,
                            'data': result
                        }),
                        'headers' :  {
                            'Access-Control-Allow-Origin': '*'}
                }

        key = f'/{api_config.profile}/{path}'
        if key in endpoint_list:
            endpoint_list[key].append(endpoint_wrapper)
        else:
            endpoint_list[key] = [endpoint_wrapper]
        return endpoint_wrapper
    return decorator
