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

```TODO: Add description```

| Endpoint | Method | Description |
|---|---|---|
| `/artists` | GET | |
| `/artists` | POST | |
| `/artists` | DELETE | |
| `/artists/<id>` | GET | |
| `/artists/<id>` | PUT | |
| `/artists/<id>` | DELETE | |

---

### Album

```TODO: Add description```

| Endpoint | Method | Description |
|---|---|---|
| `/albums` | GET | |
| `/albums` | POST | |
| `/albums` | DELETE | |
| `/albums/<id>` | GET | |
| `/albums/<id>` | PUT | |
| `/albums/<id>` | DELETE | |

---

### Track

```TODO: Add description ```

| Endpoint | Method | Description |
|---|---|---|
| `/tracks` | GET | |
| `/tracks` | POST | |
| `/tracks` | DELETE | |
| `/tracks/<id>` | GET | |
| `/tracks/<id>` | PUT | |
| `/tracks/<id>` | DELETE | |
