import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
    tv_lst = ["La que se Avecina", "House of Cards", "Grey's Anatomy", "The Crown", "Aida"]
    pic_url = ["/static/LaQueSeAvecina1.jpeg","/static/House.jpeg","/static/Greys.jpeg","/static/TheCrown.jpeg","/static/Aida.jpeg"]
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