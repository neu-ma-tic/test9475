//https://www.youtube.com/watch?v=1jtAWZK3Bbk
//npm i discord.js@13
//node index.js
//ctrl+c to stop bot running
const Discord = require("discord.js")
const TOKEN = "MTAzOTMzOTE2MTk1NTYwNjYwOQ.GBsfoN.VRbxkp0c4d4e-O-oTjTJWlq_4mqBuUD4khtnRw"
//const client = new Discord.Client()
/*
const { Client, GatewayIntentBits } = require('discord.js');
const client = new Discord.Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
  ] 
})
*/

const client = new Discord.Client({
  intents: [
    "GUILDS",
    "GUILD_MESSAGES"
  ]
})

//const { Client, Intents } = require('discord.js')
//const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] })

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`)
})

client.on("messageCreate", (message) => {
  if (message.content == "hi"){
    message.reply("Hello World")
  }
})


/*
client.on("message", msg => {
  if(msg.content === "ping") {
    msg.reply("pong")
  }
})
*/

//client.login(process.env.TOKEN)
//client.run(TOKEN)
client.login(TOKEN)
