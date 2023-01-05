import discord, datetime, time
from customModules import(
                        verifyInputModule, mostPlayedTracksModule, collageMakerModule, getArtistPosModule,
                        getScrobblesModule, getFavSongModule, timePlayedModule, registerModule, convertUsernameModule, getArtistScrobblesModule,
                        mostPlayedAlbumsModule, songLyricsModule, helpModule
                        )  

def opencfg(filename):
    file = open(filename,"r")
    keys = file.readlines()
    
    keyList = []
    for entry in keys:
        tempEntry = entry.split("=")
        tempEntry = tempEntry[1]
        tempEntry = tempEntry.replace(" ","")
        tempEntry = tempEntry.strip()
        keyList.append(tempEntry)
    return keyList
keyList = opencfg("apikeys.txt")
API_KEY, discordKey, testDiscordKey, GENIUS_API_KEY = str(keyList[0]), str(keyList[1]), str(keyList[2]), str(keyList[3])

client = discord.Client()
@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))
    
@client.event
async def on_message(message):
    usermessage = message.content.lower()
    avatar = str(message.author.avatar_url)
    avatar = avatar.replace("webp?size=1024","png?size=32")
    discordname = str(message.author.name)+"#"+str(message.author.discriminator)

    # -----------------------------------------------------------   
    #                        Help Commands
    # -----------------------------------------------------------
	
    if usermessage.startswith("$help"):
        helpMessage = helpModule.help(usermessage)
        try:
            title, description, colour = helpMessage.title, helpMessage.description, helpMessage.colour
        except:
            return
            
        embed = discord.Embed(title=title,description=description,color=colour)
        embed.set_author(name=discordname, icon_url=avatar)
        await message.channel.send(embed=embed)
			
    # -----------------------------------------------------------
    #                          Collage
    # -----------------------------------------------------------

    elif message.content.startswith("$collage"):
        usermessage = usermessage.split(" ")
        try:
            if len(usermessage) != 3 and len(usermessage) != 5:
                embed = discord.Embed(title='<:O_O:617420634854653963> parameters have been entered incorrectly',colour=0xff0000)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
            else:
                try:
                    username, timeframe, size, toggleAlbumData = str(usermessage[1]), str(usermessage[2]), int(usermessage[3]), str(usermessage[4])
                except:
                    username, timeframe, size, toggleAlbumData = str(usermessage[1]), str(usermessage[2]), 5, "true"

                username = convertUsernameModule.convert(username,API_KEY)

                embed = discord.Embed(title="creating collage for: " + username, colour=1)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)

                collageMakerModule.collageMaker(username,timeframe,size,toggleAlbumData,API_KEY)
                await message.channel.send(file=discord.File("collage.png"))
                print("success - collage")
        except:
            embed = discord.Embed(title='<:O_O:617420634854653963>  error occured',colour=0xff0000)
            embed.set_author(name=discordname, icon_url=avatar)
            await message.channel.send(embed=embed)
			
    # -----------------------------------------------------------
    #                        Time Played
    # -----------------------------------------------------------

    elif message.content.startswith("$timeplayed"):
        usermessage = usermessage.split(" ")
        try:
            if len(usermessage) != 3:
                embed = discord.Embed(title='<:O_O:617420634854653963> parameters have been entered incorrectly',colour=0xff0000)
                await message.channel.send(embed=embed)
            else:
                username, timeframe = str(usermessage[1]), str(usermessage[2])
                username = convertUsernameModule.convert(username,API_KEY)

                embed = discord.Embed(title="calculating total time played for: "+username, colour=1)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)

                userTotalTime = timePlayedModule.timePlayed(username,timeframe,API_KEY)

                if timeframe == "7day":
                    percentage = round(((userTotalTime[0]/604800)*100),2)
                    timeframe = "7 days"
                elif timeframe == "1month":
                    percentage = round(((userTotalTime[0]/2629746)*100),2)
                    timeframe = "a month"
                elif timeframe == "3month":
                    percentage = round(((userTotalTime[0]/7889238) * 100), 2)
                    timeframe = "3 months"
                elif timeframe == "6month":
                    percentage = round(((userTotalTime[0]/15778476) * 100), 2)
                    timeframe = "6 months"
                elif timeframe == "12month":
                    percentage = round(((userTotalTime[0]/31556952) * 100), 2)
                    timeframe = "a year"
                else:
                    timeframe = "the time passed since your account was created"
                    percentage = round(((userTotalTime[0]/int(userTotalTime[1])) * 100), 2)
                
                userTotalTime[0] = str(datetime.timedelta(seconds=userTotalTime[0]))
                embed = discord.Embed(title=username+"'s total time played is: " + str(userTotalTime[0]), description="which is " + str(percentage) + "% of " + str(timeframe), colour=0x4BB543)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
                print("success - timeplayed")
        except:
            embed = discord.Embed(title='<:O_O:617420634854653963>  error occured',colour=0xff0000)
            embed.set_author(name=discordname, icon_url=avatar)
            await message.channel.send(embed=embed)

    # -----------------------------------------------------------
    #                        Scrobbles
    # -----------------------------------------------------------

    elif message.content.startswith("$scrobbles"):
        usermessage = usermessage.split(" ")
        try:
            if len(usermessage) == 2:
                username = str(usermessage[1])
                username = convertUsernameModule.convert(username,API_KEY)
                userTotalScrobbles = getScrobblesModule.getScrobbles(username,API_KEY)

                embed = discord.Embed(title= username + "'s scrobble count is: " + str(userTotalScrobbles) , colour=0x4BB543)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
                print("success - scrobbles")

            elif len(usermessage) == 3:
                username = str(usermessage[1])
                username = convertUsernameModule.convert(username,API_KEY)
                artist = str(usermessage[2])
                artist = artist.replace("_","+")
                artist = verifyInputModule.parseForURL(artist)
                userTotalScrobbles = getArtistScrobblesModule.getArtistScrobbles(username,artist,API_KEY)
                if userTotalScrobbles[0] != "0":
                    embed = discord.Embed(title= username + " has scrobbled " + userTotalScrobbles[1] + " " + str(userTotalScrobbles[0]) + " times", colour=0x4BB543)
                else:
                    embed = discord.Embed(title= username + " doesn't stan " + userTotalScrobbles[1], colour=0x4BB543)

                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
            
            else:
                embed = discord.Embed(title='<:O_O:617420634854653963> parameters have been entered incorrectly',colour=0xff0000)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)

        except:
            embed = discord.Embed(title='<:O_O:617420634854653963>  error occured',colour=0xff0000)
            embed.set_author(name=discordname, icon_url=avatar)
            await message.channel.send(embed=embed)
			
    # -----------------------------------------------------------
    #                           FavSong
    # -----------------------------------------------------------

    elif message.content.startswith("$favsong"):
        usermessage = usermessage.split(" ")
        try:
            if len(usermessage) != 2:
                embed = discord.Embed(title='<:O_O:617420634854653963> parameters have been entered incorrectly',colour=0xff0000)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
            else:
                username = str(usermessage[1])
                username = convertUsernameModule.convert(username,API_KEY)
                favSong = getFavSongModule.getFavSong(username,API_KEY)
                
                embed = discord.Embed(title=username + "'s favourite song is: " + str(favSong),colour=0x4BB543)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
                print("success - favsong")
        except:
            embed = discord.Embed(title='<:O_O:617420634854653963>  error occured',colour=0xff0000)
            embed.set_author(name=discordname, icon_url=avatar)
            await message.channel.send(embed=embed)

    # -----------------------------------------------------------
    #                        ArtistPos
    # -----------------------------------------------------------

    elif message.content.startswith("$artistpos"):
        usermessage = usermessage.split(" ")
        try:
            if len(usermessage) != 4:
                embed = discord.Embed(title='<:O_O:617420634854653963> parameters have been entered incorrectly',colour=0xff0000)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
            else:
                username = str(usermessage[1])
                username = convertUsernameModule.convert(username,API_KEY)
                artist = str(usermessage[2])
                timeframe = str(usermessage[3])

                artist = verifyInputModule.parseForURL(artist)
                displayArtist = verifyInputModule.getArtistName(artist,API_KEY)
                
                embed = discord.Embed(title = "searching for " +str(displayArtist) + " in "+username+"'s library",colour=1)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)

                artistPos = getArtistPosModule.findArtistPos(username,timeframe,artist,API_KEY)

                if artistPos != None:
                    embed = discord.Embed(title = str(displayArtist) + " is "+username+"'s " + str(artistPos) + " most played artist",colour=0x4BB543)
                    embed.set_author(name=discordname, icon_url=avatar)
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(title = username + " doesn't stan " + displayArtist ,colour=0x4BB543)
                    embed.set_author(name=discordname, icon_url=avatar)
                    await message.channel.send(embed=embed)
                print("success - artistpos")
        except:
            embed = discord.Embed(title='<:O_O:617420634854653963>  error occured',colour=0xff0000)
            embed.set_author(name=discordname, icon_url=avatar)
            await message.channel.send(embed=embed)

    # -----------------------------------------------------------
    #                          Register
    # -----------------------------------------------------------

    elif message.content.startswith("$register"):
        usermessage = usermessage.split(" ")
        try:
            if len(usermessage) != 2:
                embed = discord.Embed(title='<:O_O:617420634854653963> parameters have been entered incorrectly',colour=0xff0000)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
            else:
                username = usermessage[1]
                newEntry = str(message.author.id)+":"+str(username)
                registerModule.register(newEntry)
                embed = discord.Embed(title = "successfully been registered as: "+str(username),colour=0x4BB543)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
                print("success - register")
        except:
            embed = discord.Embed(title='<:O_O:617420634854653963>  error occured',colour=0xff0000)
            embed.set_author(name=discordname, icon_url=avatar)
            await message.channel.send(embed=embed)

    # -----------------------------------------------------------
    #                    Most Played Albums
    # -----------------------------------------------------------
        
    elif message.content.startswith("$topalbums"):
        usermessage = usermessage.split(" ")
        try:
            if len(usermessage) != 4:
                embed = discord.Embed(title='<:O_O:617420634854653963> parameters have been entered incorrectly',colour=0xff0000)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
            else:
                username,timeframe,artist = usermessage[1],usermessage[2],usermessage[3]
                username = convertUsernameModule.convert(username,API_KEY)
                artist = verifyInputModule.parseForURL(artist)
                artist = verifyInputModule.getArtistName(artist,API_KEY)
                
                embed = discord.Embed(title = "finding top albums for: " +str(username),colour=1)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)

                if timeframe in set(["7day","1month","3month","6month","12month"]):
                    lst = mostPlayedAlbumsModule.mostPlayedArtistsAlbums(username,timeframe,artist,API_KEY)
                else:
                    lst = mostPlayedAlbumsModule.mostPlayedArtistsAlbumsOPTIMISED(username,artist,API_KEY)

                description = ""
                for item in lst:
                    item = str(item[0]) + " - " + str(item[1]) + " " + str(item[2])
                    description += item+"\n" 
                
                embed = discord.Embed(title = str(username)+"'s most played albums from: "+artist, description=description, colour=0x4BB543)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
                print("success - topalbums")
        except:
            embed = discord.Embed(title='<:O_O:617420634854653963>  error occured',colour=0xff0000)
            embed.set_author(name=discordname, icon_url=avatar)
            await message.channel.send(embed=embed)

    # -----------------------------------------------------------
    #                    Most Played Tracks
    # -----------------------------------------------------------
        
    elif message.content.startswith("$toptracks"):
        usermessage = usermessage.split(" ")
        try:
            if len(usermessage) != 4:
                embed = discord.Embed(title='<:O_O:617420634854653963> parameters have been entered incorrectly',colour=0xff0000)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
            else:
                username,timeframe,artist = usermessage[1],usermessage[2],usermessage[3]
                username = convertUsernameModule.convert(username,API_KEY)
                artist = verifyInputModule.parseForURL(artist)
                artist = verifyInputModule.getArtistName(artist,API_KEY)
                
                embed = discord.Embed(title = "finding top tracks for: " +str(username),colour=1)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)

                lst = mostPlayedTracksModule.mostPlayedArtistSongs(username,timeframe,artist,API_KEY)

                description = ""
                for item in lst:
                    description += item+"\n" 
                
                embed = discord.Embed(title = str(username)+"'s most played tracks from: "+artist, description=description, colour=0x4BB543)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
                print("success - toptracks")
        except:
            embed = discord.Embed(title='<:O_O:617420634854653963>  error occured',colour=0xff0000)
            embed.set_author(name=discordname, icon_url=avatar)
            await message.channel.send(embed=embed)

    # -----------------------------------------------------------
    #                    Get Song Lyrics
    # -----------------------------------------------------------

    elif message.content.startswith("$lyrics"):
        usermessage = usermessage.split(" ")
        try:
            if len(usermessage) != 3:
                embed = discord.Embed(title='<:O_O:617420634854653963> parameters have been entered incorrectly',colour=0xff0000)
                embed.set_author(name=discordname, icon_url=avatar)
                await message.channel.send(embed=embed)
            else:
                artist, songname = str(usermessage[1]), str(usermessage[2])
                artist, songname = artist.replace("_"," ") , songname.replace("_"," ")

                outputLyrics = songLyricsModule.getLyrics(GENIUS_API_KEY,artist,songname)   
                charCount = outputLyrics[1]
                outputLyrics = outputLyrics[0]
                print(outputLyrics)

                if charCount == "below1950":
                    embed = discord.Embed(title='lyrics for: "'+songname+'"', description=outputLyrics, colour=0x4BB543)
                    embed.set_author(name=discordname, icon_url=avatar)
                    await message.channel.send(embed=embed)
                else:
                    count = 0
                    for msg in outputLyrics:
                        print(msg)
                        count += 1
                        if count == 1:
                            embed = discord.Embed(title='lyrics for: "'+artist+" - "+songname+'"', description=msg, colour=0x4BB543)
                            embed.set_author(name=discordname, icon_url=avatar)
                            await message.channel.send(embed=embed)
                        else:
                            embed = discord.Embed(description=msg, colour=0x4BB543)
                            await message.channel.send(embed=embed)                            


        except Exception as e:
            print(e)
            embed = discord.Embed(title='<:O_O:617420634854653963>  error occured',description=e,colour=0xff0000)
            embed.set_author(name=discordname, icon_url=avatar)
            await message.channel.send(embed=embed)

    # -----------------------------------------------------------
    #                        Mike2 Garbage
    # -----------------------------------------------------------

	# $poopy
    elif message.content.startswith("$poopy"):
        embed = discord.Embed(title = "<:poopy:590926727900037153>", colour=0x7A5901)
        await message.channel.send(embed=embed)
	# $bigpoopy
    elif message.content.startswith("$bigpoopy"):
        await message.channel.send("<:poopy:590926727900037153>")
	# $BIGMASSIVEDUMP
    elif message.content.startswith("$BIGMASSIVEDUMP"):
        await message.channel.send(file=discord.File("poop.png"))
    elif "<@!617383576916197386>" in message.content: # Bot name mentioned
        await message.channel.send("<:poopy:590926727900037153>")

client.run(testDiscordKey)
