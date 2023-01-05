import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands


client = discord.Client()

@client.event
async def on_ready():
  print('Connecté en tant que {0.user}'.format(client)   )


@client.event
async def on_message(message):


  if message.author == client.user :
    return
  
  #----------------------------------------ressources----------------------------#
  lemec = (message.author.mention)
  
  rebjr =   ['salut beau gosse de la night','yo connard','coucou bebou :heart:','salutation messire','AYAYAYA matez moi ce bg {}'.format(lemec),'OUHOUH C REPARTI COMME EN 46']   

  resava = ['ça va et toi ?', 'On est là, comment ça va {} ?'.format(lemec),'Couci couça mais bon... ça dit quoi de ton côté?','Au calme mon reuf et toi ?','Non :( ','Je pense au suicide actuellement','Tranquille bg, dis moi tout {}'.format(lemec),'bof mais bon on avance et toi ?',"ça va pas top #emorap :call_me:"]

  bjr = ['salut','bonjour','coucou','bonsoir','wsh','bjr','slt','yo'
,'cc']
  
  cava = ['ça va ?','ca va ?','ça va?','ca va?','ça dit quoi ?','ça dit quoi?','ça dit quoi ?', 'ca dit quoi ?',' ca dit quoi?','tu vas bien ?','tu vas bien?', 'tu va bien?', 'tu va bien ?']

  merciList = ['merci','cimer','mrc','merce']

  miaouList = ['miaou','miou','meow','meouw','miao','mieou','mieouw','miaouw']

  citalist = ["https://discord.com/channels/783335537062576178/814640832120487956/814640899777888276","https://discord.com/channels/783335537062576178/814640832120487956/814887679199805510"]
  
  #------------------------------------------IF------------------------------------#


  if message.content.lower() in bjr:
    await message.channel.send('{}'.format(random.choice(rebjr))) 
  
  if message.content.lower() in cava :
    await message.channel.send ('{}'.format(random.choice(resava)))
  
  if 'sa va' in message.content.lower () or 'sava ' in message.content.lower (): 
    await message.channel.send ("ça va*. Grosse merde de {}, apprends à écrire putain! ".format(lemec))

  if 'traitre' in message.content.lower () or 'traître' in message.content.lower() or 'trahison' in message.content.lower ():
    await message.channel.send("Tu n'es pas seulement un lâche, tu es aussi un traître comme ta petite taille le laissait deviner")    

  if message.content.startswith('!sinj') or message.content.startswith('!singe'):
    await message.channel.send ('OUHOUHOUHAHAH') 
 
  if 'on taff' in message.content.lower () or 'on bosse' in message.content.lower() or 'on travaille' in message.content.lower ():
    await message.channel.send('non.')
 
  if 'petite pause' in message.content.lower() :
    await message.channel.send('allez')

  if message.content.startswith('bon toutou'):
    await message.channel.send('Wouaf Wouaf')
 
  if 'covid' in message.content.lower() or 'virus' in message.content.lower () or 'corona' in message.content.lower ():
    await message.channel.send(" #COVID #CLAMERDE ")
 
  if 'ta gueule' in message.content.lower () or 'tg' in message.content.lower():
    await message.channel.send("QUOI MA GUEULE ? QU'EST CE QU'ELLE A MA GUEULE ? :musical_note:")

  if  'grrr' in message.content.lower ():
    await message.channel.send("{} :cat:".format(random.choice(miaouList)))
  
  if message.content.lower () in miaouList:
    await message.channel.send("Grrr :heart: :D")

  if message.content.lower() in merciList :
    await message.channel.send("Derien {} :heart:".format(lemec))

  if 'situation' in message.content.lower() :
    await message.channel.send("Vous savez, moi je ne crois pas qu’il y ait de bonne ou de mauvaise situation. :thinking:  Moi, si je devais résumer ma vie aujourd’hui avec vous, je dirais que c’est d’abord des rencontres. :handshake:  Des gens qui m’ont tendu la main, :raised_back_of_hand: peut-être à un moment où je ne pouvais pas, où j’étais seul chez moi. :homes: Et c’est assez curieux :interrobang: de se dire que les hasards, les rencontres forgent une destinée… Parce que quand on a le goût de la chose, quand on a le goût de la chose bien faite, le beau geste, parfois on ne trouve pas l’interlocuteur en face :people_hugging:  je dirais, le miroir :mirror: qui vous aide à avancer :man_walking: . Alors ça n’est pas mon cas :person_gesturing_no: , comme je disais là, puisque moi au contraire, j’ai pu : et je dis merci à la vie, je lui dis merci, je chante la vie :microphone: , je danse la vie :dancer: … je ne suis qu’amour :heart: ! Et finalement, quand beaucoup de gens aujourd’hui me disent « Mais comment fais-tu pour avoir cette humanité ?  :health_worker: », et bien je leur réponds très simplement, je leur dis que c’est ce goût de l’amour :heart: ce goût donc qui m’a poussé aujourd’hui à entreprendre une construction mécanique :wrench: , mais demain qui sait ? Peut-être simplement à me mettre au service de la communauté, à faire le don, le don de soi…:dollar:")

  
  if 'dictature' in message.content.lower():
    await message.channel.send ("Une dictature, comme vous y allez ! Vous êtes bien sympathique {}, mais épargnez-moi vos analyses politiques… Savez-vous seulement ce que c'est qu'une dictature ? Une dictature c'est quand les gens sont communistes, déjà. Qu'ils ont froid, avec des chapeaux gris et des chaussures à fermeture éclair. C'est ça, une dictature, {}".format(lemec,lemec))
  

  if 'wolframalpha' in message.content.lower () or 'wolfram' in message.content.lower ():
    await message.channel.send ("https://media.discordapp.net/attachments/820353448531853332/820757885557932059/unknown.png")

  if '!Citation' in message.content.lower():
    await message.channel.send
    ("")

#---------------------------------vocal---------------------------------------------- 


#--------------------------------citations-------------------------------------------




    


#help bot-----------------------------------------------
keep_alive()
client.run(os.getenv('TOKEN'))


