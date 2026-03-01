from flask_restful import Api
from flask import jsonify
from database import app, db
from resources import ArtistCollection, ArtistItem, TrackCollection, \
    TrackItem, AlbumCollection, AlbumItem, UserCollection, UserItem, \
    PlaylistCollection, PlaylistItem

api = Api(app, prefix="/Beatify/api/v1")

api.add_resource(ArtistCollection, "/artists")
api.add_resource(ArtistItem, "/artists/<int:id>")
api.add_resource(TrackCollection, "/tracks")
api.add_resource(TrackItem, "/tracks/<int:id>")
api.add_resource(AlbumCollection, "/albums")
api.add_resource(AlbumItem, "/albums/<int:id>")
api.add_resource(UserCollection, "/users")
api.add_resource(UserItem, "/users/<int:id>")
api.add_resource(PlaylistCollection, "/playlists")
api.add_resource(PlaylistItem, "/playlists/<int:id>")


@app.route("/")
def Index():
    return jsonify({
        "api_name": "Beatify Music API",
        "version": "v1",
        "description": "A RESTful API for managing artists, albums, tracks, users and playlists.",
        "how_to_use": {
            "methods": "Use GET to read, POST to create, PUT to update, DELETE to remove.",
            "content_type": "All POST and PUT requests must use Content-Type: application/json",
            "example": "To create an artist: POST /Beatify/api/v1/artists with body {\"name\": \"Eminem\"}"
        },
        "endpoints": {
            "Artists": "http://localhost:5000/Beatify/api/v1/artists",
            "Albums": "http://localhost:5000/Beatify/api/v1/albums",
            "Tracks": "http://localhost:5000/Beatify/api/v1/tracks",
            "Users": "http://localhost:5000/Beatify/api/v1/users",
            "Playlists": "http://localhost:5000/Beatify/api/v1/playlists"
        },
        "single_item": "Add /<id> to any endpoint above, e.g. /Beatify/api/v1/artists/1"
    })

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print("App is running!")
    app.run(debug=True)