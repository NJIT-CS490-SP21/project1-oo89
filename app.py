import flask
import os
import random
import spotify_api
import genius_api
from os import getenv

app = flask.Flask(__name__)

MY_ARTIST_IDS = [
    '0vR2qb8m9WHeZ5ByCbimq2', # Reik 
    '5Pwc4xIPtQLFEnJriah9YJ', # OneRepublic
    '4VMYDCV2IEDYJArk749S6m', # Daddy Yankee 
    '4wLXwxDeWQ8mtUIRPxGiD6', # Marc Anthony 
    '6eUKZXaKkcviH0Ku9w2n3V', # Ed Sheeran 
    '1XXUv8GRyRqOXVuDwB5QaS'  # Leoni Torres
    ]


@app.route('/')

def index():
    
    # This part is to have a base from the last homework I will remove it after I finish with the other. 
    tv_lst = ["La que se Avecina", "House of Cards", "Grey's Anatomy", "The Crown", "Aida"]
    pic_url = ["/static/LaQueSeAvecina1.jpeg","/static/House.jpeg","/static/Greys.jpeg","/static/TheCrown.jpeg","/static/Aida.jpeg"]
    
    # Spotify info 
    #access_token = get_access_token()
    #artist_id = choice(ARTIST_IDS)
    #top_track_data = get_artist_top_tracks(access_token, artist_id)
    
    return flask.render_template(
        "index.html",
        tv_lst = tv_lst,
        lenght= len(tv_lst),
        pic_url = pic_url, 
        pic_leng = len(pic_url)
        )



app.run(
     port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
    ) 