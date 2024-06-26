"""CRUD operations."""

from model import db, User, Track, User_Track, Playlist_Shared, Playlist_Solo, Playlist_Shared_Track, Playlist_Solo_Track, Invitation

def create_user(username, password, explicit_content, spotify_user_id):
    """Create a user"""
    user = User(username=username, password=password, explicit_content=explicit_content, spotify_user_id=spotify_user_id)

    return user

def return_all_users():
    """Return a list of all users"""
    users = db.session.query(User).all()

    return users

def get_user_by_username(username):
    """Return a user by username"""
    user = db.session.query(User).filter(User.username == username).first()

    return user

def get_user_by_id(id):
    """Return a user by ID"""
    user = db.session.query(User).get(id)

    return user

def create_track(title, artist, artist_id, spotify_track_id, genre):
    """Create a track"""
    track = Track(title=title, artist=artist, artist_id=artist_id, spotify_track_id=spotify_track_id, genre=genre)

    return track

def get_track_by_spotify_id(track_id):
    """Get a track by Spotify track ID"""
    track = db.session.query(Track).filter_by(spotify_track_id=track_id).first()

    return track

def return_all_tracks():
    """Return a list of all tracks"""
    tracks = db.session.query(Track).all()

    return tracks

def get_users_spotify_track_ids(user):
    """Return a list of the Spotify track IDs for a given user"""
    spotify_track_ids = db.session.query(Track.spotify_track_id).filter((Track.id == User_Track.track_id) & (User_Track.user_id==user.id)).all()
    spotify_track_ids = [value for (value,) in spotify_track_ids]

    return spotify_track_ids

def get_users_spotify_tracks(user):
    """Return a list of tracks for a given user"""
    spotify_tracks = db.session.query(Track).filter((Track.id == User_Track.track_id) & (User_Track.user_id==user.id)).all()

    return spotify_tracks

def get_users_spotify_artists_ids(user):
    """Return a list of the Spotify artist IDs for a given user"""
    spotify_artists_ids = db.session.query(Track.artist_id).filter((Track.id == User_Track.track_id) & (User_Track.user_id==user.id)).all()
    spotify_artists_ids = [value for (value,) in spotify_artists_ids]

    return spotify_artists_ids

def create_user_track(user, track, listened_to):
    """Create a user track"""
    user_track = User_Track(user_id=user.id, track_id=track.id, listened_to=listened_to)

    return user_track

def create_shared_playlist(creating_user_id, joining_user_id, title, public):
    """Create a shared playlist"""
    shared_playlist = Playlist_Shared(creating_user_id=creating_user_id, joining_user_id= joining_user_id, title=title, public=public)

    return shared_playlist

def return_all_shared_playlists():
    """Return a list of all shared playlists"""
    shared_playlists = db.session.query(Playlist_Shared).all()

    return shared_playlists

def create_solo_playlist(creating_user_id, title, public):
    """Create a solo playlist"""
    solo_playlist = Playlist_Solo(creating_user_id=creating_user_id, title=title, public=public)

    return solo_playlist 

def return_all_solo_playlists():
    """Return a list of all solo playlists"""
    solo_playlists = db.session.query(Playlist_Solo).all()

    return solo_playlists

def get_solo_playlists_by_name(name):
    """Get a solo playlist by it's name"""
    solo_playlists = db.session.query(Playlist_Solo).filter(Playlist_Solo.title.like(f'{name}%')).all()

    return solo_playlists

def get_solo_playlist_by_id(playlist_id):
    """Get a solo playlist by playlist ID"""
    solo_playlist = db.session.query(Playlist_Solo).filter(Playlist_Solo.id == playlist_id).first()

    return solo_playlist

def get_shared_playlist_by_id(playlist_id):
    """Get a shared playlist by playlist ID"""
    shared_playlist = db.session.query(Playlist_Shared).filter(Playlist_Shared.id == playlist_id).first()

    return shared_playlist

def get_shared_playlists_by_name(name):
    """Get a shared playlist by name"""
    shared_playlists = db.session.query(Playlist_Shared).filter(Playlist_Shared.title.like(f'{name}%')).all()

    return shared_playlists

def create_playlist_shared_track(playlist, track):
    """Create a shared playlist track"""
    playlist_shared_track = Playlist_Shared_Track(playlist_id=playlist.id, track_id=track.id)

    return playlist_shared_track 

def create_playlist_solo_track(playlist, track):
    """Create a solo playlist track"""
    playlist_solo_track = Playlist_Solo_Track(playlist_id=playlist.id, track_id=track.id)

    return playlist_solo_track 

def create_invitation(creating_user_id, joining_user_id, accepted, declined):
    """Create an invitation"""
    invitation = Invitation(creating_user_id=creating_user_id, joining_user_id= joining_user_id, accepted=accepted, declined=declined)

    return invitation
    
def get_invitation_by_id(invitation_id):
    """Get an invitation by invitation ID"""
    invitation = db.session.query(Invitation).get(invitation_id)

    return invitation

def get_invitation_by_joining_user(joining_user):
    """Get a list of all invitations for the given the joining user"""
    invitation = db.session.query(Invitation).filter(Invitation.joining_user_id==joining_user.id).all()

    return invitation

def get_playlist_spotify_track_ids(playlist):
    """Get a list of the Spotify track IDs for the given playlist"""
    spotify_track_ids = [track.spotify_track_id for track in playlist.tracks]

    return spotify_track_ids