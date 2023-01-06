const Discord = require("discord.js")
const client = new Discord.Client()

client.on("ready", () => {
  console.log(`Logged in as $
  {client.user.tag}!`)
})

client.on("message", msg => {
  if (msg.content === "example") {
    msg.reply("this is a filler message") 
  }
})

client.login(process.env.TOKEN)
const mySecret = process.env['TOKEN']
