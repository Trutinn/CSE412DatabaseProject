from flask import Flask, render_template, request, redirect, url_for
from sqlUtil import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('homePage.html')

@app.route('/Search_By_SID', methods=['post', 'get'])
def Search_By_SID():
    songID = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        songID = request.form.get('songId')  # access the data inside
        if songID == '':
            return render_template('SearchBySongID.html') # Will likely not actually need here.
        else: 
            data = searchBySongID(songID)
            if isinstance(data, str):
                return render_template('searchError.html', data = searchBySongID(songID))
            else:
                return render_template('songIDResults.html', data = searchBySongID(songID)) # The area that is run after something is submitted.
    
    return render_template('SearchBySongID.html') # This is the get area as it is outside of the if area.

@app.route('/Search_By_AID', methods=['post', 'get'])
def Search_By_AID():
    albumId = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        albumId = request.form.get('albumId')  # access the data inside
        if albumId == '':
            return render_template('SearchByAlbumID.html') # Will likely not actually need here.
        else:
            data = searchByAlbumID(albumId)
            if isinstance(data, str):
                return render_template('searchError.html', data = searchByAlbumID(albumId))
            else:
                return render_template('albumIDResults.html', data = searchByAlbumID(albumId))  #return searchByAlbumID(albumId) # The area that is run after something is submitted.

    return render_template('SearchByAlbumID.html') # This is the get area as it is outside of the if area.

@app.route('/Search_By_ArtID', methods=['post', 'get'])
def Search_By_ArtID():
    artistId = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        artistId = request.form.get('artistId')  # access the data inside
        if artistId == '':
            return render_template('SearchByArtistID.html') # Will likely not actually need here.
        else:
            data = searchByNameID(artistId)
            if isinstance(data, str):
                return render_template('searchError.html', data = searchByNameID(artistId))
            else:
                return render_template('artistIDResults.html', data = searchByNameID(artistId))   #return searchByNameID(artistId) # The area that is run after something is submitted.

    return render_template('SearchByArtistID.html') # This is the get area as it is outside of the if area.

@app.route('/Insert_Album', methods=['post', 'get'])
def Insert_Album():
    albumId = ''
    albumTitle = ''
    duration = 0.0
    releaseDate = ''
    writerID = ''
    producerID = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        albumId = request.form.get('albumId')  # access the data inside
        albumTitle = request.form.get('albumTitle')  # access the data inside
        duration = request.form.get('duration')  # access the data inside
        releaseDate = request.form.get('releaseDate')  # access the data inside
        writerID = request.form.get('writerID')  # access the data inside
        producerID = request.form.get('producerID')  # access the data inside
        if albumId == '' or albumTitle == '' or duration == 0.0 or releaseDate == '' or writerID == '' or producerID == '':
            return render_template('InsertAlbum.html') # Will likely not actually need here.
        else:
            try:
                float(duration)
            except:
                try:
                    int(duration)
                except:
                    return render_template('insertAlbumMessages.html', message = "Error! A non-numeric value was entered for the duration. Please use the back arrow on your browser to return to the previous page.")
            return render_template('insertAlbumMessages.html', message = insertAlbum(albumId,albumTitle,duration,releaseDate,writerID,producerID)) # return insertAlbum(albumId,albumTitle,duration,releaseDate,writerID,producerID) # The area that is run after something is submitted.

    return render_template('InsertAlbum.html') # This is the get area as it is outside of the if area.

@app.route('/Insert_Artist', methods=['post', 'get'])
def Insert_Artist():
    artistId = ''
    nameString = ''
    knownAS = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        artistId = request.form.get('artistId')  # access the data inside
        nameString = request.form.get('nameString')  # access the data inside
        knownAS = request.form.get('knownAS')  # access the data inside
        if artistId == '' or nameString == '' or knownAS == '':
            return render_template('InsertArtist.html') # Will likely not actually need here.
        else:
            return render_template('insertArtistMessage.html', message = insertName(artistId, nameString, knownAS))  #return insertName(artistId, nameString, knownAS)  # The area that is run after something is submitted.

    return render_template('InsertArtist.html') # This is the get area as it is outside of the if area.



