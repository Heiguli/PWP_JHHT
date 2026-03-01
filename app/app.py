from flask_restful import Api
from database import app, db
from resources import ArtistCollection, ArtistItem, TrackCollection, \
    TrackItem, AlbumCollection, AlbumItem, UserCollection, UserItem

api = Api(app)

api.add_resource(ArtistCollection, "/artists")
api.add_resource(ArtistItem, "/artists/<int:id>")
api.add_resource(TrackCollection, "/tracks")
api.add_resource(TrackItem, "/tracks/<int:id>")
api.add_resource(AlbumCollection, "/albums")
api.add_resource(AlbumItem, "/albums/<int:id>")
api.add_resource(UserCollection, "/users")
api.add_resource(UserItem, "/users/<int:id>")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print("App is running!")
    app.run(debug=True)