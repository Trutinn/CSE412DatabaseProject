#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="musiclibrary", user = "trutin", password = "Baseball324!", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

cur = conn.cursor()
# ADD REMAINING TABLES
def printAllTables():
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
    for row in rows:
        print ("SONG: ", row)

    cur.execute("SELECT * FROM album")
    rows = cur.fetchall()
    for row in rows:
        print ("ALBUM: ", row)  

    cur.execute("SELECT * FROM name")
    rows = cur.fetchall()
    for row in rows:
        print ("NAME: ", row)

    cur.execute("SELECT * FROM artist")
    rows = cur.fetchall()
    for row in rows:
        print ("ARTIST: ", row)

    cur.execute("SELECT * FROM writer")
    rows = cur.fetchall()
    for row in rows:
        print ("WRITER: ", row)

    cur.execute("SELECT * FROM producer")
    rows = cur.fetchall()
    for row in rows:
        print ("PRODUCER: ", row)

    cur.execute("SELECT * FROM producedby")
    rows = cur.fetchall()
    for row in rows:
        print ("PRODUCEDBY: ", row)

    cur.execute("SELECT * FROM writtenBy")
    rows = cur.fetchall()
    for row in rows:
        print ("WRITTENBY: ", row)

    cur.execute("SELECT *  FROM featuredIn")
    rows = cur.fetchall()
    for row in rows:
        print ("FEATUREDIN: ", row)

    cur.execute("SELECT *  FROM performedBy")
    rows = cur.fetchall()
    for row in rows:
        print ("PERFORMEDBY: ", row)

    cur.execute("SELECT *  FROM contains")
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

def printNameTable():
    cur.execute("SELECT *  FROM name WHERE name.nameUID = '4q3ewBCX7sLwd24euuV69X';")
    rows = cur.fetchall()
    for row in rows:
        print ("NAME: ", row)
    
    cur.execute("SELECT *  FROM artist WHERE artist.nameUID = '4q3ewBCX7sLwd24euuV69X';")
    rows = cur.fetchall()
    for row in rows:
        print ("ARTIST: ", row)
    
    cur.execute("SELECT *  FROM featuredIn WHERE featuredIn.nameUID = '4q3ewBCX7sLwd24euuV69X';")
    rows = cur.fetchall()
    for row in rows:
        print ("FEATUREDIN: ", row)

    cur.execute("SELECT *  FROM performedBy WHERE performedBy.nameUID = '4q3ewBCX7sLwd24euuV69X';")
    rows = cur.fetchall()
    for row in rows:
        print ("PERFORMEDBY: ", row)

def testingInsertion():
    print("BEFORE INSERTION")
    cur.execute("SELECT *  FROM name;")
    rows = cur.fetchall()
    for row in rows:
        print ("NAME: ", row)   

    insertData = ("""INSERT INTO name (nameUID, nameString, knownAs) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING""")
    insertVals = ('UGuvJcJbk37ps77mZkcxHm', 'customArtist', 'customArtist')
    cur.execute(insertData, insertVals)

    print("AFTER INSERTION")
    cur.execute("SELECT *  FROM name;")
    rows = cur.fetchall()
    for row in rows:
        print ("NAME: ", row)  

def testingUpdate():
    print("BEFORE UPDATE")
    cur.execute("SELECT *  FROM name;")
    rows = cur.fetchall()
    for row in rows:
        print ("NAME: ", row)  
    
    updateData = ("""UPDATE name SET nameString = (%s) WHERE nameUID = (%s)""")
    updateVals = ("newName", "UGuvJcJbk37ps77mZkcxHm")
    cur.execute(updateData, updateVals)
    print("AFTER UPDATE\n")
    cur.execute("SELECT *  FROM name;")
    rows = cur.fetchall()
    for row in rows:
        print ("NAME: ", row)  

def testingNameDeletion():
    print("BEFORE DELETION")
    printNameTable()
    cur.execute("DELETE FROM name WHERE name.nameUID = '4q3ewBCX7sLwd24euuV69X';")
    print("AFTER DELETION")
    printNameTable()

def testingSelection():
    cur.execute("""SELECT name.nameString, song.songTitle 
                FROM name, song, featuredIn
                WHERE name.nameUID = featuredIn.nameUID AND
                song.songUID = featuredIn.songUID;""")
    for row in cur.fetchall():
        print("Featured in artists: ", row)

def testingSelection2():
    cur.execute("""SELECT DISTINCT name.nameString, album.albumTitle
                FROM name, artist, album, performedBy
                WHERE artist.nameUID = performedBy.nameUID AND
                album.albumUID = performedBy.albumUID AND
                name.nameUID = artist.nameUID;""")
    for row in cur.fetchall():
        print("Featured in artists: ", row)
    
#testingNameDeletion()
#testingInsertion()
#testingUpdate() 
#testingSelection()
#testingSelection2()
printAllTables()



conn.close()
cur.close()