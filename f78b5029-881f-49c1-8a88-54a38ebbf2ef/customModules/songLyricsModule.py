def getLyrics(GENIUS_API_KEY,artist,song):
    import lyricsgenius, json, os, sys

    def blockPrint():
        sys.stdout = open(os.devnull, 'w')
    def enablePrint():
        sys.stdout = sys.__stdout__

    blockPrint()
    genius = lyricsgenius.Genius(GENIUS_API_KEY)
    lyrics = genius.search_song(song, artist)
    try:
        lyrics.save_lyrics("lyrics.json")
    except:
        pass
    enablePrint()

    with open("lyrics.json") as json_file:
        data = json.load(json_file)
        data = data.get("lyrics")

    os.remove("lyrics.json")

    if lyrics == None:
        raise Exception
    else:
        if len(data) < 1950:
            return [data,"below1950"]
        else:
            count = 0
            temp = "PLACEHOLDER"
            final = []
            while temp != "":
                temp = data[count:count+1950]
                final.append(temp)
                count += 1950
            final.pop()
            return [final,"above1950"]
                