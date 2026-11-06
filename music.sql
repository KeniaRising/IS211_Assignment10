CREATE TABLE artists (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE albums (
    id INTEGER PRIMARY KEY,
    name TEXT,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artists(id)
);

CREATE TABLE songs (
    id INTEGER PRIMARY KEY,
    name TEXT,
    album_id INTEGER,
    track_number INTEGER,
    duration INTEGER,
    FOREIGN KEY (album_id) REFERENCES albums(id)
);
