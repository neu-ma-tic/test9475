def register(newEntry):
    newuserlist = []
    newuserlist.append(newEntry)                              #writes [userid:username] to new array

    file = open("register.txt","w") #creates file if doesnt exist
    file.close()

    file = open("register.txt","r")
    userlist = file.readlines()
    file.close()                      #reads file

    newEntry = newEntry.split(":")
    for entry in userlist:
        entry2 = entry.split(":")
        if entry2[0] != newEntry[0]:
            if entry != "\n":
                newuserlist.append(str(entry))
        else:
            pass                                #checks for duplicates, saves non duplicates to array

    file = open("register.txt","w")
    for entry in newuserlist:
        file.write(str(entry)+"\n")
    file.close()                                #saves non duplicates to file
