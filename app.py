import flask
import os
from random import choice 
import json 
import requests
from spotify_api import getAccessTokenSpt, getArtistTopTrack, getSongQueryString 
from genius_api import getTrackData
from os import getenv
from decouple import config 


app = flask.Flask(__name__)



# My favorite artist ids list 
MY_ARTIST_IDS = [
    '0vR2qb8m9WHeZ5ByCbimq2', # Reik 
    '5Pwc4xIPtQLFEnJriah9YJ', # OneRepublic
    '4VMYDCV2IEDYJArk749S6m', # Daddy Yankee 
    '4wLXwxDeWQ8mtUIRPxGiD6', # Marc Anthony 
    '6eUKZXaKkcviH0Ku9w2n3V', # Ed Sheeran 
    '1XXUv8GRyRqOXVuDwB5QaS', # Leoni Torres
    '2cy1zPcrFcXAJTP0APWewL',  # Gente de Zona
    ]


@app.route('/')

def index():
    
    """Spotify info"""  
    accessToken = getAccessTokenSpt()
    artistId = choice(MY_ARTIST_IDS)
    topTrackData = getArtistTopTrack(accessToken, artistId)
    
    trackName = topTrackData['name']
    artistName = topTrackData['artists'][0]['name']
    
    songQueryString = getSongQueryString(trackName, artistName)
    geniusData = getTrackData(songQueryString)
    
    return flask.render_template(
        "index.html",
        songName = trackName, 
        artistName = artistName, 
        songPreviewUrl = topTrackData['preview_url'],
        songImageUrl = topTrackData['album']['images'][1]['url'],
        lyricsUrl = geniusData['url'],
        artistImageUrl = geniusData['primary_artist']['image_url']
        )



app.run(
     port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
    ) 