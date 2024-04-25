# from jinja2 import StrictUndefined
from flask import Flask, redirect, request, session, render_template, jsonify, flash, json
from model import connect_to_db, db
from random import sample, choice
from operator import itemgetter

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

    print(session)

    return render_template('homepage.html')

@app.route('/users')
def make_new_user():
    """Show the create user page. """
    return render_template('new_user.html')

@app.route('/users', methods=['POST'])
def create_account():
    """Create a new user"""
    username = request.form.get('username')
    password = request.form.get('password')
    # explicit_content = bool(request.form.get('explicit_content'))
    explicit_content = True

    #If the given username already exists, ask user to input a new username
    if crud.get_user_by_username(username.lower()) is not None:
        flash('Account already exists with that username. Please log in or use a different username.')
    #create a new user and add the user to the session. Set the created user id in the cookie session 
    else:
        user = crud.create_user(username.lower(), password, explicit_content)
        db.session.add(user)
        db.session.commit()
        session['created_user_id'] = user.id

    return redirect('/authorize')

@app.route('/login', methods = ['POST'])
def login():
    """Log an already created user into the cookie session"""

    username = request.form.get('username')
    password = request.form.get('password')

    user = crud.get_user_by_username(username)

    #if the given username and password are valid, set the current user id in the cookie session and show the user's profile
    if user is not None:
        if user.password == password:
            flash('Logged in!')
            session['current_user'] = user.id

            #check that the access token exists and is not expired and authorize or refresh if so 
            if 'access_token' not in session: 
                return redirect('/authorize')
            if datetime.datetime.now().timestamp() > session['expires_at']:
                return redirect('/refresh-token')
            headers = {
                'Authorization': f"Bearer {session['access_token']}"
            }

            #get the user's Spotify user id
            temp = requests.get(API_BASE_URL + 'me', headers=headers)
            spotify_user_id = temp.json()['id']
            session['spotify_user_id'] = spotify_user_id

            return render_template('user_profile.html', user = user)
    
    #if the given username and password are not valid, flash message and redirect to the homepage
    flash('Email or password incorrect, please try again.') 
    
    return redirect('/')

@app.route('/profile')
def display_profile():
    """Display the current user's profile"""
    #if there is a current user set in the cookie session (ie logged in) display the user profile
    if 'current_user' in session:
        user = crud.get_user_by_id(session['current_user'])
        return render_template('user_profile.html', user = user)
    #otherwise, ask the user to log in
    else:
        flash('Please log in to access your profile.')
        return redirect('/')

@app.route('/log_out')
def log_out():
    """Log the current user out"""
    #if there is a current user and/or spotify_user_id in the cookie session, delete them and redirect to the homepage
    if 'current_user' in session:
        del session['current_user']
    if 'spotify_user_id' in session: 
        del session['spotify_user_id']
    if 'load_more' in session: 
        del session['load_more']
    flash("Logged out.")
    return redirect('/')

