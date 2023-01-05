import discord
import requests
import json
import os
import re
from keep_alive import keep_alive
from arithmetics import *
import random
from time import time


client = discord.Client()
Stop=False
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n- " + json_data[0]['a']
    return quote

def dwn(url,name="image"):
  response = requests.get(url)
  path=f"{name}_{time()}.jpg"
  with open(path, "wb") as file:
    file.write(response.content)
  return path

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global Stop
    if message.author == client.user:
        return

    msg = message.content.lower()

    if "config" in msg:
        nb=int(msg.split(" ")[1])
        quote = "All Bot responses are {}".format(["off","on"][nb])
        Stop = True if nb==0 else False
        await message.channel.send(quote)

    if not Stop:
      if "purge" in msg and "Mathsphile#7389" == f"{message.author}":
          await message.channel.purge(limit=1000)

      if "inspire" in msg or "quote" in msg:
          quote = get_quote()
          await message.channel.send(quote)

      if "hello" in msg:
          quote = f"Hello ! {message.author}"
          await message.channel.send(quote)

      if "pic" in msg:
          replys=msg.split("pic")[1].split(";")
          for reply in replys:
            reply=reply.strip().replace(' ',',')
            url = 'https://unsplash.it/2000'
            if reply!="":
              url = f"https://source.unsplash.com/2000x2000/?{reply}"
            path=dwn(url,reply)
            await message.channel.send(file=discord.File(path))
            os.remove(path)

      if "define" in msg:
          wordnik = os.environ['wordnik']
          mot = msg.split("define")[1].strip()
          f = f"https://api.wordnik.com/v4/word.json/{mot}/definitions?limit=10&api_key={wordnik}"
          resp = requests.get(f)
          datas = resp.json()
          reply = "__"+mot.title()+"__"
          for data in datas:
              if "text" in data:
                  p = "verb"
                  if "partOfSpeech" in data:
                      p = data["partOfSpeech"]
                  t = data["text"]
                  t=t.replace('<i>','*').replace('</i>','*')
                  t=t.replace('<em>','**').replace('</em>','**')
                  reply += f"\n\n{p.title()}\t:\n{t}"
          await message.channel.send(reply)
          
      # if re.search(r"^file", msg):
      #   await message.channel.send(message.attachments)
      if re.search(r"^math", msg):
            await message.channel.purge(limit=1)
            await message.channel.send("===========================")
            reply = ""
            if "pgcd" in msg:
                a, b = re.findall(r"[0-9]+", msg)
                reply = f"The PGCD of {a} and {b} is {pgcd(int(a),int(b))}"

            elif "primes" in msg:
                a, b = re.findall(r"[0-9]+", msg)
                reply = f"The prime numbers between {a} and {b} are :\n{primes(int(a),int(b))}"

            elif "ppcm" in msg or "ppmc" in msg:
                a, b = re.findall(r"[0-9]+", msg)
                reply = f"The PPMC of {a} and {b} is {ppmc(int(a),int(b))}"

            elif "decompose" in msg:
                def seul(a):
                  a = int(a)
                  datas = [f"{d['f']}^{d['s']}" if d['s'] > 1 else f"{d['f']}" for d in prime_factors(a)]
                  return f"{a} = {' x '.join(datas)}"

                numbers = re.findall(r"[0-9]+", msg)
                a=numbers[0]
                reply += seul(a)
                for a in numbers[1:]:
                  reply += "\n"+seul(a)

            elif "factoriel" in msg:
                def seul(a):
                  datas = factoriel(int(a))
                  return f"{a}! = {datas}"                  
                numbers = re.findall(r"[0-9]+", msg)
                a=numbers[0]
                reply += seul(a)
                for a in numbers[1:]:
                  reply += "\n"+seul(a)

            elif "fibonacci" in msg:
                def seul(a):
                  datas = fibbonacci(int(a))
                  return f"Fib({a}) = {datas}"

                numbers = re.findall(r"[0-9]+", msg)
                a=numbers[0]
                reply += seul(a)
                for a in numbers[1:]:
                  reply += "\n"+seul(a)

            elif "isprime" in msg:
                def seul(a):
                  a = int(a)
                  res = "indeed" if is_prime(a) else "not"
                  reply = f"{a} is {res} a prime number"
                  if not is_prime(a):
                      datas = [f"{d['f']}^{d['s']}" if d['s'] > 1 else f"{d['f']}" for d in prime_factors(int(a))]
                      reply += f"\nBecause : {a} = {' x '.join(datas)}\n"
                  return reply

                numbers = re.findall(r"[0-9]+", msg)
                a=numbers[0]
                reply += seul(a)
                for a in numbers[1:]:
                  reply += "\n"+seul(a)
            else:
                reply = "Make sure your math command is correct !"
            await message.channel.send(reply)

my_secret = os.environ['discord_tokken']

keep_alive()
client.run(my_secret)
