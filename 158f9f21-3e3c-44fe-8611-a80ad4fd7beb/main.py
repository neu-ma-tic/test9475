import discord
import os
import requests
import json
from selenium import webdriver

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return(quote)




küfür = []
with open("karaliste.txt", "r", encoding="utf-8") as file:
    küfürler = file.read()
    küfür = küfürler.split()

@client.event
async def on_ready():
    print("Canım hoş geldin gel şöyle otur soluklan {0.user}".format(client))

@client.event
async  def on_message(message):
    if (message.author == client.user):
        return

    if message.content.startswith("$merhaba"):
        await message.channel.send("hayat zor be gülüm")

    message_words = message.content.split()
    for i in message_words:
        for j in küfür:
            if (i == j):
                await message.channel.send("de sus amk")
                break
    if message.content.startswith("!söz"):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith("!çevir"):
        driver = webdriver.Chrome()

        kelime = message.content.strip("!çevir")

        kelime = kelime.replace(" ", "%20")
        new_url = "https://translate.google.com/?hl=tr&sl=en&tl=tr&text=" + kelime + "&op=translate"
        driver.get(new_url)
        çeviri = driver.find_element_by_css_selector(
            "#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb > div.dePhmb > div > div.J0lOec > span.VIiyi")
        await message.channel.send(çeviri.text)
        driver.close()





client.run(os.getenv("TOKEN"))




