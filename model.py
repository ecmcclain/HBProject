from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Data model for a user."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    explicit_content = db.Column(db.Boolean)

    tracks = db.relationship('Track', 
                            secondary='user_tracks', 
                            back_populates='users')
    sent_invitations = db.relationship('User', 
                            secondary='invitations', 
                            primaryjoin='and_(users.c.id==invitations.c.creating_user_id)', 
                            secondaryjoin='and_(invitations.c.joining_user_id==users.c.id)', 
                            back_populates='received_invitations')
    received_invitations = db.relationship('User', 
                            secondary='invitations', 
                            primaryjoin='and_(users.c.id==invitations.c.joining_user_id)', 
                            secondaryjoin='and_(invitations.c.creating_user_id==users.c.id)',
                            back_populates='sent_invitations')
    
    @classmethod
    def get_pending_invitations(cls, current_user):
        invitation_ids = db.session.query(Invitation.id).filter((current_user.id == Invitation.joining_user_id) & (Invitation.accepted==False) & (Invitation.declined ==False)).all()
        return [item for t in invitation_ids for item in t]

    @classmethod
    def get_accepted_invitations(cls, current_user):
        invitation_ids = db.session.query(Invitation.id).filter((current_user.id == Invitation.joining_user_id) & (Invitation.accepted==True) | (current_user.id == Invitation.creating_user_id) & (Invitation.accepted==True)).all()
        return [item for t in invitation_ids for item in t]

    @classmethod
    def get_other_user_by_invitation_id(cls, invitation_id):
        invitation = db.session.query(Invitation).filter(Invitation.id == invitation_id).first()
        if User.id == invitation.creating_user_id: 
            other_user_id = invitation.joining_user_id
        else: 
            other_user_id = invitation.creating_user_id
        
        other_user = db.session.query(User).filter(User.id == other_user_id).first()
        return other_user

    @classmethod
    def get_solo_playlists(cls, current_user):
        playlist = db.session.query(Playlist_Solo.id, Playlist_Solo.title).filter((current_user.id == Playlist_Solo.creating_user_id)).all()
        print(playlist)
        return playlist
        # print([item for t in playlist for item in t])
        # return [item for t in playlist for item in t]

    @classmethod
    def get_shared_playlists(cls, current_user):
        playlist = db.session.query(Playlist_Shared.id, Playlist_Shared.title).filter((current_user.id == Playlist_Shared.joining_user_id) | (current_user.id == Playlist_Shared.creating_user_id)).all()
        print(playlist)
        return playlist

class Track(db.Model):
    """Data model for a track."""

    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)
    artist_id = db.Column(db.String)
    spotify_track_id = db.Column(db.String)
    genre = db.Column(db.String)

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

class Invitation(db.Model):
    """Data model for an invitaion"""

    __tablename__ = 'invitations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creating_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    joining_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    accepted = db.Column(db.Boolean)
    declined = db.Column(db.Boolean)

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
