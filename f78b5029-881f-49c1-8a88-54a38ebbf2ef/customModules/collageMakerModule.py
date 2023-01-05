def collageMaker(username,timeframe,size,toggleAlbumData,API_KEY):

    import glob
    import urllib.request
    import json
    import os
    import datetime
    from PIL import Image, ImageDraw, ImageFont

    def deleteTempFiles():
        filelist=glob.glob("*.jpg")
        for file in filelist:
            os.remove(file)
        filelist=glob.glob("*.gif")
        for file in filelist:
            os.remove(file)
        #txt
        try:
            os.remove("album.txt")
        except:
            pass

    def getPageData(API_KEY): #gets all data within a page
        dataURL = "http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user="+username+"&api_key="+API_KEY+"&period="+timeframe+"&format=json"
        with urllib.request.urlopen(dataURL) as url:
            pageData = json.load(url) #loaded as dict
        
        pageData = pageData.get("topalbums") #condenses json to important information
        pageData = pageData.get("album") # condenses json to important information
        return pageData

    def downloadImages():
        for i in range(totalsize):
            
            temp = pageData[i] #gets the data for "i" album

            imageurl = temp.get("image")
            imageurl = imageurl[3] #moves to extralarge image
            imageurl = imageurl.get("#text") #image link is saved under #text

            if imageurl.endswith(".gif"):
                filename = str(i)+".gif"
            else:
                filename = str(i)+".jpg"
                
            try:
                urllib.request.urlretrieve(imageurl,filename)
            except:
                placeholder.save(filename, "JPEG")

    def getAlbumInfo():
        lst = []
        for i in range(totalsize):
            temp = pageData[i]
            playcount = temp.get("playcount")
            albumname = temp.get("name")
            try:
                lst.append(albumname+"|"+playcount+"\n")
            except:
                lst.append(" |"+playcount+"\n")

        return lst

    totalsize, canvaslength = size*size, 300*size                
    placeholder = Image.new('RGB', (300,300)) #creates blank image incase no album art
    canvas = Image.new('RGB', (canvaslength,canvaslength))
    coordinate = (0,0,300,300)
    count = 0
    
    deleteTempFiles()
    pageData = getPageData(API_KEY)
    downloadImages()
    album = getAlbumInfo()

    for y in range(size):
        if y > 0:
            coordinatelist = list(coordinate)
            coordinatelist[0] = 0
            coordinatelist[1] += 300
            coordinatelist[2] = 300
            coordinatelist[3] += 300     
            coordinate = tuple(coordinatelist)
            
        for _ in range(size): #unused variable, therefore replaced "x" with "_"
            filename = str(count)+".jpg"
            filename2 = str(count)+".gif"
            try:
                cover = Image.open(filename)
            except:
                Image.open(filename2).convert('RGB').save(filename)
                cover = Image.open(filename)
            
            if toggleAlbumData == "true":
                currentalbum = album[count]
                currentalbum = currentalbum.split("|")
                currentalbumname = currentalbum[0]
                currentalbumplays = currentalbum[1]
                
                pixelcoord = 5,5
                covercolour = cover.getpixel(pixelcoord)
                pixelcoord = 5,25
                covercolour2 = cover.getpixel(pixelcoord)
                
                colour1 = covercolour[0] + covercolour[1] + covercolour[2]
                colour2 = covercolour2[0] + covercolour2[1] + covercolour2[2]
                finalcolour = (colour1+colour2)/6

                try:
                    if finalcolour >= 127.5:
                        fontcolour = 0,0,0,255
                    else:
                        fontcolour = 255,255,255,255
                except:
                    fontcolour = 0,0,0,255 # default colour
                
                font = ImageFont.truetype("arial.ttf", 20)
                draw = ImageDraw.Draw(cover)
                draw.text((5,5), currentalbumname, font=font, fill=(fontcolour))
                draw.text((5,25), currentalbumplays, font=font, fill=(fontcolour))
            
            canvas.paste(cover,coordinate)
            
            coordinatelist = list(coordinate)
            coordinatelist[0] += 300
            coordinatelist[2] += 300
            coordinate = tuple(coordinatelist)
            
            count += 1
            
            cover.close()
        
    deleteTempFiles()
    
    canvas.save("collage.png","PNG")  
    canvas.close()
