const express = require("express");
const app = express();

app.get("/", (req, res) =>{
  res.send("Hello world!")
});

app.listen(3000, () => {
  console.log("project is ready!")
});

const Discord = require('discord.js');

const client = new Discord.Client({ intents: ["GUILDS", "GUILD_MESSAGES"] }); 

const  prefix  = '.';

const fs = require('fs');

client.commands = new Discord.Collection();

const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('js'));
for(const file of commandFiles){
    const command = require(`./commands/${file}`);

    client.commands.set(command.name, command);
 }




client.once('ready', () => {
    console.log('Tracker. is online!');
});

client.on("ready", () => {
    client.user.setPresence({ activity: { name: "your mom"}, status: "dnd" })

})

client.on('message', message =>{
    if(!message.content.startsWith(prefix) || message.author.bot) return;
    
    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();

    if(command === 'mik'){
        client.commands.get('mik').execute(message, args);
    } else if (command === 'ping'){
        client.commands.get('ping').execute(message, args);
    } else if (command === 'marco'){
        client.commands.get('marco').execute(message, args);
    } else if (command === 'uwu'){
        client.commands.get('uwu').execute(message, args);
    } else if (command === 'sho'){
        client.commands.get('sho').execute(message, args);
    } else if(command === 'ily'){
        client.commands.get('ily').execute(message, args);
    }
    
});
client.login('OTQ1NzAxMjg5MDI1NzU3MjY2.YhT-9Q.oE-ET7cGD0osXeOXs185D_mPYdw');