import os
from dotenv import load_dotenv, find_dotenv
from requests import get
from bs4 import BeautifulSoup

BASE_URL = 'https://api.genius.com/search'

load_dotenv(find_dotenv())

def gTData(songSData):
    
    accessToken=os.getenv('GENIUS_ACCESS_TOKEN')
    headers = {'Authorization': 'Bearer ' + accessToken}

    params = {'q': songSData}
    response = get(BASE_URL, params=params, headers=headers)

    data = response.json()
    remoteSongInfo = data['response']['hits']
    
    def filterHits(hit):
        return hit['type'] == 'song'

    songHits = filter(filterHits, remoteSongInfo)
    return list(songHits)[0]['result']

# I did this to have the song lyrics. 
def scrapSongUrl(url):
        page = get(url)
        html = BeautifulSoup(page.text, 'html.parser')
        lyrics = html.find('div', class_='lyrics').get_text()
        
        return lyrics

