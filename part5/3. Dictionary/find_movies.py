# Please write a function named find_movies(database: list, search_term: str), which processes the movie database created in the previous exercise. 
# The function should formulate a new list, which contains only the movies whose title includes the word searched for. 
# Capitalisation is irrelevant here. A search for ana should return a list containing both Anaconda and Management.

# An example of its use:

# database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
# {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
# {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

# my_movies = find_movies(database, "python")
# print(my_movies)

# [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]

def find_movies(database: list, search_term: str):
    movies_searched = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():
            movies_searched.append(movie)
    return movies_searched