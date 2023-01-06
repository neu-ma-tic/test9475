// DISCORD //
const Discord = require("discord.js");
const Main = require("./main.js");
const bot = new Main();
const client = new Discord.Client({
  intents: [
    "GUILDS",
    "GUILD_MESSAGES"
  ]
})


client.on("ready", () => {
  console.log("Logged into Jam's Server")
})

client.on("messageCreate", message => {
  if (message.author.bot) return;
  bot.filter(message);
  
  if (message.content == "-ping") {
    message.reply("Pong!")
  } else if (message.content == "-hello") {
    message.reply("Hello!")
  } else if (message.content == "-hello") {
    message.reply("Hello!")
  }
  
})



client.login(process.env['TOKEN'])