@app.route('/playlist', methods = ['POST'])
def create_solo_playlist():
    """Create a solo playlist for the logged in user"""
    #get the cookie session's current user
    user = crud.get_user_by_id(session['current_user'])

    #create a solo playlist and add it to the session
    similar_playlists = crud.get_solo_playlists_by_name(f'{user.username} Playlist') 
    if similar_playlists == []:
        title = f'{user.username} Playlist'
    else:
        title = f'{user.username} Playlist {len(similar_playlists)+1}'

    playlist = crud.create_solo_playlist(user.id, title, False)
    db.session.add(playlist)
    db.session.commit()

    #check that the access token exists and is not expired and authorize or refresh if so 
    if 'access_token' not in session: 
        return redirect('/authorize')
    if datetime.datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')
    headers = {
        'Authorization': f"Bearer {session['access_token']}"
    }

    #get the user's top 20 seed artists and tracks from Spotify
    user_seed_artists = crud.get_users_spotify_artists_ids(user)[:20]
    user_seed_tracks = crud.get_users_spotify_track_ids(user)[:20]

    #continue to request recommended songs until the length of the new playlist is 20 tracks
    while len(playlist.tracks) < 20:
        #request 50 recommended songs given 5 randomly chosen seed artists from the user's top 20 artists 
        solo_playlist_url = API_BASE_URL + f'recommendations?seed_artists={choice(user_seed_artists)},{choice(user_seed_artists)},{choice(user_seed_artists)},{choice(user_seed_artists)},{choice(user_seed_artists)}&limit=50'
        response = requests.get(solo_playlist_url, headers=headers)
        playlist_tracks = response.json()

        #check that the given track from the recommended Spotify playlist is not already in the user's tracks, and if not, add it to the playlist
        for track in playlist_tracks['tracks']:
            if len(playlist.tracks) < 20:
                track_id = track['id']
                if crud.get_track_by_spotify_id(track_id) not in user.tracks:
                    title = track['name']
                    artist = track['artists'][0]['name']
                    artist_id = track['artists'][0]['id']
                    temp = requests.get(track['artists'][0]['href'], headers=headers)
                    artist_temp = temp.json()
                    if artist_temp['genres'] != []:
                        genre = choice(artist_temp['genres'])
                    else: 
                        genre = None

                    new_track = crud.create_track(title, artist, artist_id, track_id, genre)
                    db.session.add(new_track)
                    db.session.commit()

                    playlist_track = crud.create_playlist_solo_track(playlist,new_track)
                    db.session.add(playlist_track)
                    db.session.commit()
    
    #display the playlist
    print(jsonify(crud.get_playlist_spotify_track_ids(playlist)))
    return redirect(f'/view_solo_playlist/{playlist.id}')

@app.route('/playlist/<other_id>', methods = ['POST'])
def create_shared_playlist(other_id):
    """Create a shared playlist for the logged in user"""

    #get the session's current user and the other user for the shared playlist
    current_user = crud.get_user_by_id(session['current_user'])
    other_user = crud.get_user_by_id(other_id)
    
    #create the shared playlist and add it to the session
    similar_playlists = crud.get_shared_playlists_by_name(f'{current_user.username} & {other_user.username} Playlist') 
    if similar_playlists == []:
        title = f'{current_user.username} & {other_user.username} Playlist'
    else:
        title = f'{current_user.username} & {other_user.username} Playlist {len(similar_playlists)+1}'

    playlist = crud.create_shared_playlist(current_user.id, other_id, title, False)
    db.session.add(playlist)
    db.session.commit()

    #check that the access token exists and is not expired and authorize or refresh if so 
    if 'access_token' not in session: 
        return redirect('/authorize')
    if datetime.datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')
    headers = {
        'Authorization': f"Bearer {session['access_token']}"
    }

    #continue to request recommended songs until the length of the new playlist is 20 tracks
    while len(playlist.tracks) < 20:
        for user in [current_user, other_user]:
            #set the user and other user for each user
            if user == current_user:
                other = other_user
            else:
                other = current_user

            #get the user's top 20 seed artists and tracks from Spotify
            user_seed_artists = crud.get_users_spotify_artists_ids(user)
            user_seed_tracks = crud.get_users_spotify_track_ids(user)

            #request 50 recommended songs given 5 randomly chosen seed artists from the user's top 20 artists 
            shared_playlist_url = API_BASE_URL + f'recommendations?seed_artists={choice(user_seed_artists)},{choice(user_seed_artists)},{choice(user_seed_artists)},{choice(user_seed_artists)},{choice(user_seed_artists)}&limit=50'
            response = requests.get(shared_playlist_url, headers=headers)
            playlist_tracks = response.json()

            #check that the given track from the recommended Spotify playlist is not already in the other user's tracks, and if not, add it to the playlist
            for track in playlist_tracks['tracks']:
                if len(playlist.tracks) < 10 or (user == other_user and len(playlist.tracks) < 20):
                    track_id = track['id']
                    if crud.get_track_by_spotify_id(track_id) not in other.tracks:
                        title = track['name']
                        artist = track['artists'][0]['name']
                        artist_id = track['artists'][0]['id']
                        temp = requests.get(track['artists'][0]['href'], headers=headers)
                        artist_temp = temp.json()
                        if artist_temp['genres'] != []:
                            genre = choice(artist_temp['genres'])
                        else: 
                            genre = None
                        new_track = crud.create_track(title, artist, artist_id, track_id, genre)
                        db.session.add(new_track)
                        db.session.commit()

                        playlist_track = crud.create_playlist_shared_track(playlist,new_track)
                        db.session.add(playlist_track)
                        db.session.commit()
    #display the playlist
    
    return redirect(f'/view_shared_playlist/{playlist.id}')

