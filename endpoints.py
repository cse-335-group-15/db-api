from utils import endpoint

# Use endpoint decorator to add an endpoint to the API.
# 
# The path will be whatever is after the profile name in the URL.
# So if the URL has /gwdeib01/query, the path will be 'query'.
# 
# The decorator will pass arguments from the body of the request to the function based on what it needs.
# So add parameters as neccesary to the function signature, just make sure the website actually sends those parameters.
#
# The function should return a query that will be executed on the database.
#
# Do not call these elsewhere in the code, they should only be called by the lambda_handler.

# Custom query handler
@endpoint(path='query')
def handle_query(query):
    return query

# Views
@endpoint(path='cselect')
def handle_complex_select():
    query = '''
Select name as movie_name, first_name as star_first_name, last_name as star_last_name 
FROM movies Inner join crew on movies.star_id = crew.id 
    Inner join reviews on movies.id = reviews.id 
Where Score > (select AVG(Score) FROM reviews);
    '''
    return query

@endpoint(path='select')
def handle_select():
    query = '''
SELECT M.id, M.name, M.rating, G.genre AS genre, M.release_year, S.company AS company, S.country AS country, DC.full_name AS Director_name, WC.full_name AS Writer_name, SC.full_name AS Star_name, R.score, R.votes
FROM movies M
INNER JOIN crew SC ON M.star_id = SC.id
INNER JOIN crew WC ON M.writer_id = WC.id
INNER JOIN crew DC ON M.director_id = DC.id
INNER JOIN studios S ON M.company_id = S.id
INNER JOIN genres G ON M.genre_id = G.id
INNER JOIN reviews R ON M.review_id = R.id;
    '''
    return query

@endpoint(path='find_duos')
def handle_find_duos():
    query = '''
with duos as( select CONCAT(Director.first_name, " ", Director.last_name) as Director_name, CONCAT(Star.first_name, " ", Star.last_name) as Star_name, count(*) 
from movies 
inner join crew Director on movies.Director_id = Director.id
inner join crew Star on movies.Star_id = Star.id
group by Director_id, Star_id
having count(*))

select *from duos
    '''
    return query

# Select for table views
@endpoint(path='table')
def handle_table(table_name):
    query = f'select * from {table_name};'

# Inserts for all tables
@endpoint(path='insert')
def handle_insert(id, first_name, middle_name, last_name):
    
    query = f'Insert into crew (id, first_name, middle_name, last_name) values ({id}, \'{first_name}\', \'{middle_name}\', \'{last_name}\');'
    
    return query

@endpoint(path='insert')
def handle_insert(id, name, rating, genre_id, release_year, company_id, director_id, writer_id, star_id, review_id):

    query = f'Insert into movies (id, name, rating, genre_id, release_year, company_id, director_id, writer_id, star_id, review_id) values ({id}, \'{name}\', \'{rating}\', {genre_id}, {release_year}, {company_id}, {director_id}, {writer_id}, {star_id}, {review_id});'

    return query

@endpoint(path='insert')
def handle_insert(id, company, country):
    
    query = f'Insert into studios (id, company, country) values ({id}, \'{company}\', \'{country}\');'    
    
    return query

@endpoint(path='insert')
def handle_insert(id, score, votes):
    
    query = f'Insert into reviews (id, score, votes) values ({id}, {score}, {votes});'    
    
    return query

@endpoint(path='insert')
def handle_insert(id, genre):
    
    query = f'Insert into genres (id, genre) values ({id}, \'{genre}\');'    
    
    return query

# Updates for each table
@endpoint(path='update')
def handle_update(votes, score, movie_id):
    query = f'update table reviews set votes = {votes}, score = {score} where id = (SELECT review_id FROM movies WHERE id = {movie_id})'
    return query

# Deletes for each table
@endpoint(path='delete')
def handle_delete(comparison, input):
    query = f'delete from movies where {comparison} = {input}'
    return query

