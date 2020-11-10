#!/usr/bin/python

# Will contain all of the util function for our DB (insertion, deletion, etc.)

import psycopg2
from psycopg2.extensions import AsIs

conn = psycopg2.connect(database="musiclibrary", user = "trutin", password = "Baseball324!", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

def getFeaturedNames(searchPara, searchCol):  # returns the name of featured artist of a song,
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

def producedBy(searchPara, searchCol):  # returns the albums the name produced
    producedByData = ("SELECT albumUID FROM producedBy WHERE producedBy.%s = %s;")
    producedByVals = (AsIs(searchCol), searchPara,)
    cur.execute(producedByData, producedByVals)
    rows = cur.fetchall()
    if rows:  # if they produced something
        tempList = []
        for album in rows:
            tempList.append(album[0])

        producedByList = []
        for album in tempList:
                getAlbumData = ("SELECT albumTitle FROM album WHERE album.albumUID = %s;")  # get album titles
                getAlbumVal = (album,)
                cur.execute(getAlbumData, getAlbumVal)
                producedByList.append(cur.fetchall()[0][0])
        return producedByList
    else:
        return None

def writtenBy(searchPara, searchCol):  # returns the albums the name produced
    writtenByData = ("SELECT albumUID FROM writtenBy WHERE writtenBy.%s = %s;")
    writtenByVals = (AsIs(searchCol), searchPara,)
    cur.execute(writtenByData, writtenByVals)
    rows = cur.fetchall()
    if rows:  # if they wrote something
        tempList = []
        for album in rows:
            tempList.append(album[0])

        writtenByList = []
        for album in tempList:
                getAlbumData = ("SELECT albumTitle FROM album WHERE album.albumUID = %s;")  # get album titles
                getAlbumVal = (album,)
                cur.execute(getAlbumData, getAlbumVal)
                writtenByList.append(cur.fetchall()[0][0])
        return writtenByList
    else:
        return None

def featuredIn(searchPara, searchCol):  # returns songs arist was featured in
    featuredInData = ("SELECT songUID FROM featuredIn WHERE featuredIn.%s = %s;")
    featuredInVals = (AsIs(searchCol), searchPara,)
    cur.execute(featuredInData, featuredInVals)
    rows = cur.fetchall()
    if rows:  # if they wrote something
        tempList = []
        for album in rows:
            tempList.append(album[0])

        featuredInList = []
        for song in tempList:
                getsongData = ("SELECT songTitle FROM song WHERE song.songUID = %s;")  # get song names
                getsongVal = (song,)
                cur.execute(getsongData, getsongVal)
                featuredInList.append(cur.fetchall()[0][0])
        return featuredInList
    else:
        return None    

def performedBy(searchPara, searchCol):
    performedByData = ("SELECT songUID, albumUID FROM performedBy WHERE performedBy.%s = %s;")
    performedByVals = (AsIs(searchCol), searchPara,)
    cur.execute(performedByData, performedByVals)
    rows = cur.fetchall()
    songIDList = []
    albumIDList = []
    if rows:
        for group in rows:
            songIDList.append(group[0])
            if group[1] not in albumIDList:
                albumIDList.append(group[1])
        
        songNameList = []
        albumNameList = []
        for song in songIDList:
                getSongData = ("SELECT songTitle FROM song WHERE song.songUID = %s;")  # get song names
                getSongVal = (song,)
                cur.execute(getSongData, getSongVal)
                songNameList.append(cur.fetchall()[0][0])
        for album in albumIDList:
                getAlbumData = ("SELECT albumTitle FROM album WHERE album.albumUID = %s;")  # get album names
                getAlbumVal = (album,)
                cur.execute(getAlbumData, getAlbumVal)
                albumNameList.append(cur.fetchall()[0][0])    
        return (songNameList, albumNameList)
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
    
    if not rows:  # if query returns nothing
        return "ERROR: songGenre does not exist!"
    
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
    if not rows:  # if query returns nothing
        return "ERROR: albumID does not exist!"

    info = rows[0]
    albumList = {}
    albumList['albumID'] = info[0]
    albumList['albumTitle'] = info[1]
    albumList['duration'] = info[2]
    albumList['releaseDate'] = info[3]

    return albumList

def searchByAlbumTitle(albumTitle):
    searchData = ("SELECT * FROM album WHERE album.albumTitle = %s;")
    searchVals = (albumTitle,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    print("ROWS: ", rows)
    if not rows:  # if query returns nothing  
        return "ERROR: albumTitle does not exist!"

    info = rows[0]
    albumList = {}
    albumList['albumID'] = info[0]
    albumList['albumTitle'] = info[1]
    albumList['duration'] = info[2]
    albumList['releaseDate'] = info[3]

    return albumList

def searchByAlbumDate(albumDate):
    searchData = ("SELECT * FROM album WHERE album.releaseDate = %s;")
    searchVals = (albumDate,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    print("ROWS: ", rows)
    if not rows:  # if query returns nothing  
        return "ERROR: albumDate does not exist!"

    info = rows[0]
    albumList = {}
    albumList['albumID'] = info[0]
    albumList['albumTitle'] = info[1]
    albumList['duration'] = info[2]
    albumList['releaseDate'] = info[3]

    return albumList   

def searchByNameID(nameID):
    searchData = ("SELECT * FROM name WHERE name.nameUID = %s;")
    searchVals = (nameID,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    print("ROWS: ", rows)
    if not rows:  # if query returns nothing  
        return "ERROR: nameID does not exist!"

    info = rows[0]
    nameList = {}
    nameList['nameUID'] = info[0]
    nameList['nameString'] = info[1]
    nameList['knownAs'] = info[2]

    produced = producedBy(nameID, "nameUID")
    if produced:  # if they produced something
        nameList['produced'] = produced
    written = writtenBy(nameID, "nameUID")
    if written:  # if they wrote something
        nameList['wrote'] = written
    featured = featuredIn(nameID, "nameUID")
    if featured:  # if they featured in something
        nameList['featuredIn'] = featured
    performed = performedBy(nameID, "nameUID")
    if performed:  # if they performed something
        nameList['songsPerformed'] = performed[0]
        nameList['albumsPerformed'] = performed[1]

    return nameList   

def searchByName(name):
    searchData = ("SELECT * FROM name WHERE name.nameString = %s;")
    searchVals = (name,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    print("ROWS: ", rows)
    if not rows:  # if query returns nothing  
        return "ERROR: name does not exist!"

    info = rows[0]
    nameList = {}
    nameList['nameUID'] = info[0]
    nameList['nameString'] = info[1]
    nameList['knownAs'] = info[2]

    produced = producedBy(nameList['nameUID'], "nameUID")
    if produced:  # if they produced something
        nameList['produced'] = produced
    written = writtenBy(nameList['nameUID'], "nameUID")
    if written:  # if they wrote something
        nameList['wrote'] = written
    featured = featuredIn(nameList['nameUID'], "nameUID")
    if featured:  # if they featured in something
        nameList['featuredIn'] = featured
    performed = performedBy(nameList['nameUID'], "nameUID")
    if performed:  # if they performed something
        nameList['songsPerformed'] = performed[0]
        nameList['albumsPerformed'] = performed[1]

    return nameList 