@app.route('/view_solo_playlist/<playlist_id>')
def view_solo_playlist(playlist_id):
    """View already created playlist"""
    #get the cookie session's current user
    user = crud.get_user_by_id(session['current_user'])

    #create a solo playlist and add it to the session
    playlist = crud.get_solo_playlist_by_id(playlist_id)
    
    #display the playlist
    print(jsonify(crud.get_playlist_spotify_track_ids(playlist)))
    return render_template('playlist.html', user=user, playlist=playlist, access_token = session['access_token'], playlist_tracks = crud.get_playlist_spotify_track_ids(playlist))

@app.route('/view_shared_playlist/<playlist_id>')
def view_shared_playlist(playlist_id):
    """View already created playlist"""
    #get the cookie session's current user
    user = crud.get_user_by_id(session['current_user'])

    #create a solo playlist and add it to the session
    playlist = crud.get_shared_playlist_by_id(playlist_id)
    
    #display the playlist
    print(jsonify(crud.get_playlist_spotify_track_ids(playlist)))
    return render_template('playlist.html', user=user, playlist=playlist, access_token = session['access_token'], playlist_tracks = crud.get_playlist_spotify_track_ids(playlist))

@app.route('/view_top_tracks')
def view_top_tracks():
    """View already created playlist"""
    #get the cookie session's current user
    user = crud.get_user_by_id(session['current_user'])

    #create a solo playlist and add it to the session
    playlist = crud.create_solo_playlist(user.id, "Top Tracks", False)
    db.session.add(playlist)
    for track in user.tracks:
        playlist_track = crud.create_playlist_solo_track(playlist, track)
        db.session.add(playlist_track)
    db.session.commit()

    
    #display the playlist
    # print(jsonify(crud.get_playlist_spotify_track_ids(playlist)))
    return render_template('playlist.html', user=user, playlist=playlist, access_token = session['access_token'], playlist_tracks = crud.get_playlist_spotify_track_ids(playlist))


@app.route('/blend', methods = ['POST'])
def create_blend():
    """Create an invitation from one user to another"""
    
    #get the current user from the cookie session and the other user from the form
    current_user = crud.get_user_by_id(session['current_user'])
    other_user = crud.get_user_by_username(request.form.get('other-user'))

    #if the other user does not exist, ask the user to ask the other user to create an account
    if other_user is None:
        flash('User not found—please invite user to create an account.')
        return render_template('user_profile.html', user = current_user)

    #if the other user has already recieved an invitation from this user, flash the message
    if other_user in current_user.sent_invitations:
        flash('This user already has a pending blend invitation. Please wait for them to accept or view the playlist.')
        return render_template('user_profile.html', user = current_user)

    #otherwise, create the invitation and add it to the session
    invitation = crud.create_invitation(current_user.id,other_user.id,False,False)
    db.session.add(invitation)
    db.session.commit()
   
    flash('User successfully invite to join your blend.')

    return render_template('user_profile.html', user = current_user)

@app.route('/update_invitation/<invitation_id>', methods=["POST"])
def update_invitation(invitation_id):
    """Update the invitation with the user's response"""

    #get the current user and the invitation from the cookie session 
    user = crud.get_user_by_id(session['current_user'])
    invitation = crud.get_invitation_by_id(invitation_id)
    other_user = crud.get_user_by_id(invitation.creating_user_id)

    #get the users response from the form
    value = request.form.get('invitation')

    #update the invitation with the user's response
    if value == 'accept':
        flash(f'You accepted invitation from {other_user.username}')
        invitation.accepted = True
        db.session.commit()
        return redirect(f'/playlist/{other_user.id}', code=307)
    if value == 'decline':
        flash(f'You declined invitation from {other_user.username}')
        invitation.declined = True
        db.session.commit()
        return render_template('user_profile.html', user=user)


