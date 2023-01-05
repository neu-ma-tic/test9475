def mostPlayedArtistsAlbums(username,timeframe,artist,API_KEY):

    import urllib.request
    import json

    URLartist = artist.replace(" ","+")

    def getPageAmount(username,timeframe,API_KEY): #gets the total amount of pages for the user
        dataURL = "http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user="+username+"&api_key="+API_KEY+"&period="+timeframe+"&format=json"
        
        with urllib.request.urlopen(dataURL) as url:
            data = json.load(url) #loaded as dict
            
        data = data.get("topalbums") #condenses json to important information                   
        pages = data.get("@attr") #condenses json to attributes only (includes amount of pages) 
        pages = pages.get("totalPages") #loads amount of pages                                  
        pages = int(pages) #turns amount of pages into int
        
        pages += 1
        
        return pages

    def getPageData(API_KEY,strPages): #gets all data within a page
        dataURL2 = "http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user="+username+"&api_key="+API_KEY+"&page="+strPages+"&period="+timeframe+"&format=json"

        with urllib.request.urlopen(dataURL2) as url2:
            data2 = json.load(url2) #loaded as dict
        
        data2 = data2.get("topalbums") #condenses json to important information
        data2 = data2.get("album") # condenses json to important information
        return data2

    def getArtistName(artist,API_KEY):

        import urllib.request
        import json

        try:
            artist = artist.replace("_","+")
        except:
            pass

        dataURL2 = "http://ws.audioscrobbler.com/2.0/?method=artist.getInfo&artist="+URLartist+"&api_key="+API_KEY+"&format=json"
        with urllib.request.urlopen(dataURL2) as url2:
            data = json.load(url2) #loaded as dict
        
        artist = data.get("artist")
        artist = artist.get("name")
        
        return artist

    ################################################################################################################

    lst = []
    count = 0

    artist = getArtistName(artist,API_KEY)
    pages = getPageAmount(username,timeframe,API_KEY)

    
    for i in range(pages):
        i+=1
        strPages = str(i) #and back into string for the url
        pageData = getPageData(API_KEY,strPages)
        
        for i in range(50): #only recieves 50 tracks of data per request
            try:
                temp = pageData[i] #gets the data for "i" track. i goes from 1-50, then moves to next page using the first for loop
            except:
                pass

            tempArtist = temp.get("artist")
            tempArtist = tempArtist.get("name")
            tempAlbum = temp.get("name")
            tempPlays = temp.get("playcount")

            if count < 5:
                if artist == tempArtist:            
                    if int(tempPlays) == 1:
                        scrobbles = "scrobble"
                    else:
                        scrobbles = "scrobbles"

                    lst.append([tempAlbum,tempPlays,scrobbles])
                    count += 1
    return lst

def mostPlayedArtistsAlbumsOPTIMISED(username,artist,API_KEY):

    from operator import itemgetter
    from customModules import verifyInputModule
    import urllib.request
    import json

    URLartist = artist.replace(" ","+")

    def getAlbums(artist,API_KEY):

        dataURL2 = "https://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist="+URLartist+"&api_key="+API_KEY+"&format=json"
        with urllib.request.urlopen(dataURL2) as url2:
            data = json.load(url2) #loaded as dict
        
        data = data.get("topalbums")
        data = data.get("album")
        
        return data

    ################################################################################################################

    lst = []
    lst2 = []

    albums = getAlbums(artist,API_KEY)
 
    albumcount = len(albums)
    if len(albums) > 25:
        albumcount = 25


    for i in range(albumcount):
        try:
            temp = albums[i] #gets the data for "i" album
        except:
            pass

        tempArtist = temp.get("artist")
        tempArtist = tempArtist.get("name")
        tempAlbum = temp.get("name")

        tempArtist = tempArtist.replace(" ","+")
        tempAlbum = tempAlbum.replace(" ","+")

        tempArtist = verifyInputModule.parseForURL(tempArtist)
        tempAlbum = verifyInputModule.parseForURL(tempAlbum)

        lst.append([tempAlbum,tempArtist])

    for album in lst:
        dataURL2 = "https://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key="+API_KEY+"&artist="+URLartist+"&album="+album[0]+"&username="+username+"&format=json"
        try:
            with urllib.request.urlopen(dataURL2) as url2:
                data = json.load(url2) #loaded as dict

            data = data.get("album")
            tempAlbum = data.get("name")
            tempPlaycount = data.get("userplaycount")

            if int(tempPlaycount) == 1:
                scrobbles = "scrobble"
            else:
                scrobbles = "scrobbles"

            lst2.append([tempAlbum,int(tempPlaycount),scrobbles])
            
        except:
            continue
    
    lst2 = sorted(lst2, key=itemgetter(1), reverse=True)
    lst2 = lst2[:5] 
    return lst2
