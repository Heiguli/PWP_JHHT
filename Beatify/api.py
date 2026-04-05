"""API registration in the Beatify module layout."""

from flask_restful import Api

from .models import app
from .resources import (
    AlbumCollection,
    AlbumItem,
    ArtistCollection,
    ArtistItem,
    PlaylistCollection,
    PlaylistItem,
    TrackCollection,
    TrackItem,
    UserCollection,
    UserItem,
)
from .utils import build_root_payload, json_response
from .models import db

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
def index():
    """Root endpoint with usage information."""
    return json_response(build_root_payload())


def start_api(debug: bool = True):
    """Create database tables and run the development server."""
    with app.app_context():
        db.create_all()
    print("App is running!")
    app.run(debug=debug)


if __name__ == "__main__":
    start_api(debug=True)
