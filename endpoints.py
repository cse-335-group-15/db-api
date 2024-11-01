import pymysql
import json
from api_config import connection_info

def connect_to_db():
    try:
        connection: pymysql.Connection = pymysql.connect(**connection_info)
        return connection
    except pymysql.MySQLError as e:
        print(f"ERROR: Unable to connect to MySQL. {e}")
        return None
    
def handle_insert(body):
    return "Hello World"

def handle_select(body):
    connection = connect_to_db()

    query = body["query"]

    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        
        return {
                'statusCode': 200,
                'body': json.dumps(result)
            }