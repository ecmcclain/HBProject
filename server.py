# from jinja2 import StrictUndefined
from flask import Flask, redirect, request, session, render_template, jsonify, flash
from model import connect_to_db, db
import crud

import urllib.parse, datetime

import os
import requests

app = Flask(__name__)

CLIENT_KEY = os.environ['CLIENT_KEY']
CLIENT_ID = os.environ['CLIENT_ID']
REDIRECT_URI = os.environ['REDIRECT_URI']

app.secret_key = "SECRETMCCLAINMONKEY"

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')

@app.route('/users')
def make_new_user():

    return render_template('new_user.html')

@app.route('/users', methods=['POST'])
def create_account():

    username = request.form.get('username')
    password = request.form.get('password')
    explicit_content = bool(request.form.get('explicit_content'))

    if crud.get_user_by_username(username) is not None:
        flash('Account already exists with that username. Please log in or use a different username.')
    else:
        flash('Account created, please log in.')
        user = crud.create_user(username, password, explicit_content)
        db.session.add(user)
        db.session.commit()

    return redirect('/')

@app.route('/login', methods = ['POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    user = crud.get_user_by_username(username)

    if user is not None:
        if user.password == password:
            flash('Logged in!')
            session['current_user'] = user.id
            return redirect('/authorize')
    
    flash('Email or password incorrect, please try again.') 

    return redirect('/')

@app.route('/authorize')
def authorize():

    scope = 'user-read-private user-read-email playlist-read-private, user-library-read, user-top-read'

    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True
    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    return redirect(auth_url)

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})
    
    if 'code' in request.args:
        print("I GOT HEREEEEEE")

        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_KEY
        }

        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()

        print(token_info)

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.datetime.now().timestamp() + token_info['expires_in'] # 3600 seconds (1 day) 

        return redirect('/get_user_data')

@app.route('/get_user_data')
def get_user_data():
    if 'access_token' not in session: 
        return redirect('/authorize')

    if datetime.datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')
    
    headers = {
        'Authorization': f"Bearer {session['access_token']}"
    }

    temp = requests.get(API_BASE_URL + 'me', headers=headers)
    spotify_user_id = temp.json()['id']
    session['spotify_user_id'] = spotify_user_id

    # Get all the playlists of the current user
    playlists_url = API_BASE_URL + f'users/{spotify_user_id}/playlists?limit=50&offset=0'

    # while playlists_url is not None:
    #     response = requests.get(playlists_url, headers=headers)
    #     playlists = response.json()

    #     print(playlists['next'])
    #     # playlists_url = playlists['next']
    #     playlists_url=None

    #     #Get all the tracks off of each of the user's playlists
    #     items = playlists["items"]
    #     for playlist in items:
    #         #Check that the owner of the playlist is the user
    #         if playlist['owner']['display_name'] == spotify_user_id:
    #             playlist_id = playlist['id']
    #             tracks_url = API_BASE_URL+ f'playlists/{playlist_id}/tracks'
                
    #             while tracks_url is not None: 
    #                 response = requests.get(tracks_url, headers=headers)
    #                 tracks = response.json()
    #                 tracks_url = tracks['next']

    #                 for track in tracks['items']:
    #                     title = track['track']['name']
    #                     artist = track['track']['artists'][0]['name']
    #                     spotify_track_id = track['track']['id']
    #                     if crud.get_track_by_spotify_id(spotify_track_id) is None:
    #                         new_track = crud.create_track(title, artist, spotify_track_id)
    #                         db.session.add(new_track)

    #  # Get all the saved tracks of the current user
    # saved_tracks_url = API_BASE_URL + f'me/tracks'

    # while saved_tracks_url is not None:
    #     response = requests.get(saved_tracks_url, headers=headers)
    #     saved_tracks = response.json()

    #     saved_tracks_url = saved_tracks['next']
    #     print(saved_tracks['total'])
    #     # saved_tracks_url=None

    #     #Get all the tracks off of each of the user's shared tracks
    #     items = saved_tracks["items"]
    #     for track in items:
    #         title = track['track']['name']
    #         artist = track['track']['artists'][0]['name']
    #         spotify_track_id = track['track']['id']
    #         if crud.get_track_by_spotify_id(spotify_track_id) is None:
    #             new_track = crud.create_track(title, artist, spotify_track_id)
    #             db.session.add(new_track)

    top_tracks_url = API_BASE_URL + f'me/top/tracks?time_range=long_term'

    while top_tracks_url is not None:
        response = requests.get(top_tracks_url, headers=headers)
        top_tracks = response.json()

        # top_tracks_url = top_tracks['next']
        print(top_tracks['total'])
        top_tracks_url=None

        #Get all the tracks off of each of the user's shared tracks
        items = top_tracks["items"]
        for track in items:
            title = track['name']
            artist = track['artists'][0]['name']
            spotify_track_id = track['id']
            # print(title)
            if crud.get_track_by_spotify_id(spotify_track_id) is None:
                print(crud.get_track_by_spotify_id(spotify_track_id))
                new_track = crud.create_track(title, artist, spotify_track_id)
                db.session.add(new_track)

    db.session.commit()
    return jsonify(top_tracks)

@app.route('/refresh-token')
def get_access_token():
    if 'refresh_token' not in session: 
        return redirect('/authorize')
    
    if datetime.datetime.now().timestamp() > session['expires_at']:
        req_body = {
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_KEY
        }

        response = requests.post(TOKEN_URL, data=req_body)

        new_token_info = response.json()

        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.datetime.now().timestamp() + new_token_info['expires_in'] # 3600 seconds (1 day) 

        return redirect('/get_user_data')

if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)

    app.run(host="0.0.0.0")