const linkvertise = require("linkvertise")

const Discord = require('discord.js')
const client = new Discord.Client()
const express = require('express')
const app = express()

linkvertise("https://example.com", 334940)

app.get ("!", (req, res) => {
  res.send("hello hell!")
})

client.once('ready', () => {
    console.log('Cobies Bot is Online!');
});



client.login('ODY0MzEwNjQ0MTQwMDE1NjM3.YOzmAw.UqphNs5RZf3Ew0dR1ECbwCPrmPA')