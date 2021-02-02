import os
from dotenv import load_dotenv, find_dotenv
from requests import get

BASE_URL = 'https://api.genius.com/search'

load_dotenv(find_dotenv())

def getTrackData(songQuery):
    
    accessToken=os.getenv('GENIUS_ACCESS_TOKEN')
    headers = {'Authorization': 'Bearer ' + accessToken}

    params = {'q': songQuery}
    response = get(BASE_URL, params=params, headers=headers)

    data = response.json()
    hits = data['response']['hits']

    def filterHits(hit):
        return hit['type'] == 'song'

    songHits = filter(filterHits, hits)
    return list(songHits)[0]['result']
