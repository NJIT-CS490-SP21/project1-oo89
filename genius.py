import os
from dotenv import load_dotenv, find_dotenv
from requests import get
from bs4 import BeautifulSoup
from lyricsgenius import Genius

BASE_URL = 'https://api.genius.com/search'

load_dotenv(find_dotenv())


def gTData(songSData):
    accessToken = os.getenv('GENIUS_ACCESS_TOKEN')
    headers = {'Authorization': 'Bearer ' + accessToken}

    params = {'q': songSData}
    response = get(BASE_URL, params=params, headers=headers)

    data = response.json()
    remoteSongInfo = data['response']['hits']
    #print(remoteSongInfo)
    def filterHits(hit):
        return hit['type'] == 'song'

    songHits = filter(filterHits, remoteSongInfo)
    return list(songHits)[0]['result']

def get_Lyric(artis_name, song_name):
    accessToken = os.getenv('GENIUS_ACCESS_TOKEN')
    genius = Genius(accessToken)
    try:
        song = genius.search_song(song_name, artis_name)
        song_lyric = song.lyrics
        if song_lyric is not None:
            return song_lyric
        else:
            return "No Lyrics for this song"
    except:
        return "No Lyrics fund, Sorry"




# I did this to have the song lyrics the first time I created this web but after I change to uses lyricsgenius from Genius.
"""
def scrapSongUrl(url):
    page = get(url)
    # print(page.text)
    html = BeautifulSoup(page.text, 'html.parser')
    # print(html)
    try:
        lyrics = html.find('div', class_="lyrics").get_text()
        # print(lyrics)
        return lyrics
    except AttributeError:
        print(" After using  this for month and working now is giving this error ERROR")
        return "Problem with lyrics = html.find('div', class_="").get_text() \n that was working before (BeautifulSoup)"

"""
