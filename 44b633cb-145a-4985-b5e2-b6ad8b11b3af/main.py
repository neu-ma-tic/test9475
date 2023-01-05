# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import random
import time
import os
from keep_alive import keep_alive

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.

bot = discord.Client(intents=discord.Intents.all())
global guess
g=0
gu=0
guess=['.guess 1','.guess 2','.guess 3','.guess 4','.guess 5','.guess 6','.guess 7','.guess 8','.guess 9','.guess 10']
deathoutn=['You successfully murdered {}','You stole all of {}\'s money but they escaped with their lives','You managed to kill {} but, You felt too guilty and died of EMOTIONAL DAMAGE']
deathout=['As you were about to kill them, They were 5 steps ahead of you and replaced themselves with realistic holograms which detected your movement and alerted the police to arrest you','You were too slow because you are fat which scared them more than the fact that you were attempting to murder them','You left behind no clues and managed to get away with the crime']
deathoutrl=[deathoutn,deathout]
hfusr=['monke_113','ralph_8625','yellowman_634','jeffbezoz_1964','musk_XÆA-Xii','begula','gamer_5419','emokid123','crazyman999999','lildead_87','alienbot_547']
unl=[]

commands=['.hello','.How are you?','.instagram','.info','.guess (any number from 1-10)','.hack (username)','.kill (username)']
# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("randombot0903 is in " + str(guild_count) + " guilds.")
def usercoins(user,usercoinb):
        unl.append(user)
        unl.append(usercoinb)
# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content.lower() == ".help":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send(commands)
	if message.content.lower() == ".hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("Hi there!, I am randombot0903!")
	if message.content.lower().replace(' ','')[:10] == ".howareyou":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("Imagine being so lonely asking a bot with no feelings this question as the only way you can interact with someone because you have no friends \nhttps://tenor.com/view/cool-im-so-tom-cruise-gif-13209253")
	if message.content.lower() == ".instagram":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("https://www.instagram.com/leomessi/?hl=en")
	if message.content.lower()[:6] == ".kill ":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		if random.choice(deathoutrl) == deathoutn:
		  await message.channel.send(random.choice(deathoutn).format(message.content[6:]))
		else:
		  await message.channel.send(random.choice(deathout))
	if message.content.lower() == ".info":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("Hi, I'm a bot created by a person who is dead#1558")
	if message.content[:6] == ".hack ":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("Hacking "+message.content[6:]+"...")
		time.sleep(2)
		message = await message.channel.send("Accessing databases... 26%")
		time.sleep(1.5)
		await message.edit(content="Searching for Social media accounts... 42%")
		time.sleep(1.5)
		await message.edit(content="Copying Bank Balance... 67%")
		time.sleep(1.1)
		await message.edit(content="Finding IP address through satellites... 89%")
		time.sleep(1.7)
		await message.edit(content="Hack Completed! 100%")
		rfusr=random.choice(hfusr)
		await message.channel.send("Username: "+ rfusr)
		await message.channel.send("IP address: "+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255)))
		await message.channel.send("Bank Balance: $"+ str(random.randint(1,1000000)))
		await message.channel.send("Picture: ")
		if rfusr == 'monke_113':
			await message.channel.send(file=discord.File('Lemonke.png'))
		elif rfusr == 'ralph_8625':
			await message.channel.send(file=discord.File('ralphmeme.jpg'))
		elif rfusr == 'yellowman_634':
			await message.channel.send(file=discord.File('yellowman.png'))
		elif rfusr == 'jeffbezoz_1964':
			await message.channel.send(file=discord.File('jeffbezoz.jpg'))
		elif rfusr == 'musk_XÆA-Xii':
			await message.channel.send(file=discord.File('muswnbb.jpg'))
		elif rfusr == 'begula':
			await message.channel.send(file=discord.File('memecat1.jpg'))
		elif rfusr == 'gamer_5419':
			await message.channel.send(file=discord.File('gamerkid.jpg'))
		elif rfusr == 'emokid123':
			await message.channel.send(file=discord.File('sadmeme.jpg'))
		elif rfusr == 'crazyman999999':
			await message.channel.send(file=discord.File('crazyman.jpg'))
		elif rfusr == 'lildead_87':
			await message.channel.send(file=discord.File('graveded.jpg'))
		else:
			await message.channel.send(file=discord.File('alienbot.jpg'))
	if message.content == ".coins":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send(str(unl[(unl.index(discord.Message.author.name)+1)]))
	if message.content in guess:
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		global g
		global gu
		gu=1
		g=random.choice(guess)
		rnfg = g[7:]
	if message.content == g and gu==1:
		# SENDS BACK A MESSAGE TO THE CHANNEL.
	        await message.channel.send("You guessed it, Psychic Powers??")
	        gu=0
	if message.content != g and gu==1:
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("You lost, The correct answer was "+rnfg+", Try again loser")
		gu=0
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
keep_alive()
try:
  bot.run(os.getenv('TOKEN'))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')
