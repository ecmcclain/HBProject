# Lemme Show You a Song
Lemme Show You a Song is a full stack web application which allows Spotify users to generate playlists of recommended new songs. Users can also make blended playlists of new songs with other Spotify users customized to their combined tastes. The Spotify API was utilized to analyze users’ top songs and create playlists of song recommendations which exclude their top songs. Users can export playlists directly to their Spotify account and listen to playlists through the application. Users also have the option to load more data from Spotify to get even more customized recommendations and receive up-to-date Spotify data. I also used Chart.js to create visualizations of all users’ top ten genres, as well as each user’s individual top ten genres.

![Lemme Show You a Song Hompage](/static/homepage.png)

Lemme Show You a Song is a web app created by Lily McClain. Lily is a Applied Math major-turned-developer interested in open source projects. Lily is an avid Spotify user who loves discovering new music with friends. She created Lemme Show You a Song to make it easier to access customized recommendations of songs users might not have heard before. Lily's future updates to the app will allow more than two users to create playlists together, as well as let users edit the playlist songs directly in the app. 

## Table of Contents
* [Technologies Used](#technologiesused)
* [How to Locally Run Lemme Show You a Song](#run)
* [How to Use Lemme Show You a Song](#use)

## <a name="technologiesused"></a>Technologies Used

* Python
* Flask
* PostgresSQL
* SQLAlchemy
* Javascript/jQuery
* AJAX/JSON
* Jinja2
* HTML
* CSS
* Chart.js
* Bootstrap
* Spotify API
* Spotify Web Playback API

(dependencies are listed in requirements.txt)

## <a name="run"></a>How to Locally Run Lemme Show You a Song

Lemme Show You a Song has not yet been deployed, so here is how to run the app locally on your machine.

### Run the Lemme Show You a Song Flask App

  * Set up and activate a python virtualenv, and install all dependencies:
    * `pip3 install -r requirements.txt`
  * Make sure you have PostgreSQL running. Create a new database in psql named music:
  	* `createdb music;`
  * Create the tables in your database:
    * `python3 model.py`
  * Now, start up the flask server:
    * `python3 server.py`
  * Go to localhost:5000 to see the web app


## <a name="use"></a>How to Use Lemme Show You a Song

### Create an Account and Authorize the Spotify Connection `Create new Account`

You will need to input a unique username and a password—the app will flash a message if the username already exists. You will be redirected to the Spotify OAuth page were you will prompted to log into your Spotify account to authorize Lemme Show You a Song to access and make changes to your Spotify data. Please note, this may take a few seconds. 

### Log In to View Your Profile Page `Log In`

You will then be prompted to log in on the homepage. Once you log in you will be redirected to your profile, where you can start creating solo playlists and inviting other users to create blends. 

![Sample Profile Page](/static/profile.png)

If you have more playlists than are visible in the top row, you can select `Show More Playlists` to see all of your playlists or `Show Less` to see only the top few. 

![Sample Expanded Profile Page](/static/profileExpanded.png)

### Select a Playlist to Start Listening
Playlists can be played directly in the app, the title of the playlist can be edited and the playlist can be exported externally to your Spotify account as either public or private. 

![Sample Playlist](/static/playlist.png)

### Navigating Playlists
Select the top play button or any song's play button to start the web playback in the app. If you are prompted to Authenticate, please do so and come back to the playlist you would like to play from your profile. The currently playing song is bolded and a music note is added in place of the play button. As you move the cursor around, the track numbers turn into play buttons as you hover over each song. 

![Sample Playing Playlist](/static/playlistPlaying.png)

### Refreshing Playlists to Get More New Music
If you would like to get a refreshed playlist with another user or a new playlist for yourself select `Make Fresh Playlist?` If the app is loading, a loading graphic will appear under the cursor to let you know.  

![Loading Cursor](/static/loading.png)

### Managing Invitation Options
On your profile page, you can send invitation to create blends to other users by username, view invitations you have sent, and respond to invitations from other users. If there is an invitation pending your review the green `Pending` badge will let you know. An accepted invitation will display the playlist on both users' profiles. 

![Loading Cursor](/static/invitations.png)

### Viewing Your Top Tracks and Genres
You can also view and listen to your top tracks from your profile page. 

![Loading Cursor](/static/topTracks.png)

You can also view a graphic of your top genres. Select the button in the top right to toggle between viewing all users' top ten genres and your own top ten genres. 

![Loading Cursor](/static/topGenres.png)

### Refreshing Spotify Data and Loading More Data from Spotify
You then have the option to refresh your Spotify data to get the most updated information or load more data from Spotify. If you opt to load more data, you will be alerted that this will take a few minutes. However, by loading more data, you are allowing the application to make even better recommendations for new songs. You will also be able to view your top 100 tracks if you load more data. 

![Loading Cursor](/static/dataOptions.png)

## <a name="author"></a>Author
Lily McClain is a software engineer in Brooklyn, NY.