const Discord = require("discord.js")
const { Client, Intents } = require('discord.js');
// Create a new client instance
const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`)
})

client.on("message", ms => {
  if (msg.content === "ping") {
    msg.reply("pong")
  }
})

client.login(process.env.TOKEN)

