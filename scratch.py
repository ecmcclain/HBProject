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
    print(session)
    print(session['created_user_id'])
    if 'created_user_id' in session: 
        created_user = crud.get_user_by_id(session['created_user_id'])
    else: 
        created_user = crud.get_user_by_id(session['current_user'])

    top_tracks_url = API_BASE_URL + f'me/top/tracks?time_range=long_term'

    while top_tracks_url is not None:
        response = requests.get(top_tracks_url, headers=headers)
        top_tracks = response.json()

        top_tracks_url = top_tracks['next']
        print(top_tracks['total'])
        top_tracks_url=None

        #Get all the tracks off of each of the user's shared tracks
        items = top_tracks["items"]
        for track in items:
            title = track['name']
            artist = track['artists'][0]['name']
            artist_id = track['artists'][0]['id']
            spotify_track_id = track['id']
            if crud.get_track_by_spotify_id(spotify_track_id) is None:
                print(crud.get_track_by_spotify_id(spotify_track_id))
                new_track = crud.create_track(title, artist, artist_id, spotify_track_id)
                db.session.add(new_track)
                db.session.commit()
                new_user_track = crud.create_user_track(created_user,new_track,listened_to=True)
                db.session.add(new_user_track)
    db.session.commit()

    if 'created_user_id' in session: 
        flash('Account created, please log in.')
        del session['created_user_id']
        return redirect('/')
    else: 
        flash('User data was updated')
        return render_template('user_profile.html', user = created_user)






<button id="togglePlay">Toggle Play</button>
<button className="btn-spotify" id="togglePrevious">Previous</button>
<button className="btn-spotify" id="toggleNext">Next</button>

<script src="https://sdk.scdn.co/spotify-player.js"></script>
<script>
  window.onSpotifyWebPlaybackSDKReady = () => {
      const token = '{{ access_token }}';
      const player = new Spotify.Player({
          name: 'Web Playback SDK Quick Start Player',
          getOAuthToken: cb => { cb(token); },
          volume: 0.5
      });
      
      // Ready
      player.addListener('ready', ({ device_id }) => {
          console.log('Ready with Device ID', device_id);
      });

      // Not Ready
      player.addListener('not_ready', ({ device_id }) => {
          console.log('Device ID has gone offline', device_id);
      });

      player.addListener('initialization_error', ({ message }) => {
          console.error(message);
      });

      player.addListener('authentication_error', ({ message }) => {
          console.error(message);
      });

      player.addListener('account_error', ({ message }) => {
          console.error(message);
      });

      document.getElementById('togglePlay').onclick = function() {
        player.togglePlay();
      };
      
      document.getElementById('togglePrevious').onclick = function() {
        player.previousTrack();
      };

      document.getElementById('toggleNext').onclick = function() {
        player.nextTrack();
        console.log(player.nextTrack());
      };

      player.connect();
  }
</script>


   <h3>ACCEPTED INVITATIONS</h3>

    {% for invitation_id in user.get_accepted_invitations(user) %}
      <form action = "/playlist/{{user.get_other_user_by_invitation_id(invitation_id).id}}" method = 'POST'>
        Playlist with {{user.get_other_user_by_invitation_id(invitation_id).username}}
        <button type="submit" name="invitation" value="accept">View Playlist</button>
      </form>
    {% endfor %}





<!-- <p>
Allow explicit content? 
<input type="checkbox" name="explicit_content" value="True" id="yes">
<label for="yes">Yes</label>
<input type="checkbox" name="explicit_content" value="False" id="no">
<label for="no">no</label>
</p> -->


# if 'access_token' not in session: 
    #     return redirect('/authorize')
    # if datetime.datetime.now().timestamp() > session['expires_at']:
    #     return redirect('/refresh-token')
    # headers = {
    #     'Authorization': f"Bearer {session['access_token']}",
    # }

    # genres = {}
    # temp_string= ''
    # for inner_index, track in enumerate(sample(all_tracks,100)):
    #     print(inner_index)
    #     if temp_string.count(',')> 40:
    #         break
    #     if len(track.spotify_track_id) > 4 and track.artist_id not in temp_string :
    #         temp_string = temp_string+","+track.artist_id 
    # print(temp_string)
    # temp = requests.get(API_BASE_URL + f'artists?ids={temp_string[1:]}', headers=headers)
    # artists = temp.json()
    # print(artists)
    # for artist in artists['artists']:
    #     for genre in artist['genres']:
    #         genres[f'{genre}'] = genres.get(f'{genre}', 0) +1
    # print(genres)

#FORMER USER PROFILE ACCORDION
    <div class="row"> 
    <div class="accordion" id="accordionExample">
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingOne">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
            <b>Create a Playlist with Another User</b>
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse open" aria-labelledby="headingOne">
          <div class="accordion-body">
            <div class="row">
              <form action = /blend method = 'POST'>  
                <p>
                  Please invite the other user by username: <input type="text" name="other-user">
                  <input type="submit" value="Send Invitation">
                </p>
              </form>
            </div>     
           </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingTwo">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            <b id="pending_badge">
              Review Pending Invitations
            </b>
          </button>
        </h2>
        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo">
          <div id ='pending' class="accordion-body">
            {% if user.get_pending_invitations(user) != [] %}
            {% for invitation_id in user.get_pending_invitations(user) %}
              <form action = "/update_invitation/{{ invitation_id }}" method = 'POST'>
                <li>Invitation from {{ user.get_other_user_by_invitation_id(invitation_id).username }}
                  <button type="submit" name="invitation" value="accept">Accept</button>
                  <button type="submit" name="invitation" value="decline">Decline</button>
                </li>
              </form>
            {% endfor %}
            {% else %}
              You are up to date! No pending invitations.
            {% endif %}
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingThree">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
            <b>View Sent Invitations</b>
          </button>
        </h2>
        <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree">
          <div class="accordion-body">
            Invitations sent to: 
            <ul>
            {% for users in user.sent_invitations %}
              <li>{{ users.username }}</li>
            {% endfor %}
          </ul>
           </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="headingFour">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
              <b>View Your Top Tracks</b>
            </button>
          </h2>
          <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour">
            <div class="accordion-body">
              <ol>
              {% for track in user.tracks %}
                {% if loop.index < 21 %}
                <li>{{ track.title }}, {{ track.artist }}</li>
                {% endif %}
              {% endfor %}
            </ol>
             </div>
            </div>
          </div>
      </div>
    </div>