@app.route('/Insert_Song', methods=['post', 'get'])
def Insert_Song():
    songId = ''
    songTitle = ''
    genre = ''
    albumId = ''
    artistID = ''
    featArtistIDList = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        songId = request.form.get('songId')  # access the data inside
        songTitle = request.form.get('songTitle')  # access the data inside
        genre = request.form.get('genre')  # access the data inside
        albumId = request.form.get('albumId')  # access the data inside
        artistID = request.form.get('artistID')  # access the data inside
        featArtistIDList = request.form.get('featArtistID')  # access the data inside
        if songId == '' or songTitle == '' or genre == '' or albumId == '' or artistID == '':
            return render_template('InsertSong.html') # Will likely not actually need here.
        else:
            return render_template('insertSongMessage.html', message = insertSong(songId, songTitle, genre, albumId, artistID, featArtistIDList)) #return insertSong(songId, songTitle, genre, albumId, artistID, featArtistIDList) # The area that is run after something is submitted.

    return render_template('InsertSong.html') # This is the get area as it is outside of the if area.


@app.route('/Search_By_ATitle', methods=['post', 'get'])
def Search_By_ATitle():
    albumTitle = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        albumTitle = request.form.get('albumTitle')  # access the data inside
        if albumTitle == '':
            return render_template('SearchByAlbumTitle.html') # Will likely not actually need here.
        else:
            data = searchByAlbumTitle(albumTitle)
            if isinstance(data, str):
                return render_template('searchError.html', data = searchByAlbumTitle(albumTitle))
            else:
                return render_template('albumTitleResults.html', songInfo = searchByAlbumTitle(albumTitle)) # return searchByAlbumTitle(albumTitle) # The area that is run after something is submitted.

    return render_template('SearchByAlbumTitle.html') # This is the get area as it is outside of the if area.


@app.route('/Search_By_ArtName', methods=['post', 'get'])
def Search_By_ArtName():
    knownAS = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        knownAS = request.form.get('knownAS')  # access the data inside
        if knownAS == '':
            return render_template('SearchByArtistName.html') # Will likely not actually need here.
        else:
            data = searchByName(knownAS)
            if isinstance(data, str):
                return render_template('searchError.html', data = searchByName(knownAS))
            else:
                return render_template('artistTitleResults.html', songInfo = searchByName(knownAS)) #return searchByName(knownAS) # The area that is run after something is submitted.

    return render_template('SearchByArtistName.html') # This is the get area as it is outside of the if area.


@app.route('/Search_By_Date', methods=['post', 'get'])
def Search_By_Date():  # currently have to search by specific date "YYYY-MM-DD"
    date = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        date = request.form.get('releaseDate')  # access the data inside
        if date == '':
            return render_template('SearchByDate.html') # Will likely not actually need here.
        else:
            data = searchByAlbumDate(date)
            if isinstance(data, str):
                return render_template('searchError.html', data = searchByAlbumDate(date))
            else:
                return render_template('albumTitleResults.html', songInfo = searchByAlbumDate(date)) # return searchByAlbumDate(date) # The area that is run after something is submitted.
            

    return render_template('SearchByDate.html') # This is the get area as it is outside of the if area.


@app.route('/Search_By_Genre', methods=['post', 'get'])
def Search_By_Genre():
    genre = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        genre = request.form.get('genre')  # access the data inside
        if genre == '':
            return render_template('SearchByGenre.html') # Will likely not actually need here.
        else:
            #tempDict = {}
            #tempDict['songs'] = searchBySongGenre(genre) 
            data = searchBySongGenre(genre)
            if isinstance(data, str):
                return render_template('searchError.html', data = searchBySongGenre(genre))
            else:
                return render_template('songGenreResults.html', songInfo = searchBySongGenre(genre)) # The area that is run after something is submitted.

    return render_template('SearchByGenre.html') # This is the get area as it is outside of the if area.

@app.route('/Search_By_STitle', methods=['post', 'get'])
def Search_By_STitle():
    songTitle = ''
    if request.method == 'POST': #This is the area where the submit has been posted?
        songTitle = request.form.get('songTitle')  # access the data inside
        if songTitle == '':
            return render_template('SearchBySongTitle.html') # Will likely not actually need here.
        else: 
            data = searchBySongTitle(songTitle)
            print(data)
            if isinstance(data, str):
                return render_template('searchError.html', data = searchBySongTitle(songTitle))
            else:
                return render_template('songTitleResults.html', songInfo = searchBySongTitle(songTitle)) # The area that is run after something is submitted.


            
            
            

    return render_template('SearchBySongTitle.html') # This is the get area as it is outside of the if area.

if __name__ == '__main__':
    app.debug = True
    app.run() #go to http://localhost:5000/ to view the page.
