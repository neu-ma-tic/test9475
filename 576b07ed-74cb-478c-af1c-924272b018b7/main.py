import random, os
import discord
from discord.ext import tasks
from keep_alive import keep_alive
from globals import client, rythm2, command_prefix, description, my_token, hello, not_sanyi_text, commands_text, dev_id, dev_guild_id, berencek_id, uptime_channel_id
from commons import local_time, find_member
from database_controller import add_birthday, get_birthdays, is_it_time, greet_user, delete_birthday, get_default_channel, get_default_channels, update_default_channel, reset_greetings, log_command
from database_model import Birthday
from random import randrange
from datetime import timedelta

global apriltwenty
apriltwenty = True


@client.event
async def on_ready():
    # os.system("python3 -m pip install -U discord.py[voice]")
    reinstall_voice.start()
    called_on_time.start()
    # time_to_squat.start()
    channel = client.get_channel(uptime_channel_id)
    await channel.send('Logged in at ' +
                       local_time().strftime("%Y %b %d, %H:%M:%S"))
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="!kenobi_help"))
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith(command_prefix + 'embed'):
        log_command(message)
        embed = discord.Embed(title="General Kenobi",
                              description=description,
                              url="https://youtu.be/dmQDVHjTveI",
                              color=0x00ff00)
        #creates embed
        embed.set_image(url=hello)
        await message.channel.send(embed=embed)

    elif message.content.startswith(command_prefix + 'song'):
        log_command(message)
        videoId = "dmQDVHjTveI"
        song = "https://youtu.be/" + videoId
        await message.channel.send(song)

    elif message.content.startswith(command_prefix + 'fuckoff'):
        log_command(message)
        if dev_id != message.author.id:
            await message.channel.send(not_sanyi_text)
            return
        videoId = "WZjENfDvNsE"
        song = "https://youtu.be/" + videoId
        await message.channel.send(song)

    elif message.content.startswith(command_prefix + 'forbidden'):
        log_command(message)
        if dev_id != message.author.id:
            await message.channel.send(not_sanyi_text)
            return
        await message.channel.send("All hail the Gugyus")

    elif message.content.startswith(command_prefix + 'kenobi_help'):
        log_command(message)
        await message.channel.send(commands_text)

    elif message.content.startswith(command_prefix + 'hello'):
        log_command(message)
        filename = 'images/dc26484243124b4f42647f3eff67f637.gif'
        await message.channel.send(file=discord.File(filename))

    elif message.content.startswith(command_prefix + 'coinflip'):
        log_command(message)
        yes = 'images/32c950f36a61ec7e5060f5eee9140396.gif'
        no = 'images/efe75f294292b65bd21e32541d298994.gif'
        filename = random.choice([yes, no])
        await message.channel.send(file=discord.File(filename))

    elif message.content.startswith(command_prefix + 'delbd'):
        log_command(message)
        msg = message.content.split(command_prefix + 'delbd', 1)[1].strip()
        if len(msg) == 0:
            await message.channel.send(command_prefix + 'delbd Username#tag')
            return
        msg = msg.split()
        if len(msg) != 1 or msg[0].count('#') != 1:
            await message.channel.send("Please use the following format:\n" +
                                       command_prefix + 'delbd Username#tag')
            return
        user = msg[0].split("#", 1)
        username, tag = user[0], user[1]
        member = find_member(username, tag, message.guild)
        if member == None:
            await message.channel.send("User not found.")
            return

        if delete_birthday(member.id, message.guild.id):
            await message.channel.send("tirlás")
        else:
            await message.channel.send("User wasn't signed up.")

    # adds new birthday to greetings
    elif message.content.startswith(command_prefix + 'newbd'):
        log_command(message)
        msg = message.content.split(command_prefix + 'newbd', 1)[1].strip()
        if len(msg) == 0:
            await message.channel.send(command_prefix +
                                       "newbd Username#tag MM/DD")
            return
        msg = msg.split()
        if (len(msg) != 2) or (msg[0].count('#') != 1
                               or msg[1].count('/') != 1):
            await message.channel.send("Please use the following format:\n" +
                                       command_prefix +
                                       "newbd Username#tag MM/DD")
            return
        bdate = msg[1].split("/")
        user = msg[0].split("#", 1)
        username, tag = user[0], user[1]

        member = find_member(username, tag, message.guild)
        m, d = int(bdate[0]), int(bdate[1])

        if member == None:
            await message.channel.send("No such user.")
            return
        try:
            birthday = Birthday(member.id, m, d, member.guild.id)
        except ValueError as e:
            await message.channel.send(f"Invalid date: {e}")

        if add_birthday(birthday):
            await message.channel.send("User has been signed up.")
        else:
            await message.channel.send("User is already signed up.")

    # adds new birthday to greetings to a specific guild
    elif message.content.startswith(command_prefix + 'fnewbd'):
        log_command(message)
        if dev_id != message.author.id:
            return
        msg = message.content.split(command_prefix + 'fnewbd', 1)[1].strip()
        if len(msg) == 0:
            await message.channel.send(command_prefix +
                                       "fnewbd user_id MM/DD guild_id")
            return
        msg = msg.split()
        if len(msg) != 3 or msg[1].count('/') != 1:
            await message.channel.send("Please use the following format:\n" +
                                       command_prefix +
                                       "fnewbd user_id MM/DD guild_id")
            return
        user_id = int(msg[0])
        bdate = msg[1].split("/")
        guild_id = int(msg[2])

        guild = client.get_guild(guild_id)
        if guild == None:
            await message.channel.send("No such guild.")
            return
        member = guild.get_member(user_id)
        if member == None:
            await message.channel.send("No such user in that guild.")
            return
        m, d = int(bdate[0]), int(bdate[1])

        try:
            birthday = Birthday(member.id, m, d, guild.id)
        except ValueError as e:
            await message.channel.send(f"Invalid date: {e}")

        if add_birthday(birthday):
            await message.channel.send("User has been signed up.")
        else:
            await message.channel.send("User is already signed up.")

    # lists the database
    elif message.content.startswith(command_prefix + 'db'):
        log_command(message)
        bds = get_birthdays()
        if message.guild.id == dev_guild_id:
            for guild in client.guilds:
                await message.channel.send(
                    f"{guild.name}:\n\t" +
                    bds.list(guild.id).replace('\n', '\n\t'))
        else:
            await message.channel.send(bds.list(message.guild.id))

        datas = get_default_channels()
        res = ""
        if datas == None:
            await message.channel.send("There is no set channel.")
            return
        if message.guild.id == dev_guild_id:
            for d in datas:
                channel = client.get_channel(
                    get_default_channel(int(d["guild_id"])))
                g = client.get_guild(int(d["guild_id"])).name
                guild = g + ("'" if g[-1].lower() == "s" else "'s")
                res += f"{guild} birthday greetings are sent to {channel.name}.\n"
            await message.channel.send(res)
        else:
            channel = client.get_channel(get_default_channel(message.guild.id))
            await message.channel.send(
                f"Birthday greetings are sent to {channel.name}.")

    # sets the channel for birthday greetings
    elif message.content.startswith(command_prefix + 'setchannel'):
        log_command(message)
        msg = message.content.split(command_prefix + 'setchannel',
                                    1)[1].strip()
        if len(msg) == 0:
            await message.channel.send(command_prefix +
                                       "setchannel channel_id")
            return
        msg = msg.split()
        if (len(msg) != 1):
            await message.channel.send("Please use the following format:\n" +
                                       command_prefix +
                                       "setchannel channel_id")
            return
        channel_id = int(msg[0])
        if message.guild.get_channel(channel_id) == None:
            await message.channel.send("Invalid channel id!")
            return
        update_default_channel(message.guild.id, channel_id)
        channel = message.guild.get_channel(channel_id)
        await message.channel.send("Channel set to " + channel.name)

    # disconnects person from voice
    elif message.content.startswith(command_prefix + 'kick'):
        log_command(message)
        if dev_id != message.author.id:
            await message.channel.send(not_sanyi_text)
            return
        msg = message.content.split(command_prefix + 'kick', 1)[1].strip()
        if len(msg) == 0:
            await message.channel.send(command_prefix + "kick Username#tag")
            return
        user = msg.split("#")
        member = find_member(user[0], user[1], message.guild)
        if member == None:
            await message.channel.send("Elírtad...")
            return
        elif member == client.user:
            await message.channel.send("Ne bántsd már...")
        else:
            dm = member.dm_channel
            if dm is None:
                dm = await member.create_dm()
            await dm.send("Jó éjt")
        await member.move_to(None, reason="nealudj")

    # Puts a person in the afk channel
    elif message.content.startswith(command_prefix + 'afk'):
        log_command(message)
        if dev_id != message.author.id:
            await message.channel.send(not_sanyi_text)
            return
        msg = message.content.split(command_prefix + 'afk', 1)[1].strip()
        if len(msg) == 0:
            await message.channel.send(command_prefix + "afk Username#tag")
            return
        user = msg.split("#")
        member = find_member(user[0], user[1], message.guild)
        if member == None:
            await message.channel.send("Elírtad...")
            return
        await member.move_to(
            message.guild.afk_channel,
            reason=
            "no reason ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿"
        )

    # Deletes a message
    elif message.content.startswith(command_prefix + 'md'):
        log_command(message)
        if dev_id != message.author.id:
            await message.channel.send(not_sanyi_text)
            return
        msg = message.content.split(command_prefix + 'md', 1)[1].strip()
        if len(msg) == 0:
            await message.channel.send(command_prefix +
                                       "md textchannel_id message_id")
            return
        msg = msg.split()
        if len(msg) != 2:
            await message.channel.send("Please use the following format:\n" +
                                       command_prefix +
                                       "md textchannel_id message_id")
            return

        textchannel_id = int(msg[0])
        message_id = int(msg[1])

        channel = client.get_channel(textchannel_id)
        if channel == None:
            await message.channel.send("No such channel.")
            return
        msg = await channel.fetch_message(message_id)
        if msg == None:
            await message.channel.send("No such message in that channel.")
            return

        await msg.delete()

    # starts playing a song through the bot (rythm)
    elif message.content.startswith(command_prefix +
                                    'play') or message.content == (
                                        command_prefix + 'p'):
        log_command(message)
        searchbar = message.content.split(command_prefix + 'play',
                                          1)[1].strip()
        if len(searchbar) == 0:
            await message.channel.send(command_prefix +
                                       "play 'youtube_serachbar'")
            return
        try:
            print("\nplaying\n")
            await rythm2.play(searchbar, message)
        except RuntimeError:
            dev = await message.guild.fetch_member(dev_id)
            # os.system("python3 -m pip install -U discord.py[voice]")
            await message.channel.send("I'm not working properly...\n" +
                                       dev.mention + " please restart me")

    # lists rythm's next songs
    elif message.content.startswith(command_prefix +
                                    'queue') or message.content == (
                                        command_prefix + 'q'):
        log_command(message)
        await rythm2.queue(message)

    # skips rythm's current song
    elif message.content.startswith(command_prefix +
                                    'skip') or message.content == (
                                        command_prefix + 's'):
        log_command(message)
        await rythm2.skip(message)

    # kicks rythm
    elif message.content.startswith(command_prefix +
                                    'leave') or message.content == (
                                        command_prefix + 'l'):
        log_command(message)
        await rythm2.leave(message)

    # to check rythm variables for debugging
    elif message.content.startswith(command_prefix +
                                    'data') or message.content == (
                                        command_prefix + 'd'):
        log_command(message)
        if dev_id != message.author.id:
            await message.channel.send("Fúj! Mit csinálsz?! NEM SZABAD!!!")
            return
        await rythm2.datas(message)

    # send a message(text) to a specific channel(id)
    elif message.content.startswith(command_prefix + 'tmsg'):
        log_command(message)
        if dev_id != message.author.id:
            await message.channel.send("Fúj! Mit csinálsz?! NEM SZABAD!!!")
            return
        params = message.content.split(command_prefix + 'tmsg',
                                       1)[1].strip().split(" ", 1)
        channel_id = int(params[0])
        msg = params[1]
        target_channel = client.get_channel(channel_id)
        if target_channel is not None:
            await target_channel.send(msg)
        else:
            await message.channel.send("TextChannel with id " + channel_id +
                                       " not found.")

    # to reset greetings database after new year's eve
    elif message.content == (command_prefix + 'reset_greetings'):
        log_command(message)
        if dev_id != message.author.id:
            await message.channel.send("Fúj! Mit csinálsz?! NEM SZABAD!!!")
            return
        reset_greetings()
        await message.channel.send("Greetings have been reset.")

    # Rolls a die
    elif message.content.startswith(command_prefix + 'roll'):
        log_command(message)
        params = message.content.split(command_prefix + 'roll', 1)[1].strip()
        params = params.split("d", 1)
        if (len(params) != 2):
            await message.channel.send("Invalid format")
            return

        if (params[0] == ""):
            times = 1
        else:
            try:
                times = int(params[0].strip())
            except ValueError:
                await message.channel.send("Invalid format")
                return

        params = params[1].split("+", 1)
        try:
            die = int(params[0].strip())
        except ValueError:
            await message.channel.send("Invalid format")
            return

        plus = 0
        if (len(params) == 2):
            try:
                plus = int(params[1].strip())
            except IndexError:
                plus = 0
            except ValueError:
                await message.channel.send("Invalid format")
                return

        ret_list = []
        for i in range(times):
            ret_list.append(randrange(1, die) + plus)
        ret = f"Result of {times} d{die} "
        if (plus != 0):
            ret += f"(+{plus}) "
        ret += "roll:\n"
        ret += ", ".join([str(item) for item in ret_list])
        if (times > 1):
            ret += f"\nTotal: {sum(ret_list)}"
        await message.channel.send(ret)

    # audit command
    elif message.content == (command_prefix + 'audit'):
        log_command(message)
        if dev_id != message.author.id:
            await message.channel.send("Fúj! Mit csinálsz?! NEM SZABAD!!!")
            return
        guild = client.get_guild(berencek_id)
        entries = [entry async for entry in guild.audit_logs(limit=50)]
        res = ""
        for entry in entries:
            if entry.action.name == "member_update":
                continue
            created_at = entry.created_at
            created_at += timedelta(hours=2)
            created_at = created_at.strftime('%Y %b %d, %H:%M:%S')
            res += f'action: {entry.action.name}, by: {entry.user.name}, when: {created_at}'
            if entry.action.name != "invite_create":
                res += f'\ttarget: {entry.target}'
            if entry.action.name == "message_delete":
                res += f'\tchannel: {entry.extra.channel}'
            elif entry.action.name == "channel_update":
                changes = entry.__dict__["_changes"]
                for change in changes:
                    for key in change.keys():
                        res += "\n"
                        if key == "key":
                            res += f'\t{change[key]}:'
                        else:
                            res += f'\t\t{key}: {change[key]}'
            res += '\n'
        result = []
        if len(res) >= 2000:
            txt = ""
            for i in res.split("\n"):
                if len(txt + i + "\n") <= 2000:
                    txt += i + "\n"
                else:
                    result.append(txt)
                    txt = i + "\n"
            result.append(txt)
        else:
            result.append(res)
        for i in result:
            await message.channel.send(i)

    # test command
    elif message.content == (command_prefix + 't'):
        if dev_id != message.author.id:
            await message.channel.send("Fúj! Mit csinálsz?! NEM SZABAD!!!")
            return
        res = ""
        for voice in client.voice_clients:
            res += f"{voice.guild.name} > {voice.channel.name}\n"
        if res == "":
            res = "no voice channels"
        await message.channel.send(res)

    elif message.content.startswith(command_prefix + 'mw'):
        if dev_id != message.author.id:
            await message.channel.send("Fúj! Mit csinálsz?! NEM SZABAD!!!")
            return
        msg = message.content.split(command_prefix + 'mw', 1)[1].strip()
        if len(msg) == 0:
            await message.channel.send(command_prefix +
                                       "mw textchannel_id message_id")
            return
        msg = msg.split()
        if len(msg) != 2:
            await message.channel.send("Please use the following format:\n" +
                                       command_prefix +
                                       "mw textchannel_id message_id")
            return

        textchannel_id = int(msg[0])
        message_id = int(msg[1])

        channel = client.get_channel(textchannel_id)
        if channel == None:
            await message.channel.send("No such channel.")
            return
        msg = await channel.fetch_message(message_id)
        if msg == None:
            await message.channel.send("No such message in that channel.")
            return

        await message.channel.send(msg.created_at)

    ##########################DMs###########################
    #only dev gets these messages, its for me yay
    if dev_id != message.author.id:
        return

    elif message.content.startswith('done') or message.content == ('d'):
        if type(message.channel) is not discord.channel.DMChannel:
            return
        if nagging.is_running():
            nagging.stop()
            await message.channel.send("Good job!")

    elif message.content.startswith('stop'):
        if type(message.channel) is not discord.channel.DMChannel:
            return
        if time_to_squat.is_running():
            if nagging.is_running():
                nagging.stop()
            time_to_squat.stop()
            await message.channel.send("Okay :C")

    elif message.content.startswith('start'):
        if type(message.channel) is not discord.channel.DMChannel:
            return
        if time_to_squat.is_running():
            await message.channel.send("I'm already running.")
        else:
            time_to_squat.start()
            await message.channel.send("Yay :D")


