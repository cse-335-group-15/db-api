import unittest
from lambda_function import lambda_handler
import api_config
from api_config import profile


# DO NOT INCLUDE THIS FILE IN PUBLICATION TO AWS LAMBDA

# Change connection info to test stuff
api_config.connection_info = {
    "host": "127.0.0.1",
    "user": "test",
    "passwd": "test1234",
    "db": "lab4",
    "port": 3306,
    "connect_timeout": 5
}

# Write tests here

# Create a new class to test a specific endpoint.
# This class is just to test if the lambda function is working in general.
class TestLambdaHandler(unittest.TestCase):
    def test_select(self):
        query = 'SELECT * FROM foo'

        event = {
        'httpMethod': 'POST',
        'path': f'/{profile}/query',
        'body': f'{{ "query": "{query}", "foo": "bar" }}'
        }

        expects = {
            'statusCode': 200,
            'body': '[[1, "world"], [2, "boo"], [3, "hello"]]',
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }
        
        self.assertEqual(lambda_handler(event, None), expects, "Not returning correct select query response")

    def test_insert(self):
        query = 'INSERT INTO foo VALUES (2, \\"idk\\")'

        event = {
            'httpMethod': 'POST',
            'path': f'/{profile}/insert',
            'body': f'{{ "query": "{query}"}}'
        }

        expects = {
            'statusCode': 400,
            'body': '{"error": "Couldn\'t generate query"}',
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }
        self.assertEqual(lambda_handler(event, None), expects, "Not returning correct insert query response")



if (__name__ == "__main__"):
    unittest.main()
    