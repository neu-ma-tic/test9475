const Discord = require('discord.js');

const client = new Discord.Client();

const memberCounter = require('./counters/member-counter');

client.commands = new Discord.Collection();
client.events = new Discord.Collection();

['command_handler', 'event_handler'].forEach(handler => {
    require(`./handlers/${handler}`)(client, Discord)
})

client.login('ODQyMTQ4OTc5MjgxNjI1MTA5.YJxGWw.9u9NNThcUz-IlUVoxrG07onJWps');