const Discord = require('discord.js')
const client = new Discord.client()
const config = require("./config.json")

client.on("ready", () => {
  console.log("Development bot sucessfully -Online".blue)
})

client.login(config.token)