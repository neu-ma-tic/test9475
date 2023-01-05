const express = require("express")
const app = express()

app.get("/", (req, res) => {
    res.send("hello hell!")
})

app.listen(3000, () => {
    console.log("project is ready!")
})

const Discord = require('discord.js');
const client = new Discord.Client();
const prefix = 's!';
const fs = require('fs');
client.commands = new Discord.Collection();

const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));
for(const file of commandFiles){
    const command = require(`./commands/${file}`);

    client.commands.set(command.name, command);

}

/**
 * Client Events
 */
const actvs = [
  ".UNDERDEVELOPMENT.",
  "Developer By IFU",
  "SOUTHERN SKY",
  "discord.gg/zH3FnzdfgS"
];

client.on('ready', () => {
  console.log(`${client.user.username} ready!`);
  client.user.setActivity(actvs[Math.floor(Math.random() * (actvs.length - 1) + 1)]);
  setInterval(() => {
      client.user.setActivity(actvs[Math.floor(Math.random() * (actvs.length - 1) + 1)]);
  }, 10000);
});
client.on("warn", (info) => console.log(info));
client.on("error", console.error);

client.once('ready', () => {
    console.log('SOUTHERN SKY is online!');
});

client.on('message', message =>{
    if(!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();

    if(command === 'ping'){
        client.commands.get('ping').execute(message, args);
  } else if (command == 'play'){
      client.commands.get('play').execute(message, args);
  } else if (command == 'play'){
      client.commands.get('play').execute(message, args);
  } else if (command == 'muted'){
      client.commands.get('muted').execute(message, args);
  }    
});

client.login('Nzk1Mzg1MTk1NTAyMTA4Njkz.X_ImMA.8NDxjCRXC-0bBtMWpJ7L14LU14c')
