const express = require("express")
const app = express()

app.get("/", (req, res) => {
  res.send("Hello Noob! Welcome back!")
})

app.listen(3000, () => {
  console.log("Project is ready!")
})

let Discord = require("discord.js")
let client = new Discord.Client()


client.on('ready', () => {
 client.user.setActivity(`TO PQNOS!`, { type: 'SUBSCRIBE'})
const mySecret = process.env['DISCORD_TOKEN']

})

client.login(process.env.token);