const express = require("express");
const app = express();
const Discord = require('discord.js');
const bot = new Discord.Client();
const token = "NzA1MTM3MjY3NDQxOTI2MzE3.XqnUQQ.gXcIgiuRES5ENsIb3C5CFhT0VKU";
const PREFIX = "%";
 
const fs = require('fs');
bot.commands = new Discord.Collection();
 
const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));
for(const file of commandFiles){
    const command = require(`./commands/${file}`);
 
    bot.commands.set(command.name, command);
}

app.get("/", (req, res) =>{
  res.send("Cutebot is working.")
})
 
bot.on('ready', () => {
    console.log("cutebot is online");
});

bot.on("message", async message => {
  if (message.channel.type === "dm") return;
  if (message.author.bot) return;
  if (!message.guild) return;
  if (!message.member)
    message.member = await message.guild.fetchMember(message);

  if (!message.content.startsWith(PREFIX)) return;

  const args = message.content
    .slice(PREFIX.length)
    .trim()
    .split(" ");
  const cmd = args.shift().toLowerCase();

  bot.categories = fs.readdirSync("./commands/")
  ["command"].forEach(handler => {
    require(`./handler/${handler}`(client));
  });
 
bot.on("ready", () => {
  bot.user.setPresence ({ activity: {name: "Bot by Inceptn#0001 %help"}})
})
bot.login(token);