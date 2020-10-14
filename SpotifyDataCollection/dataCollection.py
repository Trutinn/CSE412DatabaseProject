import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

cid = '6cd8bdd0db9642419e0c9405bf721545'
secret = '21450a1555a74c3197b93188406817be'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# File object for writing JSON
f = open("dataSet.json","w")

# Store JSON album objects
musicDataList = []

# Loading albums
for i in range(0, 10, 1):  # number of albums pulled, second number/third number = total pulled
    albums = sp.search(q='year:2020', type='album', limit=1, offset = i)  # pulling albums from spotify API
    for x, t in enumerate(albums['albums']['items']):  # parsing through JSON file
        # Creating variables to be populated with album data
        artistName = []
        artistID = []
        trackIDs = []
        trackNames = []
        featuredName = []
        featuredIDs = []
        
        albumID = t['id']  
        albumName = t['name']
        for artist in t['artists']:  # entering nested artist object in JSON
            artistName.append(artist['name'])
            artistID.append(artist['id'])
        #print("album genre: ", t['genres'])
        leadArtistName=artistName[0]
        leadArtistID=artistID[0]
        albumReleaseDate = t['release_date']

        albumTracks = sp.album_tracks(t['id'], limit=t['total_tracks'], offset = 0, market=None) #  getting tracks in album  
        albumDurationTemp = 0  
        for i in range(0,t['total_tracks']):  # getting all of the info for each nested track
            trackIDs.append(albumTracks['items'][i]['id'])
            trackNames.append(albumTracks['items'][i]['name'])
            albumDurationTemp+=albumTracks['items'][i]['duration_ms']/1000  # duration in seconds

            tempFeaturedInName = []
            tempFeaturedInID = []
            for x, t in enumerate(albumTracks['items'][i]['artists']):  # getting featured artists per track
                tempFeaturedInName.append(t['name'])
                tempFeaturedInID.append(t['id'])
            featuredName.append(tempFeaturedInName)
            featuredIDs.append(tempFeaturedInID)
        albumDuration = albumDurationTemp

    # Creating data for the JSON
    songList = []
    idList = []
    nameList = []
    for id in trackIDs:
        idList.append(id)
    for name in trackNames:
        nameList.append(name)
    # Prepping data from API for JSON object
    for i in range(0,len(trackIDs)):
        featuredInList = []
        for j in range(1,len(featuredIDs[i])):
            featuredInList.append({"id":featuredIDs[i][j], "name":featuredName[i][j]})
        songList.append({"id":idList[i],"name":nameList[i], "genre":"Rap", "featuredIn":featuredInList})

    # Creating JSON object
    albumPackage = {
        "albumID":albumID,
        "albumTitle":albumName,
        "artistID":leadArtistID,
        "artistName":leadArtistName,
        "albumDuration":albumDuration,
        "albumReleaseDate":albumReleaseDate,
        "producedBy": [{"id":"", "name":""}],
        "writtenBy": [],
        "songs":songList
    }

    musicDataList.append(albumPackage)
    

musicData = {
    "musicData":musicDataList
}

f.write(json.dumps(musicData, indent=4))

f.close()
    