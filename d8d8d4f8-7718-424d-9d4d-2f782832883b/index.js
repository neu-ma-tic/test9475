  
const Discord = require('discord.js');
const client = new Discord.Client({ partials: ["MESSAGE", "CHANNEL", "REACTION"]});

const prefix = '-';

const fs = require('fs');

client.commands = new Discord.Collection();

const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));
for(const file of commandFiles){
    const command = require(`./commands/${file}`);

    client.commands.set(command.name, command)
}

client.once('ready', () => {
	console.log('This bot is online!');
});

client.on('guildMemberAdd', guildMember =>{
    let welcomeRole = guildMember.guild.roles.cache.find(role => role.name === 'member');

    guildMember.roles.add(welcomeRole);
    guildMember.guild.channels.cache.get('641315807745277993').send(`Welcome <@${guildMember.user.id}> to our server! Make sure to check out the <#791405102396735528> text channel!`)
});

client.on('message', message =>{

    message.member.roles.cache.has
    if(!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();

    if(command === 'ping'){
        client.commands.get('ping').execute(message, args);
    } else if (command == 'youtube'){
        client.commands.get('youtube').execute(message, args, Discord);
    } else if (command == 'command'){
        client.commands.get('command').execute(message, args, Discord);
    } else if (command == 'clear'){
        client.commands.get('clear').execute(message, args);
    } else if (command == 'kick'){
        client.commands.get('kick').execute(message, args);
    } else if (command == 'ban'){
        client.commands.get('ban').execute(message, args);
    } else if (command =='mute'){
        client.commands.get('mute').execute(message, args);
    } else if (command =='unmute'){
        client.commands.get('unmute').execute(message, args);
    } else if (command =='reactionrole'){
        client.commands.get('reactionrole').execute(message, args, Discord, client);
    }
});

client.login('NzMxNjAxNjE1MDQzNDI4Mzcz.XwobGQ.USvbPU_HyybI4ITqtQ2BL26WYhQ');