#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="testdb", user = "USERNAME", password = "PASSWORD", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

cur = conn.cursor()

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


# CREATING TABLES
# Creating album table
cur.execute('''CREATE TABLE album
        (albumUID INT PRIMARY KEY NOT NULL,
        albumTitle TEXT NOT NULL,
        duration INT NOT NULL,
        releaseDate DATE);''')

# Creating song table
cur.execute('''CREATE TABLE song
        (songUID INT PRIMARY KEY NOT NULL,
        genre TEXT,
        songTitle TEXT NOT NULL);''')

# Creating contains table MAYBE NEED TO ADD ON DELETE FOR FOREIGN KEYS??
cur.execute('''CREATE TABLE contains
        (songUID INT NOT NULL,
        albumUID INT NOT NULL,
        PRIMARY KEY(songUID, albumUID),
        FOREIGN KEY(songUID) REFERENCES song ON DELETE NO ACTION,
        FOREIGN KEY(albumUID) REFERENCES album ON DELETE NO ACTION);''')

# Creating name table
cur.execute('''CREATE TABLE name
         (nameUID INT PRIMARY KEY NOT NULL,
         nameString TEXT NOT NULL,
         knownAs TEXT);''')

# Creating producer table
cur.execute('''CREATE TABLE producer
         (nameUID INT PRIMARY KEY NOT NULL,
         FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

# Creating writer table
cur.execute('''CREATE TABLE writer
         (nameUID INT PRIMARY KEY NOT NULL,
         FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

# Creating artist table
cur.execute('''CREATE TABLE artist
         (nameUID INT PRIMARY KEY NOT NULL,
         FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

# Creating featuredIn table
cur.execute('''CREATE TABLE featuredIn
         (songUID INT NOT NULL,
         nameUID INT NOT NULL,
         PRIMARY KEY(songUID, nameUID),
         FOREIGN KEY(songUID) REFERENCES song ON DELETE NO ACTION,
         FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

# Creating writtenBy table
cur.execute('''CREATE TABLE writtenBy
         (songUID INT NOT NULL,
         nameUID INT NOT NULL,
         PRIMARY KEY(songUID, nameUID),
         FOREIGN KEY(songUID) REFERENCES song ON DELETE NO ACTION,
         FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

# Creating producedBy table
cur.execute('''CREATE TABLE producedBy
         (songUID INT NOT NULL,
         nameUID INT NOT NULL,
         PRIMARY KEY(songUID, nameUID),
         FOREIGN KEY(songUID) REFERENCES song ON DELETE NO ACTION,
         FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

# Creating performedBy
cur.execute('''CREATE TABLE performedBy
         (songUID INT NOT NULL,
         albumUID INT NOT NULL,
         nameUID INT NOT NULL,
         PRIMARY KEY(songUID, albumUID),
         FOREIGN KEY(songUID) REFERENCES song ON DELETE NO ACTION,
         FOREIGN KEY(albumUID) REFERENCES album ON DELETE NO ACTION,
         FOREIGN KEY(nameUID) REFERENCES name ON DELETE NO ACTION);''')

print("Table created successfully")

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
conn.close()
