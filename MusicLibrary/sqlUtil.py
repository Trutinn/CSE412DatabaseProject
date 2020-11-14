#!/usr/bin/python

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

def albumProducedBy(searchPara, searchCol):
    producedByData = ("SELECT nameUID FROM producedBy WHERE producedBy.%s = %s;")
    producedByVals = (AsIs(searchCol), searchPara,)
    cur.execute(producedByData, producedByVals)
    rows = cur.fetchall()
    if rows:  # if there is a produced on album
        tempList = []
        for album in rows:
            tempList.append(album[0])

        producedByList = []
        for album in tempList:
                getAlbumData = ("SELECT nameString FROM name WHERE name.nameUID = %s;")  # get album titles
                getAlbumVal = (album,)
                cur.execute(getAlbumData, getAlbumVal)
                producedByList.append(cur.fetchall()[0][0])
        return producedByList
    else:
        return None

def albumWrittenBy(searchPara, searchCol):
    writtenByData = ("SELECT nameUID FROM writtenBy WHERE writtenBy.%s = %s;")
    writtenByVals = (AsIs(searchCol), searchPara,)
    cur.execute(writtenByData, writtenByVals)
    rows = cur.fetchall()
    if rows:  # if there is a produced on album
        tempList = []
        for album in rows:
            tempList.append(album[0])

        writtenByList = []
        for album in tempList:
                getAlbumData = ("SELECT nameString FROM name WHERE name.nameUID = %s;")  # get album titles
                getAlbumVal = (album,)
                cur.execute(getAlbumData, getAlbumVal)
                writtenByList.append(cur.fetchall()[0][0])
        return writtenByList
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

def getArtistFromSong(songID):
    searchData = ("SELECT nameUID FROM performedBy WHERE performedBy.songUID = %s;")
    searchVals = (songID,)
    cur.execute(searchData, searchVals) 

    rows = cur.fetchall()  
    nameUID = rows[0][0]

    searchData = ("SELECT nameString FROM name WHERE name.nameUID = %s;")
    searchVals = (nameUID,)
    cur.execute(searchData, searchVals)   

    rows = cur.fetchall()
    return rows[0][0]

