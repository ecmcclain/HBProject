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
# model. db.create_all()
os.system('psql music < music.sql')

