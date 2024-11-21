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
    "db": "project_test",
    "port": 3306,
    "connect_timeout": 5
}
# Write tests here
# Tests are executed from bottom to top for each class.
# TODO: Write tests for all the endpoints so I'm not gambling everytime I upload this
class TestLambdaHandler(unittest.TestCase):
    def test_method(self):
        event = {
            'httpMethod': 'GET',
        }

        expects = {
            'statusCode': 405,
            'body': {
                'error': 'Method not allowed'
            },
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }

        self.assertEqual(lambda_handler(event, None), expects, "Incorrect response to improper method")


class TestEndpoints(unittest.TestCase):
    def test_query(self):
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


    # Ignore this test for now, I'll set up a proper test db later
    def test_cselect(self):
        event = {
            'httpMethod': 'POST',
            'path': f'/{profile}/cselect'
        }

        expects = {
            'statusCode': 200,
            'body': '[[1, "world"], [2, "boo"], [3, "hello"]]',
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }
        
        self.assertEqual(lambda_handler(event, None), expects, "Not returning correct select query response")


if (__name__ == "__main__"):
    unittest.main()