def searchBySongID(songID):
    searchData = ("SELECT * FROM song WHERE song.songUID = %s;")
    searchVals = (songID,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    if not rows:  # if song doesn't exist
        return "ERROR: songID does not exist!"

    info = rows[0]
    songList = {}
    songList['songID'] = info[0]
    songList['genre'] = info[1]
    songList['songName'] = info[2]
    songList['artist'] = getArtistFromSong(songList['songID'])
    featured = getFeaturedNames(songID, "songUID")
    if featured:
        songList['featuredIn'] = featured
    
    getArtistFromSong(songID)
    
    return songList

def searchBySongTitle(songTitle):
    searchData = ("SELECT * FROM song WHERE song.songTitle = %s;")
    searchVals = (songTitle,)
    cur.execute(searchData, searchVals)
    rows = cur.fetchall()
    if not rows:  # if query returns nothing
        return "ERROR: songTitle does not exist!"

    songDict = {}
    counter = 0
    for info in rows:
        songList = {}
        songList['songID'] = info[0]
        songList['genre'] = info[1]
        songList['songName'] = info[2]
        songList['artist'] = getArtistFromSong(songList['songID'])
        featured = getFeaturedNames(info[0], "songUID")
        if featured:
            songList['featuredIn'] = featured
        songDict[counter] = songList
        counter += 1
    return songDict

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
        tempDict['songName'] = row[2]
        tempDict['artist'] = getArtistFromSong(tempDict['songID'])
        featured = getFeaturedNames(row[0], "songUID")
        if featured:
            tempDict['featuredIn'] = featured
        songList.append(tempDict)
    
    return songList

def searchSongsInAlbum(albumID):
    searchData = ("SELECT songUID FROM contains WHERE contains.albumUID = %s;")
    searchVals = (albumID,)
    cur.execute(searchData, searchVals)   

    songUIDList = cur.fetchall()
    songNameList = []
    for songID in songUIDList:
        searchData = ("SELECT songTitle FROM song WHERE song.songUID = %s;")
        searchVals = (songID[0],)
        cur.execute(searchData, searchVals) 
        songNameList.append(cur.fetchall()[0][0])
    return songNameList

def searchByAlbumID(albumID):
    searchData = ("SELECT * FROM album WHERE album.albumUID = %s;")
    searchVals = (albumID,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    if not rows:  # if query returns nothing
        return "ERROR: albumID does not exist!"

    info = rows[0]
    albumList = {}
    albumList['albumID'] = info[0]
    albumList['albumTitle'] = info[1]
    albumList['duration'] = info[2]
    albumList['releaseDate'] = info[3]
    albumList['songsInAlbum'] = searchSongsInAlbum(albumList['albumID'])
    searchSongsInAlbum(albumList['albumID'])
    produced = albumProducedBy(albumID, "albumUID")
    if produced:
        albumList['producedBy'] = produced
    written = albumWrittenBy(albumID, "albumUID")
    if written:
        albumList['writtenBy'] = written

    return albumList

def searchByAlbumTitle(albumTitle):
    searchData = ("SELECT * FROM album WHERE album.albumTitle = %s;")
    searchVals = (albumTitle,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    if not rows:  # if query returns nothing  
        return "ERROR: albumTitle does not exist!"

    albumDict = {}
    counter = 0
    for info in rows:
        albumList = {}
        albumList['albumID'] = info[0]
        albumList['albumTitle'] = info[1]
        albumList['duration'] = info[2]
        albumList['releaseDate'] = info[3]
        albumList['songsInAlbum'] = searchSongsInAlbum(albumList['albumID'])
        produced = albumProducedBy(albumList['albumID'], "albumUID")
        if produced:
            albumList['producedBy'] = produced
        written = albumWrittenBy(albumList['albumID'], "albumUID")
        if written:
            albumList['writtenBy'] = written
        albumDict[counter] = albumList
        counter += 1

    return albumDict

def searchByAlbumDate(albumDate):
    searchData = ("SELECT * FROM album WHERE album.releaseDate = %s;")
    searchVals = (albumDate,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
    if not rows:  # if query returns nothing  
        return "ERROR: albumDate does not exist!"

    albumDict = {}
    counter = 0
    for info in rows:
        albumList = {}
        albumList['albumID'] = info[0]
        albumList['albumTitle'] = info[1]
        albumList['duration'] = info[2]
        albumList['releaseDate'] = info[3]
        albumList['songsInAlbum'] = searchSongsInAlbum(albumList['albumID'])
        produced = albumProducedBy(albumList['albumID'], "albumUID")
        if produced:
            albumList['producedBy'] = produced
        written = albumWrittenBy(albumList['albumID'], "albumUID")
        if written:
            albumList['writtenBy'] = written
        albumDict[counter] = albumList
        counter += 1

    return albumDict 

def searchByNameID(nameID):
    searchData = ("SELECT * FROM name WHERE name.nameUID = %s;")
    searchVals = (nameID,)
    cur.execute(searchData, searchVals)
   
    rows = cur.fetchall()
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
    if not rows:  # if query returns nothing  
        return "ERROR: name does not exist!"

    namesDict = {}
    counter = 0
    for info in rows:
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
        namesDict[counter] = nameList
        counter += 1
    return namesDict 

def insertName(ID, name, knownAs):
    searchData = ("SELECT * FROM name WHERE name.nameUID = %s;")
    searchVals = (ID,)
    cur.execute(searchData, searchVals)
    rows = cur.fetchall()
    if rows:  # if ID is a duplicate
        return "ERROR: None unique ID"

    insertData = ("""INSERT INTO name (nameUID, nameString, knownAs) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING""")
    insertVals = (ID, name, knownAs)
    cur.execute(insertData, insertVals)
    conn.commit()
    return "Successfully inserted!"
    
def insertAlbum(albumId, albumTitle, duration, releaseDate, writerID, producerID):
    searchData = ("SELECT * FROM album WHERE album.albumUID = %s;")
    searchVals = (albumId,)
    cur.execute(searchData, searchVals)
    rows = cur.fetchall()
    if rows:  # if ID is a duplicate
        return "ERROR: None unique ID" 
        
    searchData = ("SELECT * FROM name WHERE name.nameUID = %s;")
    searchVals = (writerID,)
    cur.execute(searchData, searchVals)
    rows = cur.fetchall()
    if not rows:  # if ID does not exist
        return "ERROR: Writer ID does not exist!"   

    searchData = ("SELECT * FROM name WHERE name.nameUID = %s;")
    searchVals = (producerID,)
    cur.execute(searchData, searchVals)
    rows = cur.fetchall()
    if not rows:  # if ID does not exist
        return "ERROR: Producer ID does not exist!" 
    
    insertData = ("""INSERT INTO album (albumUID, albumTitle, duration, releaseDate) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING""")
    insertVals = (albumId, albumTitle, duration, releaseDate)
    cur.execute(insertData, insertVals)
    conn.commit()  # insert the album

    insertData = ("""INSERT INTO writtenBy (albumUID, nameUID) VALUES (%s, %s) ON CONFLICT DO NOTHING""")
    insertVals = (albumId, writerID)
    cur.execute(insertData, insertVals)
    conn.commit()  # insert writtenBy relationship

    insertData = ("""INSERT INTO producedBy (albumUID, nameUID) VALUES (%s, %s) ON CONFLICT DO NOTHING""")
    insertVals = (albumId, producerID)
    cur.execute(insertData, insertVals)
    conn.commit()  # insert producedBy relationship

    return "Album Successfully Inserted!"

def insertSong(songId, songTitle, genre, albumId, artistID, featArtistIDList):
    searchData = ("SELECT * FROM song WHERE song.songUID = %s;")
    searchVals = (songId,)
    cur.execute(searchData, searchVals)
    rows = cur.fetchall()
    if rows:  # if songID is a duplicate
        return "ERROR: None unique songID" 

    searchData = ("SELECT * FROM album WHERE album.albumUID = %s;")
    searchVals = (albumId,)
    cur.execute(searchData, searchVals)
    rows = cur.fetchall()
    if not rows:  # if albumID does not exist
        return "ERROR: AlbumID does not exist" 

    searchData = ("SELECT * FROM name WHERE name.nameUID = %s;")
    searchVals = (artistID,)
    cur.execute(searchData, searchVals)
    rows = cur.fetchall()
    if not rows:  # if ArtistID does not exist
        return "ERROR: ArtistID does not exist" 
    
    if featArtistIDList != '':
        featIDList = featArtistIDList.split(',')
        for aID in featIDList:
            searchData = ("SELECT * FROM name WHERE name.nameUID = %s;")
            searchVals = (aID,)
            cur.execute(searchData, searchVals)
            rows = cur.fetchall()
            if not rows:  # if a featured artist does not exist
                return "ERROR: A featured artist ID does not exist" 

    insertData = ("""INSERT INTO song (songUID, genre, songTitle) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING""")
    insertVals = (songId, genre, songTitle)
    cur.execute(insertData, insertVals)
    conn.commit()  # insert song

    insertData = ("""INSERT INTO contains (songUID, albumUID) VALUES (%s, %s) ON CONFLICT DO NOTHING""")
    insertVals = (songId, albumId)
    cur.execute(insertData, insertVals)
    conn.commit()  # insert contains relationship

    insertData = ("""INSERT INTO performedBy (songUID, albumUID, nameUID) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING""")
    insertVals = (songId, albumId, artistID)
    cur.execute(insertData, insertVals)
    conn.commit()  # insert contains relationship   
    if featArtistIDList != '':
        for aID in featIDList:
            insertData = ("""INSERT INTO featuredIn (songUID, nameUID) VALUES (%s, %s) ON CONFLICT DO NOTHING""")
            insertVals = (songId, aID)
            cur.execute(insertData, insertVals)
            conn.commit()  # insert contains relationship     

    return "Song Successfully Inserted!" 