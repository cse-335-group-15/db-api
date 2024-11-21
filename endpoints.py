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
def handle_insert(crew_id, first_name, middle_name, last_name):
    
    query = {'Insert into crew (id, first_name, middle_name, last_name) values ', 
             '(', crew_id, ', ', first_name, ', ', middle_name, ', ', last_name, ');'}
    
    return query

@endpoint(path='insert')
def handle_insert(movie_id, name, rating, genre_id, year, company_id, director_id, writer_id, star_id, review_id):

    query = {'Insert into movies (id, name, rating, genre_id, release_year, company_id, director_id, writer_id, star_id, review_id) ', 
             'values (', movie_id, ', ', name, ', ', rating, ', ', genre_id, ', ', year, ', ', company_id, ', ', 
             director_id, ', ', writer_id, ', ', star_id, ', ', review_id, ');'}

    return query

@endpoint(path='insert')
def handle_insert(company_id, company, country):
    
    query = {'Insert into Studios (id, company, country) values ', 
             '(', company_id, ', ', company, ', ', country, ');'}    
    
    return query

@endpoint(path='insert')
def handle_insert(review_id, score, votes):
    
    query = {'Insert into Reviews (id, score, votes) values ', 
             '(', review_id, ', ', score, ', ', votes, ');'}    
    
    return query

@endpoint(path='insert')
def handle_insert(genre_id, genre):
    
    query = {'Insert into Reviews (id, genre) values ', 
             '(', genre_id, ', ', genre, ');'}    
    
    return query

@endpoint(path='cselect')
def handle_complex_select():
    query = '''
    Select name as movie_name, first_name as star_first_name, last_name as star_last_name 
    FROM movies Inner join crew on movies.star_id = crew.id 
        Inner join reviews on movies.id = reviews.id 
    Where Score > (select AVG(Score) FROM reviews)
    '''
    return query

@endpoint(path='delete')
def handle_delete(comparison, input):
    query = {'delete * from movies where ', comparison, '=', input}
    return query

@endpoint(path='update')
def handle_update(votes, score, movie_id):
    query = {'update table reviews set votes = ', votes, 'score = ' , score, 'where id = (SELECT review_id FROM movies WHERE id = ', movie_id, ')'}
    return query

@endpoint(path='select')
def handle_select():
    query = {'''Select movies.id, name, Rating, G.genre as genre, Year, studios.Company as company, Studios.Country as country, D.full_name as Director_name, W.full_name as Writer_name, S.full_name as Star_name, Score, Votes
                FROM  movies
                inner join crew S on movies.Star_id = S.id
                inner join crew W on movies.Writer_id = W.id
                inner join crew D on movies.Director_id = D.id
                inner join studios on movies.Company_id = studios.id
                inner join genres G on movies.Genre_id = G.id
                inner join Reviews on movies.Review_id = Reviews.id'''}
    return query

@endpoint(path='find_duos')
def handle_find_duos():
    query ={'''with duos as( select Director.full_name as Director_name, Star.full_name as Star_name, count(*) 
                from movies 
                inner join crew Director on movies.Director_id = Director.id
                inner join crew Star on movies.Star_id = Star.id
                group by Director_id, Star_id
                having count(*))

               select *from duos'''}
    return query