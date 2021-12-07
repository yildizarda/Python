import imdb
from imdb.parser.sql import titleVariations

moviesDB = imdb.IMDb()
movies = moviesDB.search_movie('Maze Runner')
id = movies[0].getID()
movie = moviesDB.get_movie(id)
title = movie['title']
year = movie['year']
rating = movie['rating']
directors = movie['directors']
casting = movie['cast']
print('Film Bilgileri: ')
print(f'{title} - {year}')
print(f'Oran: {rating}')
direcStr = ' '.join(map(str,directors))
print(f'Yönetmenler: {direcStr}')
actors = ', '.join(map(str,casting[0:5]))
print(f'Oyuncular : {actors}')

