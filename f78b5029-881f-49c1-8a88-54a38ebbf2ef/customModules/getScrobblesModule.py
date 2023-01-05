def getScrobbles(username,API_KEY):

    import urllib.request
    import json

    dataURL2 = "http://ws.audioscrobbler.com/2.0/?method=user.getInfo&user="+username+"&api_key="+API_KEY+"&format=json"

    with urllib.request.urlopen(dataURL2) as url2:
        data2 = json.load(url2) #loaded as dict
    
    data2 = data2.get("user") #condenses json to important information
    data2 = int(data2.get("playcount")) # condenses json to important information
    data2 = f"{data2:,}"
    return data2