#!/usr/bin/python

import psycopg2
import json

conn = psycopg2.connect(database="musicLibrary", user = "musicLib", password = "musicPass", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

cur = conn.cursor()

def tableCreation():
    # Testing recreation of tables
    # cur.execute("DROP TABLE album CASCADE;")
    # cur.execute("DROP TABLE song CASCADE;")
    # cur.execute("DROP TABLE contains;")

    # cur.execute("DROP TABLE name CASCADE;")
    # cur.execute("DROP TABLE producer;")
    # cur.execute("DROP TABLE writer;")
    # cur.execute("DROP TABLE artist;")
    # cur.execute("DROP TABLE featuredIn;")
    # cur.execute("DROP TABLE writtenBy;")
    # cur.execute("DROP TABLE producedBy;")
    # cur.execute("DROP TABLE performedBy;")

    # CREATING TABLE
    # Creating album table
    cur.execute('''CREATE TABLE album
            (albumUID TEXT PRIMARY KEY NOT NULL,
            albumTitle TEXT NOT NULL,
            duration REAL NOT NULL,
            releaseDate DATE);''')

    # Creating song table
    cur.execute('''CREATE TABLE song
            (songUID TEXT PRIMARY KEY NOT NULL,
            genre TEXT,
            songTitle TEXT NOT NULL);''')

    # Creating contains table
    cur.execute('''CREATE TABLE contains
            (songUID TEXT NOT NULL,
            albumUID TEXT NOT NULL,
            PRIMARY KEY(songUID),
            FOREIGN KEY(songUID) REFERENCES song ON DELETE CASCADE,
            FOREIGN KEY(albumUID) REFERENCES album ON DELETE CASCADE);''')

    # Creating name table
    cur.execute('''CREATE TABLE name
                (nameUID TEXT PRIMARY KEY NOT NULL,
                nameString TEXT NOT NULL,
                knownAs TEXT);''')

    # Creating producer table
    cur.execute('''CREATE TABLE producer
                (nameUID TEXT PRIMARY KEY NOT NULL,
                FOREIGN KEY(nameUID) REFERENCES name ON DELETE CASCADE);''')

    # Creating writer table
    cur.execute('''CREATE TABLE writer
                (nameUID TEXT PRIMARY KEY NOT NULL,
                FOREIGN KEY(nameUID) REFERENCES name ON DELETE CASCADE);''')

    # Creating artist table
    cur.execute('''CREATE TABLE artist
                (nameUID TEXT PRIMARY KEY NOT NULL,
                FOREIGN KEY(nameUID) REFERENCES name ON DELETE CASCADE);''')

    # Creating featuredIn table
    cur.execute('''CREATE TABLE featuredIn
                (songUID TEXT NOT NULL,
                nameUID TEXT NOT NULL,
                PRIMARY KEY(songUID, nameUID),
                FOREIGN KEY(songUID) REFERENCES song ON DELETE CASCADE,
                FOREIGN KEY(nameUID) REFERENCES name ON DELETE CASCADE);''')

    # Creating writtenBy table
    cur.execute('''CREATE TABLE writtenBy
                (albumUID TEXT NOT NULL,
                nameUID TEXT NOT NULL,
                PRIMARY KEY(albumUID, nameUID),
                FOREIGN KEY(albumUID) REFERENCES album ON DELETE CASCADE,
                FOREIGN KEY(nameUID) REFERENCES name ON DELETE CASCADE);''')

    # Creating producedBy table
    cur.execute('''CREATE TABLE producedBy
                (albumUID TEXT NOT NULL,
                nameUID TEXT NOT NULL,
                PRIMARY KEY(albumUID, nameUID),
                FOREIGN KEY(albumUID) REFERENCES album ON DELETE CASCADE,
                FOREIGN KEY(nameUID) REFERENCES name ON DELETE CASCADE);''')

    # Creating performedBy
    cur.execute('''CREATE TABLE performedBy
                (songUID TEXT NOT NULL,
                albumUID TEXT NOT NULL,
                nameUID TEXT NOT NULL,
                PRIMARY KEY(songUID, albumUID),
                FOREIGN KEY(songUID) REFERENCES song ON DELETE CASCADE,
                FOREIGN KEY(albumUID) REFERENCES album ON DELETE CASCADE,
                FOREIGN KEY(nameUID) REFERENCES name ON DELETE CASCADE);''')

    conn.commit()
    print("Tables created successfully")

# Bulk inserting data into database from JSON
def dataInsertion():
    with open('MusicLibrary/dataSet.json') as f:
        data = json.load(f)
    for x, t in enumerate(data['musicData']):
        # Create album 
        albumInsert = """INSERT INTO album (albumUID, albumTitle, duration, releaseDate) VALUES (%s, %s, %s, %s)"""
        albumData = (t['albumID'], t['albumTitle'], float(t['albumDuration']), t['albumReleaseDate'])
        cur.execute(albumInsert, albumData)

        # Create name for artist
        nameInsert = """INSERT INTO name (nameUID, nameString, knownAs) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING"""
        nameData = (t['artistID'], t['artistName'], t['artistName'])
        cur.execute(nameInsert, nameData)

        # Create artist
        artistInsert = """INSERT INTO artist (nameUID) VALUES (%s) ON CONFLICT DO NOTHING"""
        artistData = (t['artistID'])
        cur.execute(artistInsert, [artistData])

        # Create producers
        for y, p in enumerate(t['producedBy']):
            producerNameInsert = """INSERT INTO name (nameUID, nameString, knownAs) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING"""
            producerNameData = (p['id'], p['name'], p['name'])
            cur.execute(producerNameInsert, producerNameData)

            producerInsert = """INSERT INTO producer (nameUID) VALUES (%s) ON CONFLICT DO NOTHING"""
            producerData = (p['id'])
            cur.execute(producerInsert, [producerData])

            # Create producedBy
            producedByInsert = """INSERT INTO producedBy (albumUID, nameUID) VALUES (%s, %s) ON CONFLICT DO NOTHING"""
            producedByData = (t['albumID'], p['id'])
            cur.execute(producedByInsert, producedByData)

        # Create writters
        for y, w in enumerate(t['writtenBy']):
            writerNameInsert = """INSERT INTO name (nameUID, nameString, knownAs) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING"""
            writerNameData = (w['id'], w['name'], w['name'])
            cur.execute(writerNameInsert, writerNameData)

            writerInsert = """INSERT INTO writer (nameUID) VALUES (%s) ON CONFLICT DO NOTHING"""
            writerData = (w['id'])
            cur.execute(writerInsert, [writerData])

            # Create writtenBy
            writtenByInsert = """INSERT INTO writtenBy (albumUID, nameUID) VALUES (%s, %s) ON CONFLICT DO NOTHING"""
            writtenByData = (t['albumID'], w['id'])
            cur.execute(writtenByInsert, writtenByData)

        # Iterate through all songs in the album
        for y, s in enumerate(t['songs']):
            # Create all songs
            songInsert = """INSERT INTO song (songUID, genre, songTitle) VALUES (%s, %s, %s)"""
            songData = (s['id'], s['genre'], s['name'])
            cur.execute(songInsert, songData)

            # Create all contains 
            containsInsert = """INSERT INTO contains (songUID, albumUID) VALUES (%s, %s)"""
            containsData = (s['id'], t['albumID'])
            cur.execute(containsInsert, containsData)

            # Create all performedBy
            performedByInsert = """INSERT INTO performedBy (songUID, albumUID, nameUID) VALUES (%s, %s, %s)"""
            performedByData = (s['id'], t['albumID'], t['artistID'])
            cur.execute(performedByInsert, performedByData)

            for z, a in enumerate(s['featuredIn']):
                # Creating names of featuredIn
                featuredInNameInsert = """INSERT INTO name (nameUID, nameString, knownAs) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING"""
                featuredInNameData = (a['id'], a['name'], a['name'])
                cur.execute(featuredInNameInsert, featuredInNameData)

                # Creating artist of featuredIn
                featuredInArtistInsert = """INSERT INTO artist (nameUID) VALUES (%s) ON CONFLICT DO NOTHING"""
                featuredInArtistData = (a['id'])
                cur.execute(featuredInArtistInsert, [featuredInArtistData])
                # Creating all featuredIn
                featuredInInsert = """INSERT INTO featuredIn (songUID, nameUID) VALUES (%s, %s) ON CONFLICT DO NOTHING"""
                featuredInData = (s['id'],a['id'])
                cur.execute(featuredInInsert, featuredInData)
    conn.commit()

tableCreation()
dataInsertion()

# MISSING WRITER, PRODUCER

cur.close()
conn.close()