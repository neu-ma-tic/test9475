const express = require("express");
const app = express()

app.listen(3000, () => {
  console.log("Project is running!");
})

app.get("/", (req, res) => {
  res.send("Hello world!");
})
    
const Discord = require("discord.js")
const client = new Discord.Client({intents: ["GUILDS", "GUILD_MESSAGES"]});

client.on("messageCreate", message => {
  if(message.content === "nigger") {
    message.channel.send("https://cdn.discordapp.com/attachments/970659047470682182/970808129434570772/IMG_2172.mov")
  }
})

client.login(process.env.token)