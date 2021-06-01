import requests
import collections
import tweepy

api_key = 'hAfID2NpQ4HTtbkWABczjTdrz'
api_secret_key = 'RGBsBCk3vjrvQL7DjOTE5QbNdjZoGDH4g4s0EzQj8B7IzSc05e'
access_token = '56647684-9nnetvwluL4FS4lDuSaT5Idxdo84DHshD2yyew5oh'
access_token_secret = 'BbtZsdNoO6fjsTTOXB6hfd78H30liu0dg7u7Thxv8jeeE'

def OAuth():
    try:
        auth = tweepy.OAuthHandler(api_key,api_secret_key)
        auth.set_access_token(access_token,access_token_secret)
        return auth
    except Exception as e:
        return None

oauth = OAuth()

api = tweepy.API(oauth)

#api.update_status("First automated tweet using Python")
#print('tweet has been posted')

MovieResults = collections.namedtuple('MovieResult',"Title, Year, imdbID, Type, Poster")

search = input("What are you looking to watch?\n")
url = 'http://www.omdbapi.com/?s={}&apikey=b7fb6338'.format(search)

resp = requests.get(url)
resp.raise_for_status()
movies_data = resp.json()

#print(type(movies), movies)

movies_list = movies_data.get("Search")
#print(type(movies_list), movies_list)
#print (movies_list)
movies = [MovieResults(**md) for md in movies_list]


final=[]

for m in movies:
    a = ("{} {}".format(m.Title,m.Year))
    final.append(a)

final_movie_list = "\n".join(final)

print(len(final_movie_list))

api.update_status("Automated tweet via Tweepy API written using Python" + "\n" + final_movie_list)
print('tweet has been posted')
