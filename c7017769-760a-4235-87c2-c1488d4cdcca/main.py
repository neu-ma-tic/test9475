import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="not very winning vids"))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@client.event
async def on_message(message):
  if message.author == client.user:
        return

  if message.content.startswith('!joke'):
        joke = get_joke()
        await message.channel.send(joke)

  if message.content.startswith('>invite'):
        await message.channel.send(
            "https://discord.com/api/oauth2/authorize?client_id=805934920283193406&permissions=8&scope=bot")

  if message.content.startswith('>hammer'):
        await message.channel.send("https://tenor.com/view/city-hunter-ryo-saeba-kaori-makimura-go-to-horny-jail-bonk-gif-18541691")

  if message.content.startswith('>corona2020'):
        await message.channel.send("https://cdn.discordapp.com/attachments/734295365452431390/737700297799106680/video0.mp4")
  
  if message.content.startswith('>bat'):
        await message.channel.send("https://tenor.com/view/prison-of-simps-horny-jail-gif-18556059")

  if message.content.startswith('>embedfail'):
        await message.channel.send("https://cdn.discordapp.com/attachments/728129476491214882/813494326050291762/epicembedfail.gif")

  if message.content.startswith('>info'):
        await message.channel.send(
            "`Hello, my prefix is '>' and I am a Python discord bot. Hmm, there must be some secret commands...`"
        )

  if message.content.startswith('>commands'):
        await message.channel.send(
            "`All commands lowercase, prefix is > : quote, invite, embedfail, didiask, kfctheory, raidsponsor, info, sourcecode, serverinvite, java, snake, blank, opinion, universe, thomas, codejoke, jspyjoke, ghostjoke, programmer, stevemining, corona2020`"
        )

  if message.content.startswith('>serverinvite'):
        await message.channel.send("`Join the Bot Testing server made by the owner!` https://discord.gg/Z89Xr4wRKn")
  
  if message.content.startswith('>bonk'):
        await message.channel.send("https://tenor.com/view/hornyjail-bonk-baseballbat-kitty-cat-gif-19401897")

  if message.content.startswith('>stevemining'):
    await message.channel.send("https://cdn.discordapp.com/attachments/280852949046132737/778306686737055785/unknown-1-1.png")

  if message.content.startswith('>sourcecode'):
      await message.channel.send("https://repl.it/@Guest06201/DiscordBot")

  if message.content.startswith('>didiask'):
      await message.channel.send("https://cdn.discordapp.com/attachments/769333880389500958/793006052022943764/didiask.jpg")
    
  if message.content.startswith('>opinion'):
      await message.channel.send("https://cdn.discordapp.com/attachments/728129476491214882/813469110422732810/didiaskv2.png")
    
  if message.content.startswith('>universe'):
      await message.channel.send("https://cdn.discordapp.com/attachments/728129476491214882/813470125130383443/universe.png")
  
  if message.content.startswith('>video'):
      await message.channel.send("https://cdn.discordapp.com/attachments/667386058736009226/815070326106488832/video0_1.mp4")

  if message.content.startswith('>thomas'):
      await message.channel.send(" https://cdn.discordapp.com/attachments/806582012110045253/815990827310383164/trainmc.png")

  if message.content.startswith('>codejoke'):
      await message.channel.send("```How do functions break up? They stop calling each other!```")      
    
  if message.content.startswith('>ghostjoke'):
      await message.channel.send("``What's a ghost's favorite type? Booooooolean!``")
    
  if message.content.startswith('>programmer'):
      await message.channel.send("``Why do Java Programmers wear glasses? Because they don't C#.``")

  if message.content.startswith('>jspyjoke'):
      await message.channel.send("**Python: This is plagiarism, you can't just -import essay-. Java: I'm two pages in and I still have no idea what you are saying.**")

  if message.content.startswith('>kfctheory'):
      await message.channel.send("KFC. KFC is red. Red is the color red. Red has three letters. KFC also. 3 x 3 = 9. seven eight nine.  seven, who ate nine. there are 7 days in a week. week rhymes with leak. Beak. Chickens have beaks. Chicken. Chickens have two wings. Humans have 0 wings. 2+0 is 2. The Colonel has two eyes. So do chickens. 2+2 =4. there are 4 letters in the first 4 letters of Mcdonalds, which sells chicken. KFC sells chicken. There are 9 letters in the word mcdonalds. 9 rhymes with electromagnetic delay line. magnet. magnets are metal. So are cages. Chickens are kept in cages. is this where KFC gets their chicken? Lets find out. Chickens have 2 legs, so do humans, 2 + 2 =4, the Colonel has 4 limbs. Chickens have four limbs if you count their wings. 4/4 = 1. The illuminati has one eye. **KFC IS ILLUMINATI CONFIRMED.**")

  if message.content.startswith('>raidsponsor'):
      await message.channel.send("**This bot was sponsored by Raid Shadow Legends, one of the biggest mobile role-playing games of 2021 and it's totally free! Currently almost 10 million users have joined Raid over the last six months, and it's one of the most impressive games in its class with detailed models, environments and smooth 60 frames per second animations! All the champions in the game can be customized with unique gear that changes your strategic buffs and abilities! The dungeon bosses have some ridiculous skills of their own and figuring out the perfect party and strategy to overtake them's a lot of fun! Currently with over 300,000 reviews, Raid has almost a perfect score on the Play Store! The community is growing fast and the highly anticipated new faction wars feature is now live, you might even find my squad out there in the arena! It's easier to start now than ever with rates program for new players you get a new daily login reward for the first 90 days that you play in the game! So what are you waiting for? Go to the video description, click on the special links and you'll get 50,000 silver and a free epic champion as part of the new player program to start your journey! Good luck and I'll see you here at** https://plarium.com!`")

  if message.content.startswith('>java'):
      await message.channel.send("**Add the java bot here!** https://discord.com/api/oauth2/authorize?client_id=806611240599552037&permissions=522304&scope=bot")

  if message.content.startswith('>snake'):
      await message.channel.send("```Snake... why are we still here? Just to suffer? Every night, I can feel my leg and my arm... even my fingers... the body I've lost... the comrades I've lost... won't stop hurting. It's like they're all still there. You feel it too, don't you? I'm the one who got caught up with Cipher. A group above nations... even the US. And I was the parasite below, feeding off Zero's power. They came after you in Cyprus... then Afghanistan... Cipher... just keeps growing. Swallowing everything in it's path. Getting bigger and bigger... Who knows how big now? Boss. I'm gonna make 'em give back our past... take back everything that we've lost. And I won't rest... until we do.```")

  if message.content.startswith('>blank'):
      await message.channel.send("https://media.discordapp.net/attachments/750068339375603725/782017385250816000/rick.gif")

  if message.content.startswith('>pacertest'):
      await message.channel.send("```The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.```")
  
  if message.content.startswith('>joker'):
    await message.channel.send("https://cdn.discordapp.com/attachments/680928626010750990/723174035881459763/Joker_2019.webm")
  
  if message.content.startswith('>shrek'):
    await message.channel.send("https://cdn.discordapp.com/attachments/648400331583258631/710745534486282280/SHREK.webm")

keep_alive()

print('Code is fine, dont mind the output if there seems to be errors.')

client.run(os.getenv('TOKEN'))