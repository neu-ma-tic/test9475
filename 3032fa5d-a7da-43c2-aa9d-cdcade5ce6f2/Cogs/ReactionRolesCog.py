import discord
from discord.ext import commands

class ReactRolesCog(commands.Cog):
    def __init__(Self, Bot):
        Self.Bot = Bot

        Self.Sel1  = '1️⃣'
        Self.Sel2  = '2️⃣'
        Self.Sel3  = '3️⃣'
        Self.Sel4  = '4️⃣'
        Self.Sel5  = '5️⃣'
        Self.Sel6  = '6️⃣'
        Self.Sel7  = '7️⃣'
        Self.Sel8  = '8️⃣'
        Self.Sel9  = '9️⃣'
        Self.Sel10 = '🔟'
        Self.Sel11 = '🇦'
        Self.Sel12 = '🇧'
        Self.Sel13 = '🟪'
        Self.Sel14 = '🟩'
        Self.Sel15 = '🟥'
        Self.Sel16 = '🟦'

        def SearchRoles( RoleToSearchFor ):
            Result = discord.utils.find(lambda r: r.name == RoleToSearchFor, 
                                        Bot.guilds[0].roles
                                        )
            return Result

        @Bot.event
        async def on_raw_reaction_add(Payload):

            with open( 'Data/CogData/PronounRolesMsgID.txt' ) as File:
                PronounRolesMessage = int(File.read())
            with open( 'Data/CogData/AgeRolesMsgID.txt' )     as File:
                AgeRolesMessage     = int(File.read())
            with open( 'Data/CogData/HobbieRolesMsgID.txt' )  as File:
                HobbieRolesMessage  = int(File.read())
            with open( 'Data/CogData/PingsRolesMsgID.txt' )   as File:
                PingsRolesMessage   = int(File.read())
            with open( 'Data/CogData/GamerRolesMsgID.txt' )   as File:
                GamerRolesMessage   = int(File.read())

            Member     = Payload.member
            MessageID  = Payload.message_id
            EmojiName  = Payload.emoji.name

            if Member.display_name == 'Sally':
                return

            if MessageID == PronounRolesMessage:
                if EmojiName == Self.Sel1:
                    await Member.add_roles(SearchRoles('He/Him'))
                if EmojiName == Self.Sel2:
                    await Member.add_roles(SearchRoles('She/Her'))
                if EmojiName == Self.Sel3:
                    await Member.add_roles(SearchRoles('They/Them'))
            if MessageID == AgeRolesMessage:
                if EmojiName == Self.Sel1:
                    await Member.add_roles(SearchRoles('18+'))
                if EmojiName == Self.Sel2:
                    await Member.add_roles(SearchRoles('17'))
                if EmojiName == Self.Sel3:
                    await Member.add_roles(SearchRoles('-16'))
            if MessageID == HobbieRolesMessage:
                if EmojiName == Self.Sel1:
                    await Member.add_roles(SearchRoles('Gamer'))
                if EmojiName == Self.Sel2:
                    await Member.add_roles(SearchRoles('Artist'))
                if EmojiName == Self.Sel3:
                    await Member.add_roles(SearchRoles('Streamer/YouTuber'))
            if MessageID == PingsRolesMessage:
                if EmojiName == Self.Sel1:
                    await Member.add_roles(SearchRoles('Movie Night'))        
                if EmojiName == Self.Sel2:
                    await Member.add_roles(SearchRoles('Game Night'))
                if EmojiName == Self.Sel3:
                    await Member.add_roles(SearchRoles('Announcements'))
                if EmojiName == Self.Sel4:
                    await Member.add_roles(SearchRoles('Listen Along'))
                if EmojiName == Self.Sel5:
                    await Member.add_roles(SearchRoles('Frag-fest'))
            if MessageID == GamerRolesMessage:
                if EmojiName == Self.Sel1:
                    await Member.add_roles(SearchRoles('Apex Legends'))
                if EmojiName == Self.Sel2:
                    await Member.add_roles(SearchRoles('Call of Duty'))
                if EmojiName == Self.Sel3:
                    await Member.add_roles(SearchRoles('CS:GO'))
                if EmojiName == Self.Sel4:
                    await Member.add_roles(SearchRoles('Super Smash Bros.'))
                if EmojiName == Self.Sel5:
                    await Member.add_roles(SearchRoles('Battlefront'))
                if EmojiName == Self.Sel6:
                    await Member.add_roles(SearchRoles('Battlefield'))
                if EmojiName == Self.Sel7:
                    await Member.add_roles(SearchRoles('Rocket League'))
                if EmojiName == Self.Sel8:
                    await Member.add_roles(SearchRoles('Rainbow Six Siege'))
                if EmojiName == Self.Sel9:
                    await Member.add_roles(SearchRoles('Minecraft'))
                if EmojiName == Self.Sel10:
                    await Member.add_roles(SearchRoles('League of Legends'))
                if EmojiName == Self.Sel11:
                    await Member.add_roles(SearchRoles('Fifa'))
                if EmojiName == Self.Sel12:
                    await Member.add_roles(SearchRoles('Madden'))
                if EmojiName == Self.Sel13:
                    await Member.add_roles(SearchRoles('PC'))
                if EmojiName == Self.Sel14:
                    await Member.add_roles(SearchRoles('XBox'))
                if EmojiName == Self.Sel15:
                    await Member.add_roles(SearchRoles('Nintendo Switch'))
                if EmojiName == Self.Sel16:
                    await Member.add_roles(SearchRoles('Playstation'))
        
        @Bot.event
        async def on_raw_reaction_remove(Payload):

            with open( 'Data/CogData/PronounRolesMsgID.txt' ) as File:
                PronounRolesMessage = int(File.read())
            with open( 'Data/CogData/AgeRolesMsgID.txt' )     as File:
                AgeRolesMessage     = int(File.read())
            with open( 'Data/CogData/HobbieRolesMsgID.txt' )  as File:
                HobbieRolesMessage  = int(File.read())
            with open( 'Data/CogData/PingsRolesMsgID.txt' )   as File:
                PingsRolesMessage   = int(File.read())
            with open( 'Data/CogData/GamerRolesMsgID.txt' )   as File:
                GamerRolesMessage   = int(File.read())

            Member     = discord.utils.find(lambda m: m.id == Payload.user_id, 
                                            Bot.guilds[0].members
                                            )
            MessageID  = Payload.message_id
            EmojiName  = Payload.emoji.name

            if MessageID == PronounRolesMessage:
                if EmojiName == Self.Sel1:
                    await Member.remove_roles(SearchRoles('He/Him'))
                if EmojiName == Self.Sel2:
                    await Member.remove_roles(SearchRoles('She/Her'))
                if EmojiName == Self.Sel3:
                    await Member.remove_roles(SearchRoles('They/Them'))
            if MessageID == AgeRolesMessage:
                if EmojiName == Self.Sel1:
                    await Member.remove_roles(SearchRoles('18+'))
                if EmojiName == Self.Sel2:
                    await Member.remove_roles(SearchRoles('17'))
                if EmojiName == Self.Sel3:
                    await Member.remove_roles(SearchRoles('-16'))
            if MessageID == HobbieRolesMessage:
                if EmojiName == Self.Sel1:
                    await Member.remove_roles(SearchRoles('Gamer'))
                if EmojiName == Self.Sel2:
                    await Member.remove_roles(SearchRoles('Artist'))
                if EmojiName == Self.Sel3:
                    await Member.remove_roles(SearchRoles('Streamer/YouTuber'))
            if MessageID == PingsRolesMessage:
                if EmojiName == Self.Sel1:
                    await Member.remove_roles(SearchRoles('Movie Night'))        
                if EmojiName == Self.Sel2:
                    await Member.remove_roles(SearchRoles('Game Night'))
                if EmojiName == Self.Sel3:
                    await Member.remove_roles(SearchRoles('Announcements'))
                if EmojiName == Self.Sel4:
                    await Member.remove_roles(SearchRoles('Listen Along'))
                if EmojiName == Self.Sel5:
                    await Member.remove_roles(SearchRoles('Frag-fest'))
            if MessageID == GamerRolesMessage:
                if EmojiName == Self.Sel1:
                    await Member.remove_roles(SearchRoles('Apex Legends'))
                if EmojiName == Self.Sel2:
                    await Member.remove_roles(SearchRoles('Call of Duty'))
                if EmojiName == Self.Sel3:
                    await Member.remove_roles(SearchRoles('CS:GO'))
                if EmojiName == Self.Sel4:
                    await Member.remove_roles(SearchRoles('Super Smash Bros.'))
                if EmojiName == Self.Sel5:
                    await Member.remove_roles(SearchRoles('Battlefront'))
                if EmojiName == Self.Sel6:
                    await Member.remove_roles(SearchRoles('Battlefield'))
                if EmojiName == Self.Sel7:
                    await Member.remove_roles(SearchRoles('Rocket League'))
                if EmojiName == Self.Sel8:
                    await Member.remove_roles(SearchRoles('Rainbow Six Siege'))
                if EmojiName == Self.Sel9:
                    await Member.remove_roles(SearchRoles('Minecraft'))
                if EmojiName == Self.Sel10:
                    await Member.remove_roles(SearchRoles('League of Legends'))
                if EmojiName == Self.Sel11:
                    await Member.remove_roles(SearchRoles('Fifa'))
                if EmojiName == Self.Sel12:
                    await Member.remove_roles(SearchRoles('Madden'))
                if EmojiName == Self.Sel13:
                    await Member.remove_roles(SearchRoles('PC'))
                if EmojiName == Self.Sel14:
                    await Member.remove_roles(SearchRoles('XBox'))
                if EmojiName == Self.Sel15:
                    await Member.remove_roles(SearchRoles('Nintendo Switch'))
                if EmojiName == Self.Sel16:
                    await Member.remove_roles(SearchRoles('Playstation'))            

    @commands.command()
    async def MakeRoleMenu( Self, Context ):
        RoleChannel = discord.utils.find(lambda c: c.id == 806787239316291634,
                                         Self.Bot.guilds[0].channels
                                         )

        with open('Data/CogData/PronounsRoleMenu.txt', encoding='UTF-8') as MenuText:
            Menu = await RoleChannel.send(MenuText.read())
        with open( 'Data/CogData/PronounRolesMsgID.txt', 'w' ) as File:
            File.write(str(Menu.id))

            await Menu.add_reaction(Self.Sel1)
            await Menu.add_reaction(Self.Sel2)
            await Menu.add_reaction(Self.Sel3)
        
        with open('Data/CogData/AgeRoleMenu.txt', encoding='UTF-8') as MenuText:
            Menu = await RoleChannel.send(MenuText.read())
        with open( 'Data/CogData/AgeRolesMsgID.txt', 'w' ) as File:
            File.write(str(Menu.id))

            await Menu.add_reaction(Self.Sel1)
            await Menu.add_reaction(Self.Sel2)
            await Menu.add_reaction(Self.Sel3)

        with open('Data/CogData/HobbiesRoleMenu.txt', encoding='UTF-8') as MenuText:
            Menu = await RoleChannel.send(MenuText.read())
        with open( 'Data/CogData/HobbieRolesMsgID.txt', 'w' ) as File:
            File.write(str(Menu.id))

            await Menu.add_reaction(Self.Sel1)
            await Menu.add_reaction(Self.Sel2)
            await Menu.add_reaction(Self.Sel3)

        with open('Data/CogData/PingsRoleMenu.txt', encoding='UTF-8') as MenuText:
            Menu = await RoleChannel.send(MenuText.read())
        with open( 'Data/CogData/PingsRolesMsgID.txt', 'w' ) as File:
            File.write(str(Menu.id))

            await Menu.add_reaction(Self.Sel1)
            await Menu.add_reaction(Self.Sel2)
            await Menu.add_reaction(Self.Sel3)
            await Menu.add_reaction(Self.Sel4)
            await Menu.add_reaction(Self.Sel5)

        with open('Data/CogData/GamerRoleMenu.txt', encoding='UTF-8') as MenuText:
            Menu = await RoleChannel.send(MenuText.read())
        with open( 'Data/CogData/GamerRolesMsgID.txt', 'w' ) as File:
            File.write(str(Menu.id))

            await Menu.add_reaction(Self.Sel1)
            await Menu.add_reaction(Self.Sel2)
            await Menu.add_reaction(Self.Sel3)
            await Menu.add_reaction(Self.Sel4)
            await Menu.add_reaction(Self.Sel5)
            await Menu.add_reaction(Self.Sel6)
            await Menu.add_reaction(Self.Sel7)
            await Menu.add_reaction(Self.Sel8)
            await Menu.add_reaction(Self.Sel9)
            await Menu.add_reaction(Self.Sel10)
            await Menu.add_reaction(Self.Sel11)
            await Menu.add_reaction(Self.Sel12)
            await Menu.add_reaction(Self.Sel13)
            await Menu.add_reaction(Self.Sel14)
            await Menu.add_reaction(Self.Sel15)
            await Menu.add_reaction(Self.Sel16)