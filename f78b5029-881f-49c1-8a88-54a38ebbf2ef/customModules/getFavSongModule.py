def getFavSong(username,API_KEY):

    import urllib.request
    import json

    dataURL = "http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user="+username+"&api_key="+API_KEY+"&period=7day&format=json"
    
    with urllib.request.urlopen(dataURL) as url:
        data = json.load(url) #loaded as dict
        
    data = data.get("toptracks") #condenses json to important information
    data = data.get("track") #condenses json to important information
    data = data[0] #condenses json to important information

    song = data.get("name")
    artist = data.get("artist")
    artist = artist.get("name")

    return(artist+" - "+song)
