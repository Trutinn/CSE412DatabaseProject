#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="musiclibrary", user = "trutin", password = "YOURPW", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

cur = conn.cursor()
# ADD REMAINING TABLES
def printAllTables():
   cur.execute("SELECT * FROM song WHERE song.songUID = '0fgsKar6uBO08vzHXkTjWi';")
   rows = cur.fetchall()
   for row in rows:
      print ("SONG: ", row)

   cur.execute("SELECT *  FROM featuredIn WHERE featuredIn.songUID = '0fgsKar6uBO08vzHXkTjWi';")
   rows = cur.fetchall()
   for row in rows:
      print ("FEATUREDIN: ", row)

   cur.execute("SELECT *  FROM performedBy WHERE performedBy.songUID = '0fgsKar6uBO08vzHXkTjWi';")
   rows = cur.fetchall()
   for row in rows:
      print ("PERFORMEDBY: ", row)

   cur.execute("SELECT *  FROM contains WHERE contains.songUID = '0fgsKar6uBO08vzHXkTjWi';")
   rows = cur.fetchall()
   for row in rows:
      print ("CONTAINS: ", row)   

def printingTablesSong():
   cur.execute("SELECT * FROM song WHERE song.songUID = '0fgsKar6uBO08vzHXkTjWi';")
   rows = cur.fetchall()
   for row in rows:
      print ("SONG: ", row)

   cur.execute("SELECT *  FROM featuredIn WHERE featuredIn.songUID = '0fgsKar6uBO08vzHXkTjWi';")
   rows = cur.fetchall()
   for row in rows:
      print ("FEATUREDIN: ", row)

   cur.execute("SELECT *  FROM performedBy WHERE performedBy.songUID = '0fgsKar6uBO08vzHXkTjWi';")
   rows = cur.fetchall()
   for row in rows:
      print ("PERFORMEDBY: ", row)

   cur.execute("SELECT *  FROM contains WHERE contains.songUID = '0fgsKar6uBO08vzHXkTjWi';")
   rows = cur.fetchall()
   for row in rows:
      print ("CONTAINS: ", row)

def printingTablesAlbum():
   cur.execute("SELECT * FROM album WHERE album.albumUID = '5lJqux7orBlA1QzyiBGti1';")
   rows = cur.fetchall()
   for row in rows:
      print ("album: ", row)

   cur.execute("SELECT *  FROM performedBy WHERE performedBy.albumUID = '5lJqux7orBlA1QzyiBGti1';")
   rows = cur.fetchall()
   for row in rows:
      print ("PERFORMEDBY: ", row)

   cur.execute("SELECT *  FROM contains WHERE contains.albumUID = '5lJqux7orBlA1QzyiBGti1';")
   rows = cur.fetchall()
   for row in rows:
      print ("CONTAINS: ", row)

def printingTablesName():
    cur.execute("SELECT *  FROM name WHERE name.nameUID = '4SsVbpTthjScTS7U2hmr1X';")
    rows = cur.fetchall()
    for row in rows:
        print ("NAME: ", row)
    
    cur.execute("SELECT *  FROM artist WHERE artist.nameUID = '4SsVbpTthjScTS7U2hmr1X';")
    rows = cur.fetchall()
    for row in rows:
        print ("ARTIST: ", row)
    
    cur.execute("SELECT *  FROM featuredIn WHERE featuredIn.nameUID = '4SsVbpTthjScTS7U2hmr1X';")
    rows = cur.fetchall()
    for row in rows:
        print ("FEATUREDIN: ", row)

    cur.execute("SELECT *  FROM performedBy WHERE performedBy.nameUID = '4SsVbpTthjScTS7U2hmr1X';")
    rows = cur.fetchall()
    for row in rows:
        print ("PERFORMEDBY: ", row)

printAllTables()

conn.close()
cur.close()