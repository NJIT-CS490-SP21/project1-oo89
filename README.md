#project1-oo89 Oscar Ojeda 

CS490

Music ToGo 


Heroku link: https://music-togo.herokuapp.com/

##SET UP 
1. Create a folder where is going to be the project.
2. Make all the files and directories that you will need as they are a folder to save "style.css", templates to save your HTML code, and the other python files. 
3. pip install flask 
4. Install git->  git init 
5. I made the first commit before setting up my user.name and my email so before do git config --global user. name Oscar 
6. The same thing for your email but now instead of user.name uses user.email
7. After the commit do git add . or add the files independently. 
8. Then I did git marge master because I already had a repo on Git-Hub, Also a git clone with my Git-Hub account, you also can use git log to see the logs. 
9. To Push the contents to the cloud uses git push, you can use an HTTPS link or also ssh connection where you have to save your private key and uses your 
the public key to add it to Git-Hub, in my case I used HTTPS, and each time I have to push something I have to enter the user name and pass.
10. The other part is to create your Heroku. npm install -g heroku and upload the content to there. It is important to have the requirements.txt 
document in order to succeed in your Heroku connection. (pip freeze > requirements.txt) this will add too much information you could also select what is needed
for Heroku to be added.
11. Install gunicorn
12. To push to Heroku (git push heroku main:main)
13. In this part I need to save some env var, I installed pip install -U python-dotenv, and then update your requirements document.
14. Install python -m pip install requests.
15. Save the sensitive information as they are your Spotify secret and id and also the CLIENT ACCESS TOKEN from genius.
16. Then it is important to create a .gitignore file to prevent that sensitive information from getting uploaded to Git-Hub.
17. I had a problem after doing all of this with the app on Heroku, this happened because I didn't have the Procfile file, this 
needs to have (web: python app.py) app is the name of my main python file. 
18. Important to save the environ var also in Heroku. Go to your app, settings, Reveal Config Vars and save them there in order for Heroku to use it. 

## Run Application
1. Run command in terminal `python app.py`
2. Preview web page in browser '/'

##Technical issues

1. As I explained before on #17 I had problems with Heroku because the app didn't run. After creating the file Procfile and adding the line of code 
I already explained the problem was solved. (web: python app.py) 

2. I also had a problem with the env vars that we need to connect with the Spotify and genius account. I look for a lot of information online and I create
the file key.env where I save then and I added this to gitignore file as I explained before, but the key.env file didn't work so I finally used only .env to save those
important vars. Using load_dotenv(find_dotenv()) and importing from dotenv import load_dotenv, find_dotenv will help the system to find each .env files. 


3. In addition to all of that I forgot to install the requests and I solved it by installing it as I explained #14. 
I had all of these problems as I started the project before the conferences were given by the professor. 

4. Another problem with Heroku as I didn’t save the Config Vars in there so the application didn’t work. The solution is explained in #18 

5. Also I would love to clarify that some times git-hub do weird thing as one time even having the gitignore file with the file name it was uploaded the env file.
6. This is why is very important to pay extra attention to that. 

--------------------------------------------------------------------------------------------------------------------------------------------
##More Info for each py files

#app.py 

The file app.py is the principal file of the application where is imported all the libraries I need to run this project and the others I created. 
for more information check app.py file. 

I added from bs4 import BeautifulSoup that helped with scrapSongUrl method to uses the Lyrics. To install is uses $ pip install beautifulsoup4. 

Flask was initialized, I also create a list with my 7 artist id from Spotify. You can have then by going to Spotify and find your artist, then click on share, then copy Spotify URL. Following you will need to paste to any text editor and copy the id from the link. Example: 
spotify:artist:2cy1zPcrFcXAJTP0APWewL --->> remove spotify:artist: 

Inside def index(): I access all of the information that will be coming from the Spotify file and genius file. Token, artist id, top tracks, track name, 
artist name, among others. 

Then I returned all the information that was needed in the HTML file. 
At the end run the app on the localhost and port 8080 

#spotify

As in-app I imported all the libraries I need, I create a var to save the token Spotify link. This app will be needed after, to create the complete link. 
The methods getTokenSpt will uses the var from the env and create the authResp and then returned it. 

I save the URL where is going to be the artist at Spotify. 

Method topTrack will need the token and artist id. As always we create headers that will have the access token and will be required to use the API. 
In response, we will use get to obtain top track information from Spotify. This response will need to be saved in data as a JSON and then having that is going to be easy
to access the data we want has in this case the track randomly selected.  

Method getSongQ will need the song name and artist name to clean the string. 

#genius

From os import environ, from requests import get
as before I create a var to save the genius link for search

Same as in Spotify you will need a token to do the authentication, it will be saved in accessToken. 
This whole method will help us to get the Genius data that we need. 

#Extra 
I also used this data to show in the HTML the actual Lyrics of each song that is loaded. In the future, 
I am thinking to put the actual part of the lyrics while the song is playing like a karaoke. 

# External Link I used for help. 

1. https://stmorse.github.io/journal/spotify-api.html -> where I learned most of the part to acces to the Spotify API. 
2. https://docs.genius.com/.                          -> Genius api Documentation’s. 
3. https://material-ui.com/customization/color/#2014-material-design-color-palettes -> Colors to use. 
4. https://developer.spotify.com/documentation/web-api/reference/ -> Very important documentation from Spotify where you can learn almost everything. 
5. https://jsonformatter.curiousconcept.com/           -> I also used this to see the code. 
6. https://stackoverflow.com/questions/40454368/linux-command-to-get-location-of-env-file -> Linux command to get location of env file. 
7. https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/  -> work with environment vars. 
8. https://stackoverflow.com/questions/9492249/render-a-string-in-html-and-preserve-spaces-and-linebreaks -> to render a string in html. It was used for the Lyrics part.
9. https://stackoverflow.com/questions/24917983/make-text-scrollable-within-div -> How to make the text scollable. 
10. https://websitesetup.org/web-safe-fonts-html-css/   -> Best web safe fonts html and css.
11. https://git-scm.com/doc                             -> Git documentation.
12. https://support.tunecore.com/hc/en-us/articles/360040325651-How-to-Find-my-Spotify-Artist-ID -> find Spotify artist id.
13. https://www.cyberciti.biz/faq/linux-list-all-environment-variables-env-command/ -> List off all environment var in Linux. 
14. https://stackoverflow.com/questions/25436312/gitignore-not-working -> gitignore not working. 
15. https://training.github.com/downloads/github-git-cheat-sheet/  -> Github and git cheat sheet.
16. https://devcenter.heroku.com/categories/reference             -> Heroku documentation. 
17. https://stackoverflow.com/questions/41804507/h14-error-in-heroku-no-web-processes-running -> Error with Heroku. 
18. https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app/17322636#17322636 -> Run your app in debug mode. 
19. https://docs.google.com/document/d/1WAE9kj8E9T_L2OaNsfivLlPgmZR1EvKIThHo7U_b0pA/edit -> Project orientation. 
20. https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow -> Spotify Client credentials flow. 
21. https://www.crummy.com/software/BeautifulSoup/bs4/doc/ -> from bs4 import BeautifulSoup






