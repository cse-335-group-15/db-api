from utils import endpoint

# Use endpoint decorator to add an endpoint to the API.
# 
# The path will be whatever is after the profile name in the URL.
# So if the URL is /gwdeib01/query, the path will be 'query'.
# 
# The decorator will pass arguments from the body of the request to the function based on what it needs.
# So add parameters as neccesary to the function signature, just make sure the website actually sends those parameters.
#
# The function should return a query that will be executed on the database.
#
# Do not call these elsewhere in the code, they should only be called by the lambda_handler.

@endpoint(path='query')
def handle_query(query):
    return query

@endpoint(path='insert')
def handle_insert():
    return None

@endpoint(path='Cselect')
def handle_complex_select(body):
    query = '''
    Select name as movie_name, first_name as star_first_name, last_name as star_last_name 
    FROM movie Inner join cast on movie.StarID = cast.ID 
        Inner join reviews on movie.ReviewsID = reviews.ReviewsID 
    Where Score > (select AVG(Score) FROM reviews)
    '''
    return query

@endpoint(path='delete')
def handle_delete(comparison, input):
    query = {'delete * from movies where ', comparison, '=', input}
    return query

@endpoint(path='update')
def handle_update(votes, score, movie_id):
    query = f'update table ratings set votes = {votes}, score = {score} where id = (SELECT review_id FROM movies WHERE id = {movie_id})'
    return query
