import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("Hiya, Minecrafters!")


@client.event
async def on_message(message):
  # message.author
  # message.channel
  # message.content
  # self.user
  msgauth=message.author
  msgauth=str(msgauth)
  if message.content.lower() == "%pizza":
    await message.channel.send("Sorry, i ate it all, "+ msgauth)
  if message.content.lower() == "%meme":
    await message.channel.send("im too sad to tell a meme "+ msgauth)
  if message.content.lower() == "%ping":
    await message.channel.send("pong "+ msgauth)
  if message.content.lower() == "%bestbot":
    await message.channel.send("Me ofc."+ msgauth)
  if message.content.lower() == "%minecraft":
    await message.channel.send("I love minecraft!"+ msgauth)
  if message.content.lower() == "%hey":
    await message.channel.send("ho "+ msgauth)
  if message.content.lower() == "%nitro":
    await message.channel.send("bladers500 "+ msgauth)
  if message.content.lower() == "%Alpha":
    await message.channel.send("Colbi "+ msgauth)
  if message.content.lower() == "%rip":
    await message.channel.send("rest in peace "+ msgauth)
  if message.content.lower() == "%slap":
    await message.channel.send("*smaky waky* "+ msgauth)
  if message.content.lower() == "%lol":
    await message.channel.send("Whats so funny?"+ msgauth)
  if message.content.lower() == "%kill":
    await message.channel.send(msgauth,"died by staring at an enderman for too long")
  if message.content.lower() == "%creater":
    await message.channel.send("@AlphaOmega and his smart teacher @milloni "+ msgauth)
  if message.content.lower() == "%pizza2":
    await message.channel.send("Sorry, i ate that one aswell... "+ msgauth)




def main():
  token = os.environ["BOT_TOKEN"]
  client.run(token)

if __name__ == '__main__':
  main()
