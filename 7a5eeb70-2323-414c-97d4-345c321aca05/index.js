const Discord = require("discord.js")
const client = new Discord.Client()
const mySecret = process.env['Token']

client.on("ready", () =>
{
    console.log(`Logged in as ${client.user.tags}!`)
})

client.on("message", msg => 
{
    if (msg.content === "ping")
    {
        msg.reply("pong")
    }
})


client.login(mySecret)

