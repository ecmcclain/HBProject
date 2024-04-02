from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Data model for a user."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    explicit_content = db.Column(db.Boolean)

    tracks = db.relationship('Track', secondary='user_tracks', back_populates='users')

class Track(db.Model):
    """Data model for a track."""

    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)
    spotify_track_id = db.Column(db.String)

    users = db.relationship('User', secondary='user_tracks', back_populates='tracks')
    playlists_shared = db.relationship('Playlist_Shared',secondary = 'shared_playlist_tracks', back_populates='tracks')
    playlists_solo = db.relationship('Playlist_Solo', secondary = 'solo_playlist_tracks',  back_populates='tracks')

class User_Track(db.Model):
    """Data model for a user track."""

    __tablename__ = 'user_tracks'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))
    listened_to = db.Column(db.Boolean)

class Playlist_Shared(db.Model):
    """Data model for a shared playlist."""

    __tablename__ = 'shared_playlists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creating_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    joining_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String)
    public = db.Column(db.Boolean)

    tracks = db.relationship('Track', secondary= 'shared_playlist_tracks', back_populates='playlists_shared')

class Playlist_Solo(db.Model):
    """Data model for a solo playlist."""

    __tablename__ = 'solo_playlists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creating_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String)
    public = db.Column(db.Boolean)

    tracks = db.relationship('Track', secondary ='solo_playlist_tracks',back_populates='playlists_solo')


class Playlist_Shared_Track(db.Model):
    """Data model for a shared playlist track."""

    __tablename__ = 'shared_playlist_tracks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('shared_playlists.id'))
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))


class Playlist_Solo_Track(db.Model):
    """Data model for a solo playlist track."""

    __tablename__ = 'solo_playlist_tracks'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('solo_playlists.id'))
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///music"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
