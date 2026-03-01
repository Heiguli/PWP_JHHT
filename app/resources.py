from database import db, Artist, Album, Track, Playlist, User
from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError


class ArtistCollection(Resource):
        
    def get(self):
        artist_list = []
        artists = Artist.query.all()
        for artist in artists:
            artist_data = {
                "name": artist.name
            }
            artist_list.append(artist_data)
        return artist_list

    def post(self):
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_JSON = request.json
        fields = ["name"]
        if not all(field in incoming_JSON for field in fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            name = incoming_JSON["name"]
        except (ValueError, TypeError):
            return {"message":"Invalid data types for fields"}, 400
        new_artist = Artist(name=name)
        db.session.add(new_artist)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error - possible duplicate entry"}, 400
        return {"message": f"Artist {name} created successfully!"}, 201

    def delete(self): #Dont use if not EXPLICITLY needed, because this deletes ALL artists
        num_deleted = Artist.query.delete()
        db.session.commit()
        return {"message": f"Deleted {num_deleted} artists"}, 200 
    
class ArtistItem(Resource):

    def get(self, id):
        artist = Artist.query.get(id)
        if not artist:
            return {"message": "Artist not found"}, 404
        artist_data = {
            "name": artist.name
        }
        return artist_data
    
    def put(self, id):
        artist = Artist.query.get(id)
        if not artist:
            return {"message": "Artist not found"}, 404
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_JSON = request.json
        fields = ["name"]
        if not all(field in incoming_JSON for field in fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            artist.name = incoming_JSON["name"]
        except (ValueError, TypeError):
            return {"message" : "Invalid data types for fields"}, 400
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error - possible duplicate entry"}, 400
        return {"message": f"Artist {artist.name} updated successfully!"}, 200 

    def delete(self, id):
        artist = Artist.query.get(id)
        if not artist:
            return {"message": "Artist not found"}, 404
        db.session.delete(artist)
        db.session.commit()
        return {"message": f"Artist {artist.name} deleted successfully"}, 200
    
class TrackCollection(Resource):

    def get(self):
        track_list = []
        tracks = Track.query.all()
        for track in tracks:
            track_data = {
                "name": track.name,
                "length": track.length,
                "album_id": track.album_id
            }
            track_list.append(track_data)
        return track_list
    
    def post(self):
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_JSON = request.json
        fields = ["name", "length", "album_id"]
        if not all(field in incoming_JSON for field in fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            name = incoming_JSON["name"]
            length = int(incoming_JSON["length"])
            album_id = int(incoming_JSON["album_id"])
        except (ValueError, TypeError):
            return {"message": "Invalid data types for fields"}, 400
        album = Album.query.get(album_id)
        if not album:
            return {"message": "Album not found"}, 404
        new_track = Track(name=name, length=length, album_id=album_id)
        db.session.add(new_track)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error - possible duplicate entry"}, 400
        return {"message": f"Track {name} created successfully!"}, 201
    
    def delete(self): #Dont use if not EXPLICITLY needed, because this deletes ALL tracks
        num_deleted = Track.query.delete()
        db.session.commit()
        return {"message": f"Deleted {num_deleted} tracks"}, 200 
    
class TrackItem(Resource):

    def get(self, id):
        track = Track.query.get(id)
        if not track:
            return {"message": "Track not found"}, 404
        track_data = {
            "name": track.name,
            "length": track.length,
            "album_id": track.album_id
        }
        return track_data
    
    def put(self, id):
        track = Track.query.get(id)
        if not track:
            return {"message": "Track not found"}, 404
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_JSON = request.json
        fields = ["name", "length", "album_id"]
        if not all(field in incoming_JSON for field in fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            track.name = incoming_JSON["name"]
            track.length = int(incoming_JSON["length"])
            track.album_id = int(incoming_JSON["album_id"])
        except (ValueError, TypeError):
            return {"message": "Invalid data types for fields"}, 400
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error - possible duplicate entry"}, 400
        return {"message": f"Track {track.name} updated successfully!"}, 200
    
    def delete(self, id):
        track = Track.query.get(id)
        if not track:
            return {"message": "Track not found"}, 404
        db.session.delete(track)
        db.session.commit()
        return {"message": f"Track {track.name} deleted successfully"}, 200
    
class AlbumCollection(Resource):

    def get(self):
        response_data = []
        albums = Album.query.all()
        for album in albums:
            data = {
                "name": album.name,
                "artist_id": album.artist_id
            }
            response_data.append(data)
        return response_data
    
    def post(self):
        if not request.is_json:
            return "Request content type must be JSON", 415
        # Check that request includes fields "name" and "artist_id" with correct type
        try:
            name = request.json["name"]
            artist_id = int(request.json["artist_id"])
        except KeyError:
            return "Incomplete request - missing fields", 400
        except ValueError:
            return "artist_id must be an integer", 400
        # Check that artist_id matches an artist in the database
        if not Artist.query.filter_by(id=artist_id).first():
            return "artist_id does not match any artist", 400
        # Check that the album by this artist does not exist in database
        if Album.query.filter_by(name=name, artist_id=artist_id).first():
            return f"Album {name} by artist_id {artist_id} already exists", 400
        # Create new album
        new_album = Album(
            name=name,
            artist_id=artist_id
        )
        # Add the new album to the database
        try:
            db.session.add(new_album)
            db.session.commit()
        except IntegrityError:
            # This should not get called because neither album.name nor
            # album.artist_id has to be unique
            return "Failed to add album to database", 409
        return f"Album {name} created successfully", 201

class AlbumItem(Resource):

    def get(self, id):
        album = Album.query.get(id)
        if not album:
            return "Album not found", 404
        album_data = {
            "name": album.name,
            "artist_id": album.artist_id
        }
        return album_data

    def put(self, id):
        album = Album.query.get(id)
        if not album:
            return "Album not found", 404
        if not request.is_json:
            return "Request content type must be JSON", 415
        try:
            name = request.json["name"]
            artist_id = int(request.json["artist_id"])
        except KeyError:
            return "Incomplete request - missing fields", 400
        except ValueError:
            return "artist_id must be an integer", 400
        # Check that artist_id matches an artist in the database
        if not Artist.query.filter_by(id=artist_id).first():
            return "artist_id does not match any artist", 400
        # Check for changes
        if (name == album.name) and (artist_id == album.artist_id):
        #if Album.query.filter_by(name=name, artist_id=artist_id).first(): #alternative
            return f"No changes detected", 400   
        # Update album info
        album.name = name
        album.artist_id = artist_id
        db.session.commit()
        return f"Album {name} updated successfully", 200

    def delete(self, id):
        album = Album.query.get(id)
        if not album:
            return "Album not found", 400
        db.session.delete(album)
        db.session.commit()
        return f"Album {album.name} deleted successfully", 200

class UserCollection(Resource):
    def get(self):
        userList = []
        allUsers = User.query.all()
        for user in allUsers:
            userData = {
                "id": user.id,
                "name": user.name
            }
            userList.append(userData)
        return userList

    def post(self):
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incomingData = request.json
        requiredFields = ["name"]
        if not all(field in incomingData for field in requiredFields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            userName = incomingData["name"]
        except (ValueError, TypeError):
            return {"message": "Invalid data types for fields"}, 400
        newUser = User(name=userName)
        db.session.add(newUser)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error - possible duplicate entry"}, 400
        return {"message": f"User {userName} created successfully!"}, 201

    def delete(self): #Dont use if not EXPLICITLY needed, because this deletes ALL users
        numDeleted = User.query.delete()
        db.session.commit()
        return {"message": f"Deleted {numDeleted} users"}, 200


class UserItem(Resource):

    def get(self, id):
        user = User.query.get(id)
        if not user:
            return {"message": "User not found"}, 404
        # also show the playlists this user has
        playlistList = []
        for playlist in user.playlists:
            playlistList.append({
                "id": playlist.id,
                "name": playlist.name
            })
        userData = {
            "id": user.id,
            "name": user.name,
            "playlists": playlistList
        }
        return userData

    def put(self, id):
        user = User.query.get(id)
        if not user:
            return {"message": "User not found"}, 404
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incomingData = request.json
        requiredFields = ["name"]
        if not all(field in incomingData for field in requiredFields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            user.name = incomingData["name"]
        except (ValueError, TypeError):
            return {"message": "Invalid data types for fields"}, 400
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error - possible duplicate entry"}, 400
        return {"message": f"User {user.name} updated successfully!"}, 200

    def delete(self, id):
        user = User.query.get(id)
        if not user:
            return {"message": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.name} deleted successfully"}, 200