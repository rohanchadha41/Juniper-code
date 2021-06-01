import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")


search = input("Which movie are you looking to watch today?\n")
url = 'https://movieservice.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)
resp.raise_for_status()


movie_data = resp.json()
#print(type(movie_data), movie_data)
movies_list = movie_data.get('hits')
#print(movies_list)
#print(resp.status_code)
#print(type(resp.text))
movies = []

for md in movies_list:
    m = MovieResult(imdb_code = md.get('imdb_code'),
                    title = md.get('title'),
                    director= md.get('director'),
                    duration = md.get('duration'),
                    year = md.get('year', 0),
                    rating = md.get('rating', 0),
                    imdb_score  = md.get('imdb_score', 0.0),
                    keywords = md.get('keywords '),
                    genres = md.get('genres'))

    movies.append(m)

for m in movies:
    print("{}-----{}".format(m.year, m.title))


#print(type(movies))
