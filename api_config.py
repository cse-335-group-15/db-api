profile = "gwdeib01"

# Keep setting names inline with the kwarg names of the connect() method
try:
    import test # To see if the code is being run in the test environment
except ModuleNotFoundError: # If the module is not found, use prod data
    connection_info = {} # TODO: Add prod connection info
except ImportError: # If the modules is found, it will cause a circular import so an import error is thrown, use test data
    connection_info = {
    "host": "127.0.0.1",
    "user": "test",
    "passwd": "test1234",
    "db": "lab4",
    "port": 3306,
    "connect_timeout": 5
    }
    print("Config running as in test environment")

