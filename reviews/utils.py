import requests
from django.conf import settings

def fetch_movie_details(movie_title):
    url = f'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': settings.TMDB_API_KEY,
        'query': movie_title
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]
        
        return None