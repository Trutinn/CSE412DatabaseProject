#!/usr/bin/python

import psycopg2
import json

conn = psycopg2.connect(database="musiclibrary", user = "trutin", password = "Baseball324!", host = "127.0.0.1", port = "5432")

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
      print(t['albumID'])
      print(t['albumTitle'])
      print(t['albumDuration'])
      print(t['albumReleaseDate'])

      # Create name
      print(t['artistID'])
      print(t['artistName'])  # nameString
      print(t['artistName'])  # knownAs

      # Create artist
      print(t['artistID'])

      # Iterate through all songs in the album
      for y, s in enumerate(t['songs']):
         # Create all songs
         print(s['id'])
         print(s['name'])
         # MUST MANUALLY ADD GENRE

         # Create all contains 
         print(s['id'])
         print(t['albumID'])

         # Create all performedBy
         print(s['id'])
         print(t['albumID'])
         print(t['artistID'])

         for z, a in enumerate(s['featuredIn']):
            # Creating all featuredIn
            print(s['id'])
            print(a['id'])

tableCreation()
dataInsertion()

conn.commit()
cur.close()
conn.close()
