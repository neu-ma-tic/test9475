def getArtistName(artist,API_KEY):

    import urllib.request
    import json

    try:
        artist = artist.replace("_","+")
    except:
        pass

    dataURL2 = "http://ws.audioscrobbler.com/2.0/?method=artist.getInfo&artist="+artist+"&api_key="+API_KEY+"&format=json"
    with urllib.request.urlopen(dataURL2) as url2:
        data = json.load(url2) #loaded as dict
    
    artist = data.get("artist")
    artist = artist.get("name")
    
    return artist

def getUsername(username,API_KEY):

    import urllib.request
    import json

    dataURL2 = "http://ws.audioscrobbler.com/2.0/?method=user.getInfo&user="+username+"&api_key="+API_KEY+"&format=json"
    with urllib.request.urlopen(dataURL2) as url2:
        data = json.load(url2) #loaded as dict
    
    username = data.get("user")
    username = username.get("name")
    
    return username

def getTimeframe(timeframe):
    lst = ["7day","1month","3month","6month","12month","overall"]
    if timeframe in lst:
        return timeframe
    else:
        return None

def parseForURL(artist):
    import urllib
    artist = urllib.parse.quote(artist)
    artist = artist.replace("%2B","+") #it makes the + in url go fucky fucky mode for artists with more than 1 word etc james blake
    return artist