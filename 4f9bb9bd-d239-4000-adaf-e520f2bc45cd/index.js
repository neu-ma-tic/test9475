const Discord = require("discord.js");
const fs = require("fs");
require("dotenv").config();

const token = process.env.token;
const { setCommands } = require("./commands/help.js")
const { prefix } = require("./config.js");

const client = new Discord.Client();
const commands = {};

// load commands
const commandFiles = fs.readdirSync("./commands").filter(file => file.endsWith(".js"));

for (const file of commandFiles) {
  const command = require(`./commands/${file}`);
  commands[command.name] = command;
}

setCommands(commands)

// login bot
client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.on("message", message => {
  if(!message.content.startsWith(prefix) || message.author.bot) return;

  const args = message.content.slice(prefix.length).trim().split(/ +/);
  const command = args.shift().toLowerCase();

  let cmd = commands[command];
  if(cmd)
    cmd.execute(message, args)
});

client.login(token);