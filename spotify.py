import os
from dotenv import load_dotenv, find_dotenv
from random import choice 
from requests import get, post 
from decouple import config
import json

load_dotenv(find_dotenv())

SPT_AUTH_URL = 'https://accounts.spotify.com/api/token'

def getTokenSpt():
    
    sptClientId=os.getenv('CLIENT_ID')
    sptClientSecret=os.getenv('CLIENT_SECRET')
    
    authResp = post(SPT_AUTH_URL, {'grant_type': 'client_credentials', 'client_id': sptClientId, 'client_secret': sptClientSecret,})
    
    authResponseData = authResp.json()
    return authResponseData['access_token']

BASE_URL = 'https://api.spotify.com/v1/artists/'
PARAMS = {'market': 'US'}
SEARCH_URL = 'https://api.spotify.com/v1/search'

def searchSong(song_name, artist_name, accessToken):

    headers = {
        'Authorization': 'Bearer {token}'.format(token=accessToken)
    }
    response = get(SEARCH_URL + '?q=' + song_name + ' ' + artist_name + '&offset=0&type=track', headers=headers, params=PARAMS)
    data = response.json()
    print(data)
    #if data['tracks']['total'] == 0:
     #   return "No Song fund"
    #else:
    tracks = ""
    popularity = 0
    for track in data['tracks']['items']:
        if int(track['popularity']) > popularity:
            popularity = int(track['popularity'])
            tracks = track
            #print(track['name'] + 'popularity' + str(track['popularity']))
        else:
            continue
    #print(tracks)
    #print(tracks['artists'][0]['name'])
    return tracks


def topTrack(accessToken, artistId):
    
    #find the top track for the artist 
    headers = {
        'Authorization': 'Bearer {token}'.format(token=accessToken)
    }
    response = get(BASE_URL + artistId + '/top-tracks', headers=headers, params=PARAMS)
    data = response.json()

    return choice(data['tracks'])

def getSongQ(songName, artistName):
    
    goodSongName = songName.split('(')[0]
    return goodSongName + ' ' + artistName
