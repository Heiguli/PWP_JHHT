from flask import Flask  #import Flask, which allows us to get the core functionalities behind building a web app
from flask_sqlalchemy import SQLAlchemy #import SQLAlchemy because it allows us to easily do databases via python classes
from sqlalchemy.exc import IntegrityError #import exception class for checking database contraints
from sqlalchemy.engine import Engine #Needed to check for example, connections,
from sqlalchemy import event #and then we can listen for a event, like connection event via engine, and then we run a function after connection event

app = Flask(__name__) #Creates Flask application object, and tells flask that the application is located in app.py
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db" #Tells flask to which database to connect to, and store database in file called "test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #Turns of object modification tracking 
db = SQLAlchemy(app) #Creates a SQLAlchemy database object

#Join table for playlists and tracks. With this we can get many-to-many connections between playlists and tracks, 
#so same song on multiple playlists, and playlists may have multiple songs 
playlists_table = db.Table("playlists",
    db.Column("playlist_id", db.Integer, db.ForeignKey("playlist.id", ondelete = "CASCADE"), primary_key=True),
    db.Column("track_id", db.Integer, db.ForeignKey("track.id", ondelete = "CASCADE"), primary_key=True)
)

#Join table for playlists and users. With this we can get many-to-many connections between playlists and users, 
#so same playlist can be connected to multiple users, and users can have multiple playlists. Kind of like "share playlist" in spotify 
playlists_users_table = db.Table("playlists_users",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id", ondelete = "CASCADE"), primary_key=True),
    db.Column("playlist_id", db.Integer, db.ForeignKey("playlist.id", ondelete = "CASCADE"), primary_key=True)                        
)

@event.listens_for(Engine, "connect") #Whenever SQLAlchemy creates a new database connection using an Engine, run the function below
def set_sqlite_pragma(dbapi_connection, connection_record): #SQLite has foreign keys off by default, so we need this function to turn them on, after connection
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class Artist(db.Model):    #Database class for Artist object. Makes Artist tables
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    albums = db.relationship("Album", back_populates="artist", cascade="all, delete", uselist=True) #Relationship between artist and albums

    def __repr__(self): #Just more clear print output when python prints artists, not needed
        return f"[Artist {self.name}]"
    
class Album(db.Model):  #Database class for Album object. Makes Album tables
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id", ondelete="CASCADE"), nullable=False)

    artist = db.relationship("Artist", back_populates="albums", uselist=False) #Relationship between albums and artist
    tracks = db.relationship("Track", back_populates="album", cascade="all, delete") #Relationship between tracks and album

    def __repr__(self):
        return f"[Album {self.name}]"

class Track(db.Model):  #Database class for Track object. Makes Track tables
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    length = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("album.id"), nullable=False)
    
    album = db.relationship("Album", back_populates="tracks") #Relationship between album and tracks
    playlists = db.relationship("Playlist", secondary=playlists_table, back_populates="tracks") #Relationship between tracks and playlists

    def __repr__(self):
        return f"[Track {self.name}]"
    
class User(db.Model):   #Database class for User object. Makes User tables
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    playlists = db.relationship("Playlist", secondary=playlists_users_table, back_populates="users", cascade="all, delete") #Relationship between users and playlists

    def __repr__(self):
        return f"[User {self.name}]"
    
class Playlist(db.Model):   #Database class for Playlist object. Makes Playlist tables
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    #user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False) Not needed now since many-to-many via join table, if only one user per playlist, then use this

    users = db.relationship("User", secondary=playlists_users_table, back_populates="playlists") #Relationship between users and playlists
    tracks = db.relationship("Track", secondary=playlists_table, back_populates="playlists") #Relationship between tracks and playlists

    def __repr__(self):
        return f"[Playlist {self.name}]"
    
if __name__ == "__main__": #If the file is directly run, then do the following commands
    with app.app_context(): #Use this apps database config
        db.create_all() #Create database
    print("Database created")
    #app.run(debug=True)
    