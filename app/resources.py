"""
This module contains API resource classes with HTTP methods for managing application data.
"""
from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from database import db, Artist, Album, Track, Playlist, User

class ArtistCollection(Resource):
    '''
    Resource for viewing artist collection and adding new artists.
     
    Methods:
        GET
        POST
        DELETE
    '''

    def get(self):
        """
        Retrieve all artists in the database.

        Returns:
            list[dict[str, str]]: A list of artist data.
        """
        artist_list = []
        artists = Artist.query.all()
        for artist in artists:
            artist_data = {
                "name": artist.name
            }
            artist_list.append(artist_data)
        return artist_list

    def post(self):
        '''
        Add a new artist to the database.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.

        Raises:
            ValueError, TypeError: If fields have invalid data types.
            IntegrityError: If name is not unique.
        '''
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_json = request.json
        fields = ["name"]
        if not all(field in incoming_json for field in fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            name = incoming_json["name"]
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
        """
        Deletes all artists from the database.
        
        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.
        """
        num_deleted = Artist.query.delete()
        db.session.commit()
        return {"message": f"Deleted {num_deleted} artists"}, 200

class ArtistItem(Resource):
    '''
    Resource for managing individual artists.
     
    Methods:
        GET
        PUT
        DELETE
    '''

    def get(self, id):
        """
        Retrieve an artist from the database.

        Args:
            id (int): Id of the artist.

        Returns:
            dict[str, str]: Artist data.
        """
        artist = Artist.query.get(id)
        if not artist:
            return {"message": "Artist not found"}, 404
        artist_data = {
            "name": artist.name
        }
        return artist_data

    def put(self, id):
        '''
        Modify an existing artist in the database.

        Args:
            id (int): Id of the artist to be modified.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.

        Raises:
            ValueError, TypeError: If fields have invalid data types.
            IntegrityError: If name is not unique.
        '''
        artist = Artist.query.get(id)
        if not artist:
            return {"message": "Artist not found"}, 404
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_json = request.json
        fields = ["name"]
        if not all(field in incoming_json for field in fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            artist.name = incoming_json["name"]
        except (ValueError, TypeError):
            return {"message" : "Invalid data types for fields"}, 400
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error - possible duplicate entry"}, 400
        return {"message": f"Artist {artist.name} updated successfully!"}, 200

    def delete(self, id):
        """
        Delete an artist from the database.

        Args:
            id (int): Id of the artist to be deleted.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.
        """
        artist = Artist.query.get(id)
        if not artist:
            return {"message": "Artist not found"}, 404
        db.session.delete(artist)
        db.session.commit()
        return {"message": f"Artist {artist.name} deleted successfully"}, 200

class TrackCollection(Resource):
    '''
    Resource for viewing track collection and adding new tracks.
     
    Methods:
        GET
        POST
        DELETE
    '''

    def get(self):
        """
        Retrieve all tracks in the database.

        Returns:
            list[dict[str, str | int]]: A list of track data.
        """
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
        '''
        Add a new track to the database.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.

        Raises:
            ValueError, TypeError: If fields have invalid data types.
            IntegrityError: If name is not unique.
        '''
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_json = request.json
        fields = ["name", "length", "album_id"]
        if not all(field in incoming_json for field in fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            name = incoming_json["name"]
            length = int(incoming_json["length"])
            album_id = int(incoming_json["album_id"])
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
        """
        Deletes all artists from the database.
        
        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.
        """
        num_deleted = Track.query.delete()
        db.session.commit()
        return {"message": f"Deleted {num_deleted} tracks"}, 200

class TrackItem(Resource):
    '''
    Resource for managing individual tracks.
     
    Methods:
        GET
        PUT
        DELETE
    '''

    def get(self, id):
        """
        Retrieve a track from the database.

        Args:
            id (int): Id of the track.

        Returns:
            dict[str, str | int]: Track data.
        """
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
        '''
        Modify an existing track in the database.

        Args:
            id (int): Id of the track to be modified.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.

        Raises:
            ValueError, TypeError: If fields have invalid data types.
            IntegrityError: If name is not unique.
        '''
        track = Track.query.get(id)
        if not track:
            return {"message": "Track not found"}, 404
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_json = request.json
        fields = ["name", "length", "album_id"]
        if not all(field in incoming_json for field in fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            track.name = incoming_json["name"]
            track.length = int(incoming_json["length"])
            track.album_id = int(incoming_json["album_id"])
        except (ValueError, TypeError):
            return {"message": "Invalid data types for fields"}, 400
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error - possible duplicate entry"}, 400
        return {"message": f"Track {track.name} updated successfully!"}, 200

    def delete(self, id):
        """
        Delete a track from the database.

        Args:
            id (int): Id of the track to be deleted.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.
        """
        track = Track.query.get(id)
        if not track:
            return {"message": "Track not found"}, 404
        db.session.delete(track)
        db.session.commit()
        return {"message": f"Track {track.name} deleted successfully"}, 200

# Code from
# https://github.com/UniOulu-Ubicomp-Programming-Courses/pwp-sensorhub-example/blob/ex2-02-resource-classes/app.py
# was used as a framework for implementing get and post methods in AlbumCollection.
class AlbumCollection(Resource):
    '''
    Resource for viewing album collection and adding new albums.
     
    Methods:
        GET
        POST
    '''

    def get(self):
        """
        Retrieve all albums in the database.

        Returns:
            list[dict[str, str | int]]: A list of album data.
        """
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
        '''
        Add a new album to the database.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.

        Raises:
            KeyError: If the request is missing fields.
            ValueError: If the field "artist_id" is not an integer.
        '''
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        # Check that request includes fields "name" and "artist_id" with correct type
        try:
            name = request.json["name"]
            artist_id = int(request.json["artist_id"])
        except KeyError:
            return {"message": "Incomplete request - missing fields"}, 400
        except ValueError:
            return {"message": "artist_id must be an integer"}, 400
        # Check that artist_id matches an artist in the database
        if not Artist.query.filter_by(id=artist_id).first():
            return {"message": "artist_id does not match any artist"}, 400
        # Check that the album by this artist does not exist in database
        if Album.query.filter_by(name=name, artist_id=artist_id).first():
            return {"message": f"Album {name} by artist_id {artist_id} already exists"}, 400
        # Create new album
        new_album = Album(
            name=name,
            artist_id=artist_id
        )
        # Add the new album to the database
        db.session.add(new_album)
        db.session.commit()
        return {"message": f"Album {name} created successfully"}, 201

# Code from
# https://github.com/UniOulu-Ubicomp-Programming-Courses/pwp-sensorhub-example/blob/ex2-02-resource-classes/app.py
# was used as a framework for implementing get and put methods in AlbumItem.
class AlbumItem(Resource):
    '''
    Resource for managing individual albums.
     
    Methods:
        GET
        PUT
        DELETE
    '''

    def get(self, id):
        """
        Retrieve an album from the database.

        Args:
            id (int): Id of the album.

        Returns:
            dict[str, str | int]: Album data.
        """
        album = Album.query.get(id)
        if not album:
            return {"message": "Album not found"}, 404
        album_data = {
            "name": album.name,
            "artist_id": album.artist_id
        }
        return album_data

    def put(self, id):
        '''
        Modify an existing album in the database.

        Args:
            id (int): Id of the album to be modified.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.

        Raises:
            KeyError: If the request is missing fields.
            ValueError: If the field "artist_id" is not an integer.
        '''
        album = Album.query.get(id)
        if not album:
            return {"message": "Album not found"}, 404
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        try:
            name = request.json["name"]
            artist_id = int(request.json["artist_id"])
        except KeyError:
            return {"message": "Incomplete request - missing fields"}, 400
        except ValueError:
            return {"message": "artist_id must be an integer"}, 400
        # Check that artist_id matches an artist in the database
        if not Artist.query.filter_by(id=artist_id).first():
            return {"message": "artist_id does not match any artist"}, 400
        # Check for changes
        if (name == album.name) and (artist_id == album.artist_id):
        #if Album.query.filter_by(name=name, artist_id=artist_id).first(): #alternative
            return {"message": "No changes detected"}, 400
        # Update album info
        album.name = name
        album.artist_id = artist_id
        db.session.commit()
        return {"message": f"Album {name} updated successfully"}, 200

    def delete(self, id):
        """
        Delete an album from the database.

        Args:
            id (int): Id of the album to be deleted.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.
        """
        album = Album.query.get(id)
        if not album:
            return {"message": "Album not found"}, 400
        db.session.delete(album)
        db.session.commit()
        return {"message": f"Album {album.name} deleted successfully"}, 200

class UserCollection(Resource):
    '''
    Resource for viewing user collection and adding new users.
     
    Methods:
        GET
        POST
        DELETE
    '''

    def get(self):
        """
        Retrieve all users in the database.

        Returns:
            list[dict[str, int | str]]: A list of user data.
        """
        user_list = []
        all_users = User.query.all()
        for user in all_users:
            user_data = {
                "id": user.id,
                "name": user.name
            }
            user_list.append(user_data)
        return user_list

    def post(self):
        '''
        Add a new user to the database.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.

        Raises:
            ValueError, TypeError: If fields have invalid data types.
            IntegrityError: If name is not unique.
        '''
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_data = request.json
        required_fields = ["name"]
        if not all(field in incoming_data for field in required_fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            user_name = incoming_data["name"]
        except (ValueError, TypeError):
            return {"message": "Invalid data types for fields"}, 400
        new_user = User(name=user_name)
        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error - possible duplicate entry"}, 400
        return {"message": f"User {user_name} created successfully!"}, 201

    def delete(self): #Dont use if not EXPLICITLY needed, because this deletes ALL users
        """
        Deletes all users from the database.
        
        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.
        """
        num_deleted = User.query.delete()
        db.session.commit()
        return {"message": f"Deleted {num_deleted} users"}, 200


class UserItem(Resource):
    '''
    Resource for managing individual users.
     
    Methods:
        GET
        PUT
        DELETE
    '''

    def get(self, id):
        """
        Retrieve a user from the database.

        Args:
            id (int): Id of the user.

        Returns:
            dict[str, int | str]: User data.
        """
        user = User.query.get(id)
        if not user:
            return {"message": "User not found"}, 404
        # also show the playlists this user has
        playlist_list = []
        for playlist in user.playlists:
            playlist_list.append({
                "id": playlist.id,
                "name": playlist.name
            })
        user_data = {
            "id": user.id,
            "name": user.name,
            "playlists": playlist_list
        }
        return user_data

    def put(self, id):
        '''
        Modify an existing user in the database.

        Args:
            id (int): Id of the user to be modified.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.

        Raises:
            ValueError, TypeError: If fields have invalid data types.
            IntegrityError: If name is not unique.
        '''
        user = User.query.get(id)
        if not user:
            return {"message": "User not found"}, 404
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_data = request.json
        required_fields = ["name"]
        if not all(field in incoming_data for field in required_fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            user.name = incoming_data["name"]
        except (ValueError, TypeError):
            return {"message": "Invalid data types for fields"}, 400
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error - possible duplicate entry"}, 400
        return {"message": f"User {user.name} updated successfully!"}, 200

    def delete(self, id):
        """
        Delete u user from the database.

        Args:
            id (int): Id of the user to be deleted.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.
        """
        user = User.query.get(id)
        if not user:
            return {"message": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.name} deleted successfully"}, 200

# got the idea from other resource classes and adapted it to fit the playlist model
class PlaylistCollection(Resource):
    '''
    Resource for viewing playlist collection and adding new playlists.
     
    Methods:
        GET
        POST
        DELETE
    '''

    def get(self):
        """
        Retrieve all playlists in the database.

        Returns:
            list[dict[str, int | str]]: A list of playlist data.
        """
        playlist_list = []
        all_playlists = Playlist.query.all()
        for playlist in all_playlists:
            playlist_data = {
                "id": playlist.id,
                "name": playlist.name,
                "description": playlist.description
            }
            playlist_list.append(playlist_data)
        return playlist_list

    def post(self):
        '''
        Add a new playlist to the database.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.

        Raises:
            ValueError, TypeError: If fields have invalid data types.
            IntegrityError: Database integrity error.
        '''
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_data = request.json
        required_fields = ["name"]
        if not all(field in incoming_data for field in required_fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            playlist_name = incoming_data["name"]
            playlist_desc = incoming_data.get("description", "") # description is optional
        except (ValueError, TypeError):
            return {"message": "Invalid data types for fields"}, 400
        new_playlist = Playlist(name=playlist_name, description=playlist_desc)
        # if user_id is given, link the playlist to that user
        if "user_id" in incoming_data:
            try:
                user_id = int(incoming_data["user_id"])
            except (ValueError, TypeError):
                return {"message": "user_id must be an integer"}, 400
            found_user = User.query.get(user_id)
            if not found_user:
                return {"message": "User not found"}, 404
            new_playlist.users.append(found_user)
        db.session.add(new_playlist)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error"}, 400
        return {"message": f"Playlist {playlist_name} created successfully!"}, 201

    def delete(self): #Dont use if not EXPLICITLY needed, because this deletes ALL playlists
        """
        Deletes all playlists from the database.
        
        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.
        """
        num_deleted = Playlist.query.delete()
        db.session.commit()
        return {"message": f"Deleted {num_deleted} playlists"}, 200


class PlaylistItem(Resource):
    '''
    Resource for managing individual playlists.
     
    Methods:
        GET
        PUT
        DELETE
    '''

    def get(self, id):
        """
        Retrieve a playlist from the database.

        Args:
            id (int): Id of the playlist.

        Returns:
            dict[str, int | str]: Playlist data.
        """
        playlist = Playlist.query.get(id)
        if not playlist:
            return {"message": "Playlist not found"}, 404
        # show which tracks are on this playlist
        track_list = []
        for track in playlist.tracks:
            track_list.append({
                "id": track.id,
                "name": track.name,
                "length": track.length
            })
        # show which users own this playlist
        user_list = []
        for user in playlist.users:
            user_list.append({
                "id": user.id,
                "name": user.name
            })
        playlist_data = {
            "id": playlist.id,
            "name": playlist.name,
            "description": playlist.description,
            "tracks": track_list,
            "users": user_list
        }
        return playlist_data

    def put(self, id):
        '''
        Modify an existing playlist in the database.

        Args:
            id (int): Id of the playlist to be modified.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.

        Raises:
            ValueError, TypeError: If fields have invalid data types.
            IntegrityError: Database integrity error.
        '''
        playlist = Playlist.query.get(id)
        if not playlist:
            return {"message": "Playlist not found"}, 404
        if not request.is_json:
            return {"message": "Request content type must be JSON"}, 415
        incoming_data = request.json
        required_fields = ["name"]
        if not all(field in incoming_data for field in required_fields):
            return {"message": "Incomplete request - missing fields"}, 400
        try:
            playlist.name = incoming_data["name"]
            playlist.description = incoming_data.get("description", playlist.description)
        except (ValueError, TypeError):
            return {"message": "Invalid data types for fields"}, 400
        # if track_id is given, add that track to the playlist
        if "track_id" in incoming_data:
            try:
                track_id = int(incoming_data["track_id"])
            except (ValueError, TypeError):
                return {"message": "track_id must be an integer"}, 400
            found_track = Track.query.get(track_id)
            if not found_track:
                return {"message": "Track not found"}, 404
            if found_track not in playlist.tracks:
                playlist.tracks.append(found_track)
        # if user_id is given, link that user to the playlist
        if "user_id" in incoming_data:
            try:
                user_id = int(incoming_data["user_id"])
            except (ValueError, TypeError):
                return {"message": "user_id must be an integer"}, 400
            found_user = User.query.get(user_id)
            if not found_user:
                return {"message": "User not found"}, 404
            if found_user not in playlist.users:
                playlist.users.append(found_user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Database integrity error"}, 400
        return {"message": f"Playlist {playlist.name} updated successfully!"}, 200

    def delete(self, id):
        """
        Delete a playlist from the database.

        Args:
            id (int): Id of the playlist to be deleted.

        Returns:
            tuple[dict[str, str], int]: Result message and HTTP status code.
        """
        playlist = Playlist.query.get(id)
        if not playlist:
            return {"message": "Playlist not found"}, 404
        db.session.delete(playlist)
        db.session.commit()
        return {"message": f"Playlist {playlist.name} deleted successfully"}, 200
