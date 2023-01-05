def mostPlayedArtistSongs(username,timeframe,artist,API_KEY):

    import urllib.request
    import json

    def getPageAmount(username,timeframe,API_KEY): #gets the total amount of pages for the user
        dataURL = "http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user="+username+"&api_key="+API_KEY+"&period="+timeframe+"&format=json"
        
        with urllib.request.urlopen(dataURL) as url:
            data = json.load(url) #loaded as dict
            
        data = data.get("toptracks") #condenses json to important information                   
        pages = data.get("@attr") #condenses json to attributes only (includes amount of pages) 
        pages = pages.get("totalPages") #loads amount of pages                                  
        pages = int(pages) #turns amount of pages into int
        
        pages += 1
        
        return pages

    def getPageData(API_KEY,strPages): #gets all data within a page
        dataURL2 = "http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user="+username+"&api_key="+API_KEY+"&page="+strPages+"&period="+timeframe+"&format=json"
        with urllib.request.urlopen(dataURL2) as url2:
            data2 = json.load(url2) #loaded as dict
        
        data2 = data2.get("toptracks") #condenses json to important information
        data2 = data2.get("track") # condenses json to important information
        return data2

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

################################################################################################################

    lst = []
    count = 0

    artist = getArtistName(artist,"c29c8563437753a0c51d5982baae82ed")
    pages = getPageAmount(username,timeframe,"c29c8563437753a0c51d5982baae82ed")
    
    for i in range(pages):
        i+=1
        
        strPages = str(i) #and back into string for the url
        pageData = getPageData("c29c8563437753a0c51d5982baae82ed",strPages)
        
        for i in range(50): #only recieves 50 tracks of data per request
            try:
                temp = pageData[i] #gets the data for "i" track. i goes from 1-50, then moves to next page using the first for loop
            except:
                pass

            tempArtist = temp.get("artist")
            tempArtist = tempArtist.get("name")

            tempAlbum = temp.get("name")

            tempPlays = temp.get("playcount")
            if tempPlays == "1":
                tempPlays = str(tempPlays)+" scrobble"
            else:
                tempPlays = str(tempPlays)+" scrobbles"

            if count < 5:
                if artist == tempArtist:
                    lst.append(tempAlbum+" - "+tempPlays)
                    count += 1
            else:
                return lst
    return lst
