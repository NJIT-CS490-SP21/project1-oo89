from bs4 import BeautifulSoup
import flask
from flask import request
import os
from random import choice 
import json 
import requests
from spotify import getTokenSpt, topTrack, getSongQ, searchSong
from genius import gTData, get_Lyric
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

@app.route('/', methods=['GET', 'POST'])
def search():
   if request.method == 'POST':
          artist_name01 = (request.form.get('artist_name')).lower()
          song_name01 = (request.form.get('song_name')).lower()
          if not artist_name01 or not song_name01:
              return
          # token
          token = getTokenSpt()
          # Random artis ID
          artistId = choice(MY_ARTIST)

          data_from_search = searchSong(song_name01, artist_name01, token)
          try:
              trackName = data_from_search['name']
              artistName = data_from_search['artists'][0]['name']
          except:
              return flask.render_template("search.html")


          # the string to uses to get de genius data
          songString = getSongQ(trackName, artistName)
          # Genius data to have the Lyrics
          geniusData = gTData(songString)
          # I did this to have the song lyrics. OLD
          # myLyrics = scrapSongUrl(geniusData['url'])
          # I did this to have the song lyrics.
          myLyrics02 = get_Lyric(artistName, trackName)

          return flask.render_template(
            "index.html",
            songName = trackName,
            artistName = artistName,
            songPreviewUrl = data_from_search['preview_url'],
            songImageUrl = data_from_search['album']['images'][1]['url'],
            lyricsUrl = geniusData['url'],
            artistImageUrl = geniusData['primary_artist']['image_url'],
            myLyrics02 = myLyrics02
            )
          # otherwise handle the GET request
   return flask.render_template(
      "search.html")

@app.route('/play')
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
    # I did this to have the song lyrics. OLD
    #myLyrics = scrapSongUrl(geniusData['url'])
    # I did this to have the song lyrics.
    myLyrics02 = get_Lyric(artistName, trackName)


    # this is the return part
    return flask.render_template(
        "index.html",
        songName = trackName,
        artistName = artistName,
        songPreviewUrl = topTrackData['preview_url'],
        songImageUrl = topTrackData['album']['images'][1]['url'],
        lyricsUrl = geniusData['url'],
        artistImageUrl = geniusData['primary_artist']['image_url'],
        myLyrics02 = myLyrics02
        )


# server and ips to run the app 
app.run(
     port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
    ) 
    
