from database import db, app, Artist, Album, Track, User, Playlist

with app.app_context():
    artist1 = Artist(name="Radiohead")
    artist2 = Artist(name="Daft Punk")
    db.session.add_all([artist1, artist2])
    album1 = Album(name="OK Computer", artist=artist1)
    album2 = Album(name="Discovery", artist=artist2)
    db.session.add_all([album1, album2])
    track1 = Track(name="Paranoid Android", length=386, album=album1)
    track2 = Track(name="One More Time", length=320, album=album2)
    db.session.add_all([track1, track2])
    user1 = User(name="Alice")
    playlist1 = Playlist(name="Favorites", description="My favorite songs")
    playlist1.users.append(user1)
    playlist1.tracks.extend([track1, track2])
    db.session.add_all([user1, playlist1])

    db.session.commit()