@app.route('/export_playlist', methods=['POST'])
def playback():

    user = crud.get_user_by_id(session['current_user'])
    print(session)

     #check that the access token exists and is not expired and authorize or refresh if so 
    if 'access_token' not in session: 
        return redirect('/authorize')
    if datetime.datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')
    headers = {
        'Authorization': f"Bearer {session['access_token']}",
        'Content-Type': 'application/json',
    }

    playlist_id = request.form.get('playlist_id_shared')
    if playlist_id is None:
        playlist_id = request.form.get('playlist_id_solo')
        playlist = crud.get_solo_playlist_by_id(playlist_id)
    else:
        playlist= crud.get_shared_playlist_by_id(playlist_id)

    spotify_user_id = session['spotify_user_id']

    req_body = json.dumps({
        'name': f'{playlist.title}',
        'public': f'{playlist.public}',
    })

    export_url = API_BASE_URL + f'users/{spotify_user_id}/playlists'
    response = requests.post(export_url, data=req_body, headers=headers)
    play = response.json()

    spotify_playlist_id = play['id']

    playlist_spotify_track_ids = crud.get_playlist_spotify_track_ids(playlist)
    playlist_spotify_track_id = ['spotify:track:' + id for id in  playlist_spotify_track_ids]

    req_body = json.dumps({
        'uris': playlist_spotify_track_id,
    })

    add_tracks_url = API_BASE_URL + f'playlists/{spotify_playlist_id}/tracks'
    response = requests.post(add_tracks_url, data=req_body, headers=headers)
    play = response.json()
    flash('Playlist exported to Spotify.')

    return render_template('playlist.html', user=user, playlist=playlist, access_token = session['access_token'], playlist_tracks = crud.get_playlist_spotify_track_ids(playlist))

@app.route('/rename_solo_playlist/<playlist_id>', methods=['POST'])
def rename_solo_playlist(playlist_id):
    new_name = request.form.get('new_name')
    playlist = crud.get_solo_playlist_by_id(playlist_id)
    playlist.title = new_name
    db.session.commit()
    print(playlist.title)
    return redirect(f'/view_solo_playlist/{playlist_id}')

@app.route('/rename_shared_playlist/<playlist_id>', methods=['POST'])
def rename_shared_playlist(playlist_id):
    new_name = request.form.get('new_name')
    playlist = crud.get_shared_playlist_by_id(playlist_id)
    playlist.title = new_name
    db.session.commit()
    print(playlist.title)
    return redirect(f'/view_shared_playlist/{playlist_id}')

@app.route('/make_public', methods=['POST'])
def make_public():
    playlist_id = request.form.get('playlist_id_shared')
    if playlist_id is None:
        playlist_id = request.form.get('playlist_id_solo')
        playlist_shared = False
        playlist = crud.get_solo_playlist_by_id(playlist_id)
    else:
        playlist_shared = True
        playlist= crud.get_shared_playlist_by_id(playlist_id)

    if not playlist.public:
        playlist.public = True
    else:
        playlist.public = False
    db.session.commit()

    if playlist_shared:
        return redirect(f'/view_shared_playlist{playlist_id}') 
    return redirect(f'/view_solo_playlist/{playlist_id}')

@app.route('/load_more')
def load_more():

    if 'current_user' in session:
        session["load_more"] = True
        return redirect('/authorize')
    else:
        flash('Please log in to access data options.')
        return redirect('/')

@app.route('/get_genres.json')
def get_genres():
    all_tracks = crud.return_all_tracks()

    genres = {}
    for track in all_tracks:
        genre = track.genre
        genres[f'{genre}'] = genres.get(f'{genre}', 0) +1

    genres = dict(sorted(genres.items(), key=itemgetter(1), reverse=True)[:10])

    all_genres = []
    all_genres.append({'name': list(genres.keys()),
                        'count': list(genres.values())})
    print(all_genres)  
    print("should see graph")
    return jsonify({'data': all_genres})

