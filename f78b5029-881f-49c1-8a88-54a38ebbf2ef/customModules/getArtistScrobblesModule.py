def getArtistScrobbles(username,artist,API_KEY):

    import urllib.request
    import json
    import re
    dataURL2 = "http://ws.audioscrobbler.com/2.0/?method=artist.getInfo&user="+username+"&artist="+artist+"&api_key="+API_KEY+"&format=json"

    with urllib.request.urlopen(dataURL2) as url2:
        data = json.load(url2) #loaded as dict
    
    plays = data.get("artist") #condenses json to important information
    plays = plays.get("stats") # condenses json to important information
    plays = int(plays.get("userplaycount"))
    plays = f"{plays:,}"

    try:
        artist = data.get("artist") #condenses json to important information
        artist = artist.get("name") # condenses json to important information
    except:
        pass

    lst = [plays,artist]
    return lst