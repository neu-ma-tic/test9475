def timePlayed(username,timeframe,API_KEY):
    
    import glob
    import urllib.request
    import json
    import os
    import time

    totalDuration = 0
    
    def getPageAmount(API_KEY): #gets the total amount of pages for the user
        dataURL = "http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user="+username+"&api_key="+API_KEY+"&period="+timeframe+"&format=json"
        
        with urllib.request.urlopen(dataURL) as url:
            data = json.load(url) #loaded as dict
            
        data = data.get("toptracks") #condenses json to important information                   
        pages = data.get("@attr") #condenses json to attributes only (includes amount of pages) 
        pages = pages.get("totalPages") #loads amount of pages                                  
        pages = int(pages) #turns amount of pages into int
        
        pages += 1
        
        return pages

    def getPageData(API_KEY): #gets all data within a page
        dataURL2 = "http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user="+username+"&api_key="+API_KEY+"&page="+strPages+"&period="+timeframe+"&format=json"

        with urllib.request.urlopen(dataURL2) as url2:
            data2 = json.load(url2) #loaded as dict
        
        data2 = data2.get("toptracks") #condenses json to important information
        data2 = data2.get("track") # condenses json to important information
        return data2

    def getUserSignUpTime(API_KEY):
        dataURL3 = "http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user="+username+"&api_key="+API_KEY+"&format=json"

        with urllib.request.urlopen(dataURL3) as url3:
            data3 = json.load(url3) #loaded as dict
        
        data3 = data3.get("user")
        data3 = data3.get("registered")
        data3 = data3.get("unixtime")
        return data3

    pages = getPageAmount(API_KEY)
    
    timeSince = int(getUserSignUpTime(API_KEY))
    timeSince = int(time.time()) - timeSince

    try:
        for i in range(1,pages):

            #print("page",i,"out of",pages-1) #DEBUG COMMAND
            strPages = str(i) #and back into string for the url
            pageData = getPageData(API_KEY)
            
            for i in range(50): #only recieves 50 tracks of data per request

                temp = pageData[i] #gets the data for "i" track. i goes from 1-50, then moves to next page using the first for loop

                tempDuration = temp.get("duration") #gets the duration for "i" track
                tempPlayCount = temp.get("playcount") #gets the playcount for "i" track

                tempDuration = int(tempDuration)   # self explanatory
                tempPlayCount = int(tempPlayCount) # self explanatory

                duration = tempDuration*tempPlayCount   
                totalDuration += duration #adds current song total duration to count

        lst = [int(totalDuration),timeSince]
        return lst
    except:
        lst = [int(totalDuration),timeSince]
        return lst
