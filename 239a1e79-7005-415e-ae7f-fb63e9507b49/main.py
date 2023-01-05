import discord
import os
import requests
import json
import random
from replit import db
import pandas as pd
#import plotly
from keep_alive import keep_alive
#import plotly.graph_objects as go
from datetime import datetime
import matplotlib.pyplot as plt

client = discord.Client()


def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + ' -' + json_data[0]['a']
	return (quote)


def get_price(ticker):
	base_url = "https://api.binance.com"
	url = f"/api/v3/ticker/price?symbol={ticker.upper()}"
	response = requests.get(base_url + url)
	json_data = json.loads(response.text)
	print(json_data)
	price = json_data['price']
	return (price)


def get_chart(ticker):
	base_url = "https://api.binance.com"
	url = f"/api/v3/klines?symbol={ticker.upper()}&interval=1h"
	response = requests.get(base_url + url)
	json_data = json.loads(response.text)
	#print(json_data)
	return json_data


def create_chart(df):
	fig = go.Figure(data=[
	    go.Candlestick(x=df['Date'],
	                   open=df['Open'],
	                   high=df['High'],
	                   low=df['Low'],
	                   close=df['Close'])
	])

	return fig  #.write_image("chart.png")


def update_bullish_vibes(bullish_message):
	if "bullish_vibes" in db.keys():
		bullish_vibes = db['bullish_vibes']
		bullish_vibes.append(bullish_message)
		db['bullish_vibes'] = bullish_vibes
	else:
		db['bullish_vibes'] = [bullish_message]


def delete_bullish_vibes(index):
	bullish_vibes = db['bullish_vibes']
	if len(bullish_vibes) > index:
		del bullish_vibes[index]
		db['bullish_vibes'] = bullish_vibes


bearish_words = ['sell', 'dump', 'dumping', 'bear', 'bearish', 'scared', 'damp']

starter_bullish = ["We are not bearish, we are bullish!",
                  "Let's Fucking Goooooo!",
                  'Up Only, Sir', "U gonna sell, u ngmi"]

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	msg = message.content
	msg_list = msg.split(" ")

	if msg.startswith("$hello"):
		await message.channel.send("Hello, Welcome to CryptoMoniez!")

	if msg.startswith("$signal"):
		await message.channel.send("Long now!")

	if msg.startswith("$inspire"):
		quote = get_quote()
		await message.channel.send(quote)

	options = starter_bullish
	if "bullish_vibes" in db.keys():
		options = options + list(db['bullish_vibes'])

	if msg.startswith("$new"):
		if "Pedro" in msg or "pedro" in msg or "chairo" in msg or "Chairo" in msg:
			response_message = "Lol, Belman. Good try"
			await message.channel.send(response_message)

		bullish_input = msg.split("$new ", 1)[1]
		update_bullish_vibes(bullish_input)
		await message.channel.send("New bullish vibe added.")

	if msg.startswith("$del"):
		bullish_vibes = []
		if "bullish_vibes" in db.keys():
			index = int(msg.split("$del", 1)[1])
			delete_bullish_vibes(index)
			bullish_vibes = db['bullish_vibes']
		await message.channel.send(bullish_vibes)

	if msg.startswith("$list"):
		bullish_vibes = []
		if "bullish_vibes" in db.keys():
			bullish_vibes = db['bullish_vibes']
		await message.channel.send(bullish_vibes)

	if any(str(x).lower() in bearish_words for x in msg_list):
		await message.channel.send(random.choice(options))

	if message.content.startswith("$getPrice"):
		ticker = msg.split("$getPrice ", 1)[1]
		price = get_price(ticker)
		await message.channel.send(f"{ticker}: " + price + ' -BINANCE')

	if message.content.startswith("$getChart"):
	  ticker = msg.split("$getChart ", 1)[1]
	  chart = get_chart(ticker)
	  chart_df = pd.DataFrame(chart,columns=[
		                            "OpenTime", "Open", "High", "Low", "Close",
		                            "Volume", "CloseTime", "QuoteAssetVolume",
		                            "NumberOfTrades", "TakerBuyBase",
		                            "TakerBuyQuote", "Ignore"])
	  cols = ["Open", "Close", "High","Low"]
	  chart_df[cols] = chart_df[cols].apply(pd.to_numeric)
	  chart_df["Date"] = pd.to_datetime(chart_df["CloseTime"], unit="ms")
	  chart_df.set_index("Date", inplace=True)
	  print(chart_df)
	  
	  chart_df["Close"].plot.line()
	  plt.title(f"Close Price {ticker}")
	  plt.xlabel("Date")
	  plt.ylabel("Price")
	  plt.savefig("no2_concentrations.png")
	  plt.close()
	  await message.channel.send(file=discord.File('no2_concentrations.png'))
	  
keep_alive()
client.run(os.getenv('TOKEN'))