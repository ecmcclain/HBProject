import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

#drop and create the database
os.system("dropdb music")
os.system('createdb music')

#connect to the server
model.connect_to_db(server.app)

#for TESTING
# model. db.create_all()

#load the seed data into the database
os.system('psql music < music.sql')

