import random


# Napravite listu s deset omiljenih filmova, sortirajte ih abecedno i ispisite ih na ekran

favorite_movies = [
    'The Godfather',
    'Pulp Fiction',
    'The Dark Knight',
    'Forrest Gump',
    'The Shawshank Redemption',
    'The Silence of the Lambs',
    'Fight Club',
    'Goodfelas',
    'Inception',
    'The Matrix'

]

favorite_movies.sort()

for movie in favorite_movies:
    print(movie)

print()


# Unos ocjena za unešene filmove ----------------------------------------------------------------------

# grade_list = []
# for movie in favorite_movies: 
#     input_grade = float(input(f'Unesite ocjenu za {favorite_movies[favorite_movies.index(movie)]} '))
#     grade_list.append(input_grade)
#     print()

# print()
# print(f'Prosjecna ocjena top 10 filmova je: {sum(grade_list) / len(grade_list)}')

# Godine izlaska pojedinih filmova ---------------------------------------------------------------------

release_date = [
    '1987',
    '1999',
    '1997',
    '2001',
    '2003',
    '1995',
    '1988',
    '2007',
    '2005',
    '2010'
]

movies_info = []
for movie in favorite_movies:
    movies_info.append([movie, release_date[favorite_movies.index(movie)]])
    
print(movies_info)

movie = None
for movie in movies_info:
    print(movie[0], movie[1])


# Dodavanje zanra filmovima -----------------------------------------------------------------------------
    
genres = [
    'Action',
    'Thriller',
    'Action',
    'SF',
    'Comedy',
    'Drama',
    'Action',
    'SF',
    'Thriller',
    'Action'
]

print()

movie = None
for movie in movies_info:
    movie.append(genres[movies_info.index(movie)])

print(movies_info)
print()

# Lista fimova koji bi se ponovno gledali -------------------------------------------------------------------

movies_to_rewatch = []

movies_to_watch = [
    'The Silence of the Lambs',
    'Fight Club',
    'Goodfelas',
    'Inception',
    'The Matrix'
]

movie = None
for movie in movies_info:
    for element in movies_to_watch:
        if element == movie[0]:
            movies_to_rewatch.append(element)

print(movies_to_rewatch)

movies_to_rewatch2 = []

movie = None
element = None
for movie in movies_info:
    movies_to_rewatch2.extend(element for element in movies_to_watch if element in movie)

print(movies_to_rewatch2)
print()

# Dodavanje trajanja filma ------------------------------------------------------------------------

movie = None
for movie in movies_info:
    duration = random.randint(60, 180)
    movie.append(duration)

movie = None
duration_sum = 0
for movie in movies_info:
    duration_sum += movie[3]

average_duration = duration_sum / len(movies_info)

print(average_duration)
print(movies_info)













