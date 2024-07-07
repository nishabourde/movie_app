# api/utils.py

import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings

def fetch_movies(page=1):
    url = 'https://demo.credy.in/api/v1/maya/movies/'
    response = requests.get(
        url,
        auth=HTTPBasicAuth(settings.MOVIE_API_USERNAME, settings.MOVIE_API_PASSWORD),
        params={'page': page},
        timeout=5
    )
    response.raise_for_status()
    return response.json()
