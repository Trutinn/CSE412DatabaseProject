#!/usr/bin/python

# Will create and relate all tables in our database (should only need to be run once per DB)

import psycopg2



conn = psycopg2.connect(database="musiclibrary", user = "USERNAME", password = "PASSWORD", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

cur = conn.cursor()

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

conn.commit()
cur.close()