@app.route('/user_genres.json')
def user_genres():
    current_user = crud.get_user_by_id(session['current_user'])
    all_tracks = crud.get_users_spotify_tracks(current_user)
    print(all_tracks)

    genres = {}
    for track in all_tracks:
        genre = track.genre
        genres[f'{genre}'] = genres.get(f'{genre}', 0) +1

    genres = dict(sorted(genres.items(), key=itemgetter(1), reverse=True)[:10])

    all_genres = []
    all_genres.append({'name': list(genres.keys()),
                        'count': list(genres.values())})
    print(all_genres)  
    print("should see graph user")
    return jsonify({'data': all_genres})





@app.route('/authorize')
def authorize():
    """Complete Spotify's OAuth for the user"""

    if 'current_user' not in session and 'created_user_id' not in session:
        flash('Please log in to access data options.')
        return redirect('/')

    scope = 'user-read-private user-read-email playlist-read-private user-library-read user-top-read streaming user-modify-playback-state playlist-modify-public playlist-modify-private'

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
    """Spotify OAuth callback route"""
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})
    
    if 'code' in request.args:

        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_KEY
        }

        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.datetime.now().timestamp() + token_info['expires_in'] # 3600 seconds (1 day) 

        return redirect('/get_user_data')

@app.route('/get_user_data')
def get_user_data():
    """Get the user's track data from Spotify"""
    print("GETTTING USER DATA.....")
    print(session)

    #check that the access token exists and is not expired and authorize or refresh if so 
    if 'access_token' not in session: 
        return redirect('/authorize')
    if datetime.datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')
    headers = {
        'Authorization': f"Bearer {session['access_token']}"
    }

    #get the user's Spotify user id
    temp = requests.get(API_BASE_URL + 'me', headers=headers)
    spotify_user_id = temp.json()['id']
    session['spotify_user_id'] = spotify_user_id

    #get the current user or the created user, if the user has just been created
    if 'created_user_id' in session: 
        created_user = crud.get_user_by_id(session['created_user_id'])
    else: 
        created_user = crud.get_user_by_id(session['current_user'])

    #get the user's top tracks from Spotify
    top_tracks_url = API_BASE_URL + f'me/top/tracks?time_range=long_term'

    count = 0 
    while top_tracks_url is not None and count < 10:
        count = count + 1
        response = requests.get(top_tracks_url, headers=headers)
        top_tracks = response.json()

        if "load_more" in session or len(created_user.tracks) > 20:
            top_tracks_url = top_tracks['next']
            print(top_tracks['total'])
        else:
            top_tracks_url=None

        #Get all the tracks off of each of the user's shared tracks
        items = top_tracks["items"]
        for track in items:
            title = track['name']
            artist = track['artists'][0]['name']
            artist_id = track['artists'][0]['id']
            spotify_track_id = track['id']
            temp = requests.get(track['artists'][0]['href'], headers=headers)
            artist_temp = temp.json()
            if artist_temp['genres'] != []:
                genre = choice(artist_temp['genres'])
            else: 
                genre = None
            if crud.get_track_by_spotify_id(spotify_track_id) is None:
                print(crud.get_track_by_spotify_id(spotify_track_id))
                new_track = crud.create_track(title, artist, artist_id, spotify_track_id, genre)
                db.session.add(new_track)
                db.session.commit()
                new_user_track = crud.create_user_track(created_user,new_track,listened_to=True)
                db.session.add(new_user_track)
    db.session.commit()

    #delete the created user id from the session if it exists and ask the user to log in
    if 'created_user_id' in session: 
        flash('Account created, please log in.')
        del session['created_user_id']
        return redirect('/')
    #confirm data was updated and render the user's profile
    else: 
        flash('User data was updated.')
        return redirect('/profile')

@app.route('/refresh-token')
def get_access_token():
    """Refresh the Spotify access token"""
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
       
    if 'current_user' not in session: 
        return redirect('/get_user_data')
    return redirect('/profile')


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)

    app.run(host="0.0.0.0")