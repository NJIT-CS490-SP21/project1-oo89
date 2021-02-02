# project1-oo89 Oscar Ojeda 

CS490

Music ToGo 


Heroku link: https://music-togo.herokuapp.com/

SET UP 

1- Create folder where is going to be the project.

2- Make all the files and directories that you will need as they are an folder to save "style.css", tamplates to save your html code and the other pyton files. 

3- pip install fask 

4- Install git->  git init 

5- I made the first commit before seting up my user.name and my email so before do git config --global user. name Oscar 

6- The same thing for your email but now instead of user.name uses user.email

7- After the commit do git add . 

8- Then I did git marge master because I already had a repo on Git-Hub, Also a git clone with my Git-Hub account, you also can use git log to see the logs. 

9- The Push the contente to the cloud uses git push, you can uses https link or also ssh connection where you have to save your privet key and uses your 
public key to add it to Git-Hub, in my case I uses https and each time I have to push something I have to enter user name and pass.

10- The other part is to create your keroku. npm install -g heroku and upload the content to there. It is important to have the requirements.txt 
document in order to success in your heroku connection. (pip freeze > requirements.txt).

11- Install gunicorn 

12- To push to heroku (git push heroku main:main)

13- In this part I need to save some env var, I installed pip install -U python-dotenv, and then update your requirements document.

14- Install python -m pip install requests.

15- Save the sensitive information as they are your Spotify secret and id and also the CLIENT ACCESS TOKEN from genius.

16- Then it is important to create .gitignore file to prevent that the sensitive information from getting uploaded to Git-Hub.

17- I had problem after doing all of this with the app on heroku, this happened because I didn't have the Procfile file, this 
needs to have (web: python app.py) app is the name of my main python file. 

Technical issues

As I explained before on #17 I had problems with heroku because the app didn't run. After create the file Procfile and adding the line of code 
I already explained the problem was solved. 

I also had problem with the env vars that we need to connect with the Spotofy and genius account. I look for a lot of information online and I create
the file key.env where I save then and I added this to gitignore file as I explained before. 

In addition to all of that I forgot to install the requests and I solved it by installing it as I explained #14 

--------------------------------------------------------------------------------------------------------------------------------------------
More Info each py files

app.py 

The file app.py is the principal file of the application where is imported all the library I need to run this project and the others I created. 
for more information check app.py file. 

Flask was initialized, I also create a list with my 7 artist id from Spotfy. You can have then by going to spotify and find your 
artist, then click on share, then copy spotify url. Following you will need to past to any text editor and copy the id from the link. Example: 
spotify:artist:2cy1zPcrFcXAJTP0APWewL --->> remove spotify:artist: 
inside def index(): I access to all of the information that will be comming from spotify file and genius file. Token, artis id, top tracks, track name, 
artis name, among other. 

Then I returned all the information that was need in the html file. 
At the end run the app on the localhost and port 8080 

spotify_api file 

As in app I imported all the libraries i need, I create a var to save the token spotify link. This app will be need after to create the complete link. 
The methods getAccessTokenSpt will uses the var from the env and create the authResp and then returned it. 

I save the url where is going to be the artis. 

Method getArtistTopTrack will need the token and artis id. 

Method getSongQueryString will need song name and artis name. 

genius_api 

I imported
from os import environ, from requests import get
as before I create a var to save the genius link for search

Method getTrackData





