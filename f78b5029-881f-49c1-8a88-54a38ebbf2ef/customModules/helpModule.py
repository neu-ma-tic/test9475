class createHelpMessage:
    def __init__(self, title, description, colour):
        self.title = title
        self.description = description
        self.colour = colour

def help(usermessage):
    if usermessage.startswith("$help collage"):
        if usermessage.endswith("username"):
            helpMessage = createHelpMessage("your last.fm username","example: SHKTV",1)
            
        elif usermessage.endswith("timeframe"):
            helpMessage = createHelpMessage("time period in which data should be fetched","accepted values: overall, 7day, 1month, 3month, 6month, 12month",1)
            
        elif usermessage.endswith("size"):
            helpMessage = createHelpMessage("size of the collage in images wide/tall","accepted values: 1,2,3,4,5,6,7",1)
            
        elif usermessage.endswith("togglealbumdata"):
            helpMessage = createHelpMessage("enable printing of album names and playcount","accepted values: True, False",1)
        
        else:
            helpMessage = createHelpMessage("usage: $collage username timeframe","optionally: $collage username timeframe size toggleAlbumData", 1)
            
                            
    # ----------------------------------------------------------
    #                      Time Played Help
    # ----------------------------------------------------------

    elif usermessage.startswith("$help timeplayed"):
        if usermessage.endswith("username"):
            helpMessage = createHelpMessage("your last.fm username","example: SHKTV",1)
            
        elif usermessage.endswith("timeframe"):
            helpMessage = createHelpMessage("time period in which data should be fetched","accepted values: overall, 7day, 1month, 3month, 6month, 12month",1)
            
        else:
            helpMessage = createHelpMessage("$timeplayed username timeframe","sample response: `SHKTV's total time played is: 20:30:01, which is 12.2% of 7 days`",1)
                                    
    # ----------------------------------------------------------
    #                      Scrobbles Help
    # ----------------------------------------------------------

    elif usermessage.startswith("$help scrobbles"):
        if usermessage.endswith("username"):
            helpMessage = createHelpMessage("your last.fm username","example: SHKTV",1)
            
        elif usermessage.endswith("artist"):
            helpMessage = createHelpMessage("any artist on last.fm","examples: EDEN, James_Blake, Blood_Orange",1)
            
        else:
            helpMessage = createHelpMessage("usage: $scrobbles username","alternatively: $scrobbles username artist",1)
                                
    # ----------------------------------------------------------
    #                      Fav Song Help
    # ----------------------------------------------------------

    elif usermessage.startswith("$help favsong"):
        if usermessage.endswith("username"):
            helpMessage = createHelpMessage("your last.fm username","example: SHKTV",1)
            
        else:
            helpMessage = createHelpMessage("usage: $favsong username","sample response: `SHKTV's favourite song is: Eden - projector`",1)       
                            
    # ----------------------------------------------------------
    #                      Artist Pos Help
    # ----------------------------------------------------------

    elif usermessage.startswith("$help artistpos"):
        if usermessage.endswith("username"):
            helpMessage = createHelpMessage("your last.fm username","example: SHKTV",1)
                
        elif usermessage.endswith("timeframe"):
            helpMessage = createHelpMessage("time period in which data should be fetched","accepted values: overall, 7day, 1month, 3month, 6month, 12month",1)
            
        elif usermessage.endswith("artist"):
            helpMessage = createHelpMessage("any artist on last.fm","examples: EDEN, James_Blake, Blood_Orange",1)
                        
        else:
            helpMessage = createHelpMessage("$artistpos username artist timeframe","sample response: `Blood Orange is SHKTV's 13th most played artist`",1)
                            
    # ----------------------------------------------------------
    #                      Register Help
    # ----------------------------------------------------------

    elif usermessage.startswith("$help register"):
        if usermessage.endswith("username"):
            helpMessage = createHelpMessage("your last.fm username","example: SHKTV",1)
                
        else:
            helpMessage = createHelpMessage("usage: $register username","usage: used to link discord to lastfm `i.e. $collage @sarim overall`",1)

    # ----------------------------------------------------------
    #                      Most Played Albums Help
    # ----------------------------------------------------------

    elif usermessage.startswith("$help topalbums"):
        if usermessage.endswith("username"):
            helpMessage = createHelpMessage("your last.fm username","example: SHKTV",1)

        elif usermessage.endswith("timeframe"):
            helpMessage = createHelpMessage("time period in which data should be fetched","accepted values: overall, 7day, 1month, 3month, 6month, 12month",1)
            
        elif usermessage.endswith("artist"):
            helpMessage = createHelpMessage("any artist on last.fm","examples: EDEN, James_Blake, Blood_Orange",1)
                                        
        else:
            helpMessage = createHelpMessage("usage: $topalbums username timeframe artist","used to show a users most played albums from an artist",1)

    # ----------------------------------------------------------
    #                      Most Played Tracks Help
    # ----------------------------------------------------------
    
    elif usermessage.startswith("$help toptracks"):
        if usermessage.endswith("username"):
            helpMessage = createHelpMessage("your last.fm username","example: SHKTV",1)
            
        elif usermessage.endswith("timeframe"):
            helpMessage = createHelpMessage("time period in which data should be fetched","accepted values: overall, 7day, 1month, 3month, 6month, 12month",1)
            
        elif usermessage.endswith("artist"):
            helpMessage = createHelpMessage("any artist on last.fm","examples: EDEN, James_Blake, Blood_Orange",1)

        else:
            helpMessage = createHelpMessage("usage: $toptracks username timeframe artist", "used to show a users most played tracks from an artists", 1)
    
    # ----------------------------------------------------------
    #                      Lyrics Help
    # ----------------------------------------------------------

    elif usermessage.startswith("$help lyrics"):
        if usermessage.endswith("song"):
            helpMessage = createHelpMessage("the name of your chosen song","example: about_time",1)
            
        elif usermessage.endswith("artist"):
            helpMessage = createHelpMessage("the name of your chosen artist","examples: blood_orange, st._vincent",1)
            
        else:
            helpMessage = createHelpMessage("$lyrics artist song","sample responses: `will return lyrics in a single embed, or multiple if lyrics are too long.`",1)

    elif usermessage == "$help":
        helpMessage = createHelpMessage("music commands:","$collage\n$timeplayed\n$scrobbles\n$favsong\n$artistpos\n$topalbums\n$toptracks\n$lyrics\n$register",1)

    else:
        return

    return helpMessage
