#from requests import get, post 
from os import environ 
from random import choice 
from requests import get, post 
from decouple import config
import json
#from key import CLIENT_ID, CLIENT_SECRET 

SPT_AUTH_URL = "https://accounts.spotify.com/api/token"

# GET https://accounts.spotify.com/authorize

# Meth to get api token 
def getAccessTokenSpt():
    
    sptClientId = environ['CLIENT_ID'] # I changed to config because an error environ
    sptClientSecret = environ['CLIENT_SECRET']
    
    authResp = post(SPT_AUTH_URL, {'grant_type': 'client_credentials', 'client_id': sptClientId, 'client_secret': sptClientSecret})
    
    authResponseData = authResp.json()
    return authResponseData["access_token"]


BASE_URL = "https://api.spotify.com/v1/artists/"
PARAMS = {'market': 'US'}

def getArtistTopTrack(accessToken, artistId):
    #find the top track for the artist 

    headers = {
        'Authorization': 'Bearer {token}'.format(token=accessToken)
    }
    response = get(BASE_URL + artistId + '/top-tracks', headers=headers, params=PARAMS)
    data = response.json()

    return choice(data['tracks'])

def getSongQueryString(songName, artistName):
    """Returns query string for Genius API search call"""

    goodSongName = songName.split('(')[0]
    return goodSongName + ' ' + artistName
    
    

