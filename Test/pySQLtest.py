#!/usr/bin/python

import psycopg2
import json

conn = psycopg2.connect(database="YOURDB", user = "YOURUSERNAME", password = "YOURPW", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

cur = conn.cursor()

def tableCreation():
   # Testing recreation of tables
   cur.execute("DROP TABLE album CASCADE;")
   cur.execute("DROP TABLE song CASCADE;")
   cur.execute("DROP TABLE contains;")

   cur.execute("DROP TABLE name CASCADE;")
   cur.execute("DROP TABLE producer;")
   cur.execute("DROP TABLE writer;")
   cur.execute("DROP TABLE artist;")
   cur.execute("DROP TABLE featuredIn;")
   cur.execute("DROP TABLE writtenBy;")
   cur.execute("DROP TABLE producedBy;")
   cur.execute("DROP TABLE performedBy;")

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

   # Creating contains table MAYBE NEED TO ADD ON DELETE FOR FOREIGN KEYS??
   cur.execute('''CREATE TABLE contains
         (songUID TEXT NOT NULL,
         albumUID TEXT NOT NULL,
         PRIMARY KEY(songUID),
         FOREIGN KEY(songUID) REFERENCES song ON DELETE NO ACTION,
         FOREIGN KEY(albumUID) REFERENCES album ON DELETE NO ACTION);''')

   # Creating name table
   cur.execute('''CREATE TABLE name
            (nameUID TEXT PRIMARY KEY NOT NULL,
            nameString TEXT NOT NULL,
            knownAs TEXT);''')

   # Creating producer table
   cur.execute('''CREATE TABLE producer
            (nameUID TEXT PRIMARY KEY NOT NULL,
            FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

   # Creating writer table
   cur.execute('''CREATE TABLE writer
            (nameUID TEXT PRIMARY KEY NOT NULL,
            FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

   # Creating artist table
   cur.execute('''CREATE TABLE artist
            (nameUID TEXT PRIMARY KEY NOT NULL,
            FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

   # Creating featuredIn table
   cur.execute('''CREATE TABLE featuredIn
            (songUID TEXT NOT NULL,
            nameUID TEXT NOT NULL,
            PRIMARY KEY(songUID, nameUID),
            FOREIGN KEY(songUID) REFERENCES song ON DELETE NO ACTION,
            FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

   # Creating writtenBy table
   cur.execute('''CREATE TABLE writtenBy
            (songUID TEXT NOT NULL,
            nameUID TEXT NOT NULL,
            PRIMARY KEY(songUID, nameUID),
            FOREIGN KEY(songUID) REFERENCES song ON DELETE NO ACTION,
            FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

   # Creating producedBy table
   cur.execute('''CREATE TABLE producedBy
            (songUID TEXT NOT NULL,
            nameUID TEXT NOT NULL,
            PRIMARY KEY(songUID, nameUID),
            FOREIGN KEY(songUID) REFERENCES song ON DELETE NO ACTION,
            FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

   # Creating performedBy
   cur.execute('''CREATE TABLE performedBy
            (songUID TEXT NOT NULL,
            albumUID TEXT NOT NULL,
            nameUID TEXT NOT NULL,
            PRIMARY KEY(songUID, albumUID),
            FOREIGN KEY(songUID) REFERENCES song ON DELETE NO ACTION,
            FOREIGN KEY(albumUID) REFERENCES album ON DELETE NO ACTION,
            FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

   print("Table created successfully")
   conn.commit()

def testInserts():
   # Creating data for the table
   cur.execute("INSERT INTO ALBUM (albumUID, albumTitle, duration, releaseDate)\
      VALUES (1, 'albumIsBest', 800, NULL)");

   cur.execute("INSERT INTO SONG (songUID, genre, songTitle)\
      VALUES (1, 'rock', 'helloSongTitle')");

   cur.execute("INSERT INTO CONTAINS (songUID, albumUID)\
      VALUES(1,1)");

   conn.commit()

   cur.execute("SELECT *  from ALBUM")
   rows = cur.fetchall()
   for row in rows:
      print (row)

   cur.execute('''SELECT albumTitle, songTitle
               FROM album, contains, song
               WHERE contains.albumUID = album.albumUID;''')
   rows = cur.fetchall()
   for row in rows:
      print(row)


   print ("Operation done successfully")

def dataInsertion():
   with open('dataSet.json') as f:
      data = json.load(f)
   for x, t in enumerate(data['musicData']):
      # Create album 
      albumInsert = """INSERT INTO album (albumUID, albumTitle, duration, releaseDate) VALUES (%s, %s, %s, %s)"""
      albumData = (t['albumID'], t['albumTitle'], float(t['albumDuration']), t['albumReleaseDate'])
      cur.execute(albumInsert, albumData)

      # Create name
      nameInsert = """INSERT INTO name (nameUID, nameString, knownAs) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING"""
      nameData = (t['artistID'], t['artistName'], t['artistName'])
      cur.execute(nameInsert, nameData)

      # Create artist
      artistInsert = """INSERT INTO artist (nameUID) VALUES (%s) ON CONFLICT DO NOTHING"""
      artistData = (t['artistID'])
      cur.execute(artistInsert, [artistData])

      # Iterate through all songs in the album
      for y, s in enumerate(t['songs']):
         # Create all songs
         songInsert = """INSERT INTO song (songUID, genre, songTitle) VALUES (%s, NULL, %s)"""
         songData = (s['id'], s['name'])
         cur.execute(songInsert, songData)
         # MUST MANUALLY ADD GENRE

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

cur.execute("SELECT *  from ALBUM")
rows = cur.fetchall()
for row in rows:
   print (row)

cur.close()
conn.close()
