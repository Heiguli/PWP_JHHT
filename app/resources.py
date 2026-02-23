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
            return {"message", "Artist not found"}, 404
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
    
