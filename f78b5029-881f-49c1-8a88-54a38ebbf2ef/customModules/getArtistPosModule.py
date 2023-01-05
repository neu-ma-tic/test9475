def findArtistPos(username,timeframe,artist,API_KEY):

    import urllib.request
    import json

    def ordinal(numb):
        if numb < 20: #determining suffix for < 20
            if numb == 1: 
                suffix = 'st'
            elif numb == 2:
                suffix = 'nd'
            elif numb == 3:
                suffix = 'rd'
            else:
                suffix = 'th'  
        
        else:   #determining suffix for > 20
            tens = str(numb)
            tens = tens[-2]
            unit = str(numb)
            unit = unit[-1]
            if tens == "1":
                suffix = "th"
            else:
                if unit == "1": 
                    suffix = 'st'
                elif unit == "2":
                    suffix = 'nd'
                elif unit == "3":
                    suffix = 'rd'
                else:
                    suffix = 'th'

        return str(numb)+suffix

    def getPageAmount(API_KEY): #gets the total amount of pages for the user
        dataURL = "http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user="+username+"&api_key="+API_KEY+"&period="+timeframe+"&format=json"
        
        with urllib.request.urlopen(dataURL) as url:
            data = json.load(url) #loaded as dict
            
        data = data.get("topartists") #condenses json to important information                   
        pages = data.get("@attr") #condenses json to attributes only (includes amount of pages) 
        pages = pages.get("totalPages") #loads amount of pages                                  
        pages = int(pages) #turns amount of pages into int
        
        pages += 1
        
        return pages

    def getPageData(API_KEY,strPages): #gets all data within a page
        dataURL2 = "http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user="+username+"&api_key="+API_KEY+"&page="+strPages+"&period="+timeframe+"&format=json"

        with urllib.request.urlopen(dataURL2) as url2:
            data2 = json.load(url2) #loaded as dict
        
        data2 = data2.get("topartists") #condenses json to important information
        data2 = data2.get("artist") # condenses json to important information
        return data2

    try:
        artist = artist.replace("_","+")
    except:
        pass

    artist = getArtistName(artist,API_KEY)
    pages = getPageAmount(API_KEY)

    for i in range(1,pages):

        strPages = str(i) #and back into string for the url
        pageData = getPageData(API_KEY,strPages)
        
        for i in range(50): #only recieves 50 tracks of data per request
            try:
                temp = pageData[i] #gets the data for "i" track. i goes from 1-50, then moves to next page using the first for loop
            except:
                pass

            tempRank = temp.get("@attr")
            tempRank = tempRank.get("rank")
            tempArtist = temp.get("name")

            if artist == tempArtist:
                tempRank = ordinal(int(tempRank))
                return tempRank

            else:
                pass

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