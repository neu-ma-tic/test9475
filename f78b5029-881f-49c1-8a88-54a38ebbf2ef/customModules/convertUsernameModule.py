def convert(username,API_KEY):
    
    import urllib.request,json
    def getUsername(username,API_KEY):
        dataURL2 = "http://ws.audioscrobbler.com/2.0/?method=user.getInfo&user="+username+"&api_key="+API_KEY+"&format=json"
        with urllib.request.urlopen(dataURL2) as url2:
            data = json.load(url2) #loaded as dict 
        name = data.get("user")
        name = name.get("name")
        return name

    tempusername = username[len("<@"):-len(">")]

    if tempusername.startswith("!") == True:
        tempusername = tempusername+">"
        tempusername = username[len("<@!"):-len(">")]

    tempusername = str(tempusername)

    if tempusername.isnumeric() == False: #discord id's are numeric, if not numeric then return original username
        username = getUsername(username,API_KEY)
        return username
    else:     
        file = open("register.txt","r")
        userlist = file.readlines()
        file.close()

        for entry in userlist:
            entry2 = entry.split(":")
            if entry2[0] == tempusername:
                username = entry2[1]
                username = username.strip('\n')
                username = getUsername(username,API_KEY)
                return username
            else:
                pass