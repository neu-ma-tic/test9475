const Discord = require("discord.js")
const {Intents} = require("discord.js")

const Client = new Discord.Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MEMBERS, Intents.FLAGS.GUILD_MESSAGES, Intents.FLAGS.GUILD_VOICE_STATES, Intents.FLAGS.GUILD_MESSAGE_REACTIONS], partials: ["MESSAGE", "CHANNEL", "REACTION" ]})

const prefix = '-';

const fs = require('fs');


Client.commands = new Discord.Collection();

const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));
for(const file of commandFiles){
    const command = require(`./commands/${file}`);
    
    Client.commands.set(command.name, command);
}

Client.once('ready', () => {
    console.log('SixStarBot is online!');
});

Client.on('messageCreate', message =>{
   if(!message.content.startsWith(prefix) || message.author.bot) return;

   const args = message.content.slice(prefix.length).split(/ +/);
   const command = args.shift().toLowerCase();

   if(command == 'command'){
       Client.commands.get('command').execute(message, args, Discord);
    } else if (command == 'lame'){
        Client.commands.get('lame').execute(message, args);
    } else if (command == 'reactionrole'){
        Client.commands.get('reactionrole').execute(message, args, Discord, Client);
    } else if(command == 'ping'){
        Client.commands.get('ping').execute(message, args);

});
Client.login('TOKEN');
