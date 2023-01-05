import os
import discord
import random
from discord.ext import commands
import sys
from keep_alive import keep_alive

my_secret = os.environ['token']
bot = commands.Bot(command_prefix='$')
nicki = []
oczka = []
path = os.getcwd()
filename = path+"/zadania_discord.txt"

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name=f"$pomoc aby wyswietlic instrukcje"))

@bot.command()
async def pomoc(ctx):
  embed = discord.Embed(
    title="Pomoc", 
    colour=discord.Colour.red()
    )
  embed.set_author(name="Autor: Jazo")

  embed.add_field(name="$graj ***", value="Rozpoczyna gre, w miejsce gwiazdek wpisz nazwy graczy po spacjach")
  embed.add_field(name="$n", value="Wykonujesz swoj ruch")
  embed.add_field(name="$restart", value="Przygotowuje bota do nastepnej gry")
  
  await ctx.channel.send(embed=embed)

@bot.command()
async def clear(ctx, amount=100):
  await ctx.channel.purge(limit=amount)


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@bot.command()
async def restart(ctx):
    await ctx.message.delete()
    await ctx.channel.send("Restartowanie...")
    restart_program()



@bot.command()
async def graj(ctx, *nicki):
  if len(nicki) == 0:
    await ctx.channel.send("Nie moze byc 0 graczy")
    await restart(ctx)
  await ctx.send('{} graczy: {}'.format(len(nicki), ', '.join(nicki)))
  for x in range(0, len(nicki)):
    oczka.append(0)
  file = open(filename, "r")
  zadania = file.readlines()
  zadania = random.sample(zadania, 69)
  file.close()

  async def chinol():
    while True:
      for x in range(0, len(nicki)):
        await ctx.channel.send(nicki[x] + " twoj ruch")
        try:
          message = await bot.wait_for('message', check=lambda m: m.channel == ctx.channel)
        except:
          await ctx.channel.send("error")
        else:
          if message.content == "$restart":
            return
          elif message.content == "$n":
            kostka = random.randint(1, 6)
            await ctx.channel.send("Wyrzuciles " + str(kostka) + " oczek")
            oczka[x] += kostka
            if oczka[x] >= 69:
              await ctx.channel.send("Koniec gry, wygral " + nicki[x] + "!\n\n")
              return
            await ctx.channel.send(zadania[oczka[x]-1])

            if zadania[oczka[x]-1] == 'Zamieniasz sie z graczem ktory byl na najdalszym polu i oboje pijecie':
                  max = 0
                  for y in range(0, nicki):
                      if oczka[y] >= oczka[max]:
                          max = y
                  oczka[x], oczka[max] = oczka[max], oczka[x]
            elif zadania[oczka[x]-1] == 'Pijesz i wracasz na start':
                oczka[x] = 0
            elif zadania[oczka[x]-1] == 'Idziesz na pole 9 i pijesz 1x':
                oczka[x] = 9
            elif zadania[oczka[x]-1] == 'Cofasz sie o 6 pol':
                oczka[x] -= 6
                if oczka[x] < 0:
                    oczka[x] = 0
            elif zadania[oczka[x]-1] == 'Niefart, wracasz na start i pijesz 3x':
                oczka[x] = 0
            elif zadania[oczka[x]-1] == 'Wszyscy cofaja sie o 1 pole':
                for i in range(0,nicki):
                    oczka[i] -= 1 
            
            for x in range(0, len(nicki)):
              await ctx.channel.send(nicki[x] + ": " + str(oczka[x]))

            

    
      

  await chinol()
  

    
keep_alive()
bot.run(my_secret)