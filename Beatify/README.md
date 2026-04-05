# Beatify Music API

This module contains the core application code for the Beatify Music API, a RESTful API for managing artists, albums, tracks, users and playlists.

## Files

- **app.py** - Main entry point. Sets up Flask RESTful routes and runs the server.
- **database.py** - Database models and SQLAlchemy configuration.
- **resources.py** - Resource classes that handle HTTP requests for each endpoint.

## Base URL

```
/Beatify/api/v1
```

## Resources

### User

Represents a registered user who can own playlists.

**Fields:** `id`, `name`

| Endpoint | Method | Description |
|---|---|---|
| `/users` | GET | Get all users |
| `/users` | POST | Create a new user |
| `/users` | DELETE | Delete all users |
| `/users/<id>` | GET | Get a single user (includes their playlists) |
| `/users/<id>` | PUT | Update a user's name |
| `/users/<id>` | DELETE | Delete a user |
---

### Playlist

Represents a playlist that can contain tracks and be shared between users.

**Fields:** `id`, `name`, `description` (optional)

| Endpoint | Method | Description |
|---|---|---|
| `/playlists` | GET | Get all playlists |
| `/playlists` | POST | Create a new playlist (optionally link to a user via `user_id`) |
| `/playlists` | DELETE | Delete all playlists |
| `/playlists/<id>` | GET | Get a single playlist |
| `/playlists/<id>` | PUT | Update a playlist |
| `/playlists/<id>` | DELETE | Delete a playlist |

---

### Artist

```Represents a Artist resource object which tracks individual artists and which tracks and albums belong to which artists.```

| Endpoint | Method | Description |
|---|---|---|
| `/artists` | GET |Get ALL artists |
| `/artists` | POST |Create a singular artist |
| `/artists` | DELETE |Delete ALL artists (should not be used, risky) |
| `/artists/<id>` | GET |Get singular artist |
| `/artists/<id>` | PUT |Update a artist |
| `/artists/<id>` | DELETE |Delete singular artist |

---

### Album

```Represents a Album resource object which tracks individual albums and which tracks belong to which albums. Also to whom (artist) the album belongs to.```

| Endpoint | Method | Description |
|---|---|---|
| `/albums` | GET |Get ALL albums |
| `/albums` | POST |Create singular album |
| `/albums` | DELETE |Delete ALL albums (should not be used, risky) |
| `/albums/<id>` | GET |Get singular album |
| `/albums/<id>` | PUT |Update singular album |
| `/albums/<id>` | DELETE |Delete singular album |

---

### Track

```Represents a Track resource object which tracks indidual tracks and to whom (artist) they belong to and to which album they belong to.  ```

| Endpoint | Method | Description |
|---|---|---|
| `/tracks` | GET |Get ALL tracks |
| `/tracks` | POST |Create singular track |
| `/tracks` | DELETE |Delete ALL tracks (should not be used, risky) |
| `/tracks/<id>` | GET |Get singular track |
| `/tracks/<id>` | PUT |Update singular track |
| `/tracks/<id>` | DELETE |Delete singular track |
