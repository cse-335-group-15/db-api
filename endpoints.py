import pymysql
import json
import api_config

def connect_to_db():
    try:
        connection: pymysql.Connection = pymysql.connect(**api_config.connection_info)
        return connection
    except pymysql.MySQLError as e:
        print(f"ERROR: Unable to connect to MySQL. {e}")
        return None
    
def handle_insert(body):
    connection = connect_to_db()
    return {
        'statusCode': 200,
        'body': json.dumps({
            'msg': 'endpoint not implemented'
        })
    }

def handle_complex_select(body):
    connection = connect_to_db()

    query = 'Select name as movie_name, first_name as star_first_name, last_name as star_last_name FROM movie Inner join cast on movie.StarID = cast.ID Inner join reviews on movie.ReviewsID = reviews.ReviewsID Where Score > (select AVG(Score)  FROM reviews)'

    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        
        return {
                'statusCode': 200,
                'body': json.dumps(result),
                'headers' :  {
                    'Access-Control-Allow-Origin': '*'}
            }

def handle_delete(body):
    connection = connect_to_db()

    postData = body

    query = {'delete * from movies where ', postData['comparison'], '=', postData['input']}

    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        
        return {
                'statusCode': 200,
                'body': json.dumps(result),
                'headers' :  {
                    'Access-Control-Allow-Origin': '*'}
        }
    
def handle_update(body):
    connection = connect_to_db()

    query = {'update table ratings set votes = {votes}, score = {score} where id = (SELECT review_id FROM movies WHERE id = {movie_id})'}

    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()

    return {
                'statusCode': 200,
                'body': json.dumps(result),
                'headers' :  {
                    'Access-Control-Allow-Origin': '*'}
            }