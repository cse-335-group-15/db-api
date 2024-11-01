from lambda_function import lambda_handler
from api_config import profile

# DO NOT INCLUDE THIS FILE IN PUBLICATION TO AWS LAMBDA

def test_lambda_handler():
    query = 'SELECT * FROM employees WHERE position = \\"Developer\\"'

    event = {
        'httpMethod': 'POST',
        'path': f'/{profile}/select',
        'body': f'{{ "query": "{query}"}}'
    }
    print(lambda_handler(event, None))

if (__name__ == "__main__"):
    test_lambda_handler()