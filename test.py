from main import lambda_handler

def test_lambda_handler():
    # Test insert
    event = {
        'httpMethod': 'POST',
        'path': '/gwdeib01/insert',
        'body': {
            "name": "John Doe", 
            "email": "JohnDoe@louisville.edu"
        }
    }
    assert lambda_handler(event) == "Hello World"
