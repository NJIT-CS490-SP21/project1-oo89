from bs4 import BeautifulSoup
import flask
import os
from random import choice 
import json 
import requests
from spotify import getTokenSpt, topTrack, getSongQ 
from genius import gTData, scrapSongUrl
from decouple import config

app = flask.Flask(__name__)

# My favorite artist ids list 
MY_ARTIST = [
    '0vR2qb8m9WHeZ5ByCbimq2', # Reik 
    '5Pwc4xIPtQLFEnJriah9YJ', # OneRepublic
    '4VMYDCV2IEDYJArk749S6m', # Daddy Yankee 
    '4wLXwxDeWQ8mtUIRPxGiD6', # Marc Anthony 
    '6eUKZXaKkcviH0Ku9w2n3V', # Ed Sheeran 
    '1XXUv8GRyRqOXVuDwB5QaS', # Leoni Torres
    '2cy1zPcrFcXAJTP0APWewL', # Gente de Zona
    ]


@app.route('/')

def index():
    
    # token
    token = getTokenSpt()
    #Random artis ID 
    artistId = choice(MY_ARTIST)
    #With the token and artist id to get the top tracks. 
    topTrackData = topTrack(token, artistId)
    #from the top track data obtain the track name accessing to that with name. 
    trackName = topTrackData['name']
    # the JSON return will help to have the artis name. 
    artistName = topTrackData['artists'][0]['name']
    # the string to uses to get de genius data 
    songString = getSongQ(trackName, artistName)
    # Genius data to have the Lyrics 
    geniusData = gTData(songString)
    # I did this to have the song lyrics.
    myLyrics = scrapSongUrl(geniusData['url'])
    
    # this is the return part 
    return flask.render_template(
        "index.html",
        songName = trackName, 
        artistName = artistName, 
        songPreviewUrl = topTrackData['preview_url'],
        songImageUrl = topTrackData['album']['images'][1]['url'],
        lyricsUrl = geniusData['url'],
        artistImageUrl = geniusData['primary_artist']['image_url'],
        myLyrics = myLyrics
        )


# server and ips to run the app 
app.run(
     port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
    ) 
    
