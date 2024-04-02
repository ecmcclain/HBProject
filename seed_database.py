import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb music")
os.system('createdb music')
model.connect_to_db(server.app)
model.db.create_all()

#create fake users and tracks
for n in range(10):
    username = f'user{n}@test.com' 
    password = 'test'

    user = crud.create_user(username, password, True)

    # TODO: create a user here
    model.db.session.add(user)
    # model.db.session.commit()

    # TODO: create 10 tracks for the user
    user_tracks = []

    for j in range(10):
        title = f'texas holdem{j}' 
        artist = f'Beyonce{j}'
        spotify_track_id = n+100 
        track = crud.create_track(title,artist,spotify_track_id)
        
        model.db.session.add(track)
        model.db.session.commit()
        
        user_track = crud.create_user_track(user, track, True)
        user_tracks.append(user_track)
    
    model.db.session.add_all(user_tracks)

model.db.session.commit()