##########################################################


@tasks.loop(minutes=90)
async def time_to_squat():
    now = local_time()
    if 11 <= now.hour <= 23 and not nagging.is_running():
        nagging.start()


@tasks.loop(minutes=5, count=3)
async def nagging():
    me = client.get_user(dev_id)
    dm = me.dm_channel
    if dm == None:
        dm = await me.create_dm()
    await dm.send("Time to do some squats!")


@tasks.loop(seconds=10)
async def april():
    now = local_time()
    if now.minute == 20:
        channel = client.get_channel(uptime_channel_id)
        await channel.send("https://tenor.com/view/weed-noweed-gif-20024478")
        april.stop()
    elif now.minute >= 21:
        april.stop()


##########################################################


@tasks.loop(hours=1)
async def reinstall_voice():
    os.system("python3 -m pip install -U discord.py[voice]")


# @tasks.loop(hours=1)
@tasks.loop(minutes=10)
async def called_on_time():
    await rythm2.leave_check()

    now = local_time()
    global apriltwenty
    if apriltwenty and now.month == 4 and now.day == 20 and now.hour == 4:
        apriltwenty = False
        april.start()

    if now.hour >= 11:
        birthdays = get_birthdays()
        for bd in birthdays.getRecords():
            if is_it_time(bd.getBirthday()) and not bd.greetedThisYear():
                guild_Id = bd.getGuild()
                channel = client.get_channel(get_default_channel(guild_Id))
                if channel is None:
                    print(
                        "Channel was None. Maybe there is no default channel for this guild: "
                        + guild_Id)
                    continue
                member = client.get_user(bd.getUser())
                await channel.send(
                    "Boldog születésnapot kívánok a Jedi Tanács nevében! Az erő legyen veled "
                    + member.mention)
                print(greet_user(bd.getUser(), bd.getGuild()))


if __name__ == '__main__':
    keep_alive()
    client.run(my_token)
    print("Server is running...")
