#!/usr/bin/python

# Will contain all of the util function for our DB (insertion, deletion, etc.)

import psycopg2
from psycopg2.extensions import AsIs

conn = psycopg2.connect(database="musiclibrary", user = "trutin", password = "Baseball324!", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

def getFeaturedNames(searchPara, searchCol):  # returns the name of featured artist, input search parameter and the column associated with that search parameter
    featuredInData = ("SELECT nameUID FROM featuredIn WHERE featuredIn.%s = %s;")
    featuredInVals = (AsIs(searchCol), searchPara,)
    cur.execute(featuredInData, featuredInVals)
    rows = cur.fetchall()
    
    if rows:  # if there are featured artists
        tempList = []
        for featuredIn in rows:
            tempList.append(featuredIn[0])
        
        featuredInList = []
        for artist in tempList:
                getNameData = ("SELECT nameString FROM name WHERE name.nameUID = %s;")  # get names of featuredIDs fetched
                getNameVal = (artist,)
                cur.execute(getNameData, getNameVal)
                featuredInList.append(cur.fetchall()[0][0])
        return featuredInList
    else:
        return None

def searchBySongID(songID):
    searchData = ("SELECT * FROM song WHERE song.songUID = %s;")
    searchVals = (songID,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    print("ROWS: ", rows)
    if not rows:  # if song doesn't exist
        return "ERROR: songID does not exist!"

    info = rows[0]
    songList = {}
    songList['songID'] = info[0]
    songList['genre'] = info[1]
    songList['artist'] = info[2]
    featured = getFeaturedNames(songID, "songUID")
    if featured:
        songList['featuredIn'] = featured
    
    return songList

def searchBySongTitle(songTitle):
    searchData = ("SELECT * FROM song WHERE song.songTitle = %s;")
    searchVals = (songTitle,)
    cur.execute(searchData, searchVals)
    rows = cur.fetchall()
    if not rows:  # if query returns nothing
        return "ERROR: songTitle does not exist!"

    print("ROWS", rows)
    info = rows[0]
    songList = {}
    songList['songID'] = info[0]
    songList['genre'] = info[1]
    songList['artist'] = info[2]
    featured = getFeaturedNames(info[0], "songUID")
    if featured:
        songList['featuredIn'] = featured
    return songList

def searchBySongGenre(songGenre):
    searchData = ("SELECT * FROM song WHERE song.genre = %s;")
    searchVals = (songGenre,)
    cur.execute(searchData, searchVals)
    rows = cur.fetchall()
    songList = []
    
    for row in rows:
        tempDict = {}
        tempDict['songID'] = row[0]
        tempDict['genre'] = row[1]
        tempDict['artist'] = row[2]
        featured = getFeaturedNames(row[0], "songUID")
        if featured:
            tempDict['featuredIn'] = featured
        songList.append(tempDict)
    
    return songList

def searchByAlbumID(albumID):
    searchData = ("SELECT * FROM album WHERE album.albumUID = %s;")
    searchVals = (albumID,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    print("ROWS: ", rows)
    if not rows:  # if song doesn't exist
        return "ERROR: songID does not exist!"

    info = rows[0]
    songList = {}
    songList['albumID'] = info[0]
    songList['albumTitle'] = info[1]
    songList['duration'] = info[2]
    songList['releaseDate'] = info[3]

    return songList

def searchByAlbumTitle(albumTitle):
    searchData = ("SELECT * FROM album WHERE album.albumTitle = %s;")
    searchVals = (albumTitle,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    print("ROWS: ", rows)
    if not rows:  # if song doesn't exist
        return "ERROR: songID does not exist!"

    info = rows[0]
    songList = {}
    songList['albumID'] = info[0]
    songList['albumTitle'] = info[1]
    songList['duration'] = info[2]
    songList['releaseDate'] = info[3]

    return songList

def searchByAlbumDate(albumDate):
    searchData = ("SELECT * FROM album WHERE album.releaseDate = %s;")
    searchVals = (albumDate,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    print("ROWS: ", rows)
    if not rows:  # if song doesn't exist
        return "ERROR: songID does not exist!"

    info = rows[0]
    songList = {}
    songList['albumID'] = info[0]
    songList['albumTitle'] = info[1]
    songList['duration'] = info[2]
    songList['releaseDate'] = info[3]

    return songList   