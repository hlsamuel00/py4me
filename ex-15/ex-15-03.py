import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('ex-15-03.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, 
    rating INTEGER, 
    count INTEGER
);
''')

file_name = input('Enter file name: ')
if len(file_name) < 1: file_name = 'Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

data = ET.parse(file_name)
all_data = data.findall('dict/dict/dict')
print('Dict count', len(all_data))

for entry in all_data:
    if ( lookup(entry, 'Track ID') is None ): continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None or genre is None: continue

    print(f'Name: {name}, Artist: {artist}, Album: {album}, Genre: {genre}, Play Count: {count}, Rating: {rating}, length: {length}')

    # Create or find artist in table
    cur.execute(''' INSERT OR IGNORE INTO Artist(name) VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ',(artist,))
    # Get artist id from table
    artist_id = cur.fetchone()[0]

    # Create or find genre in table
    cur.execute(''' INSERT OR IGNORE INTO Genre(name) VALUES ( ? )''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ',(genre,))
    genre_id = cur.fetchone()[0]

    # Create or find album in table
    cur.execute('''INSERT OR IGNORE INTO Album(title, artist_id) VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    # Get album id from table
    album_id = cur.fetchone()[0]

    #Create track in table
    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES(?,?,?,?,?,?)''',(name, album_id, genre_id, length, rating, count) )

    conn.commit()

