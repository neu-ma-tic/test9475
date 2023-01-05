import discord
from google.cloud import secretmanager

# create the Secret Manager client
secret_client = secretmanager.SecretManagerServiceClient()

# resource name of the secret version
resource_name = "projects/850171112360/secrets/discord_bot_token/versions/1"

# access the secret version
secret_response = secret_client.access_secret_version(request={"name": resource_name})

# get the secret payload
secret_payload = secret_response.payload.data.decode("UTF-8")

client = discord.Client()
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user and "poop" in message.content.lower():
        await message.channel.send("Did you mention poop? I love eating poop!")
        
client.run(secret_payload)