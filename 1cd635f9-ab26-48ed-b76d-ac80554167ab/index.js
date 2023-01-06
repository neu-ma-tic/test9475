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

client.on("message", message => {
  if(message.content === "404.ping") {
    message.channel.send("pong")
  }
})

client.on("message", message => {
  if(message.content === "404.requirements") {
    message.channel.send("Rank: C1+")
    message.channel.send("LVL 1000")
    message.channel.send("Have atleast one bijuu level max")
    message.channel.send("50 or -50 REP")
  }
})

client.login(process.env.token)