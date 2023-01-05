const Discord = require('discord.js');
require('dotenv').config();

const client = new Discord.Client({ partials: ["MESSAGE", "CHANNEL", "REACTION" ], intents: ["GUILDS", "GUILD_MESSAGES"]});

const memberCount = require('./counters/member-counter');

const prefix = ",";

const fs = require('fs');

client.commands = new Discord.Collection();
client.event = new Discord.Collection();

['command_handler', 'event_handler'].forEach(handler =>{
    require(`./handlers/${handler}`)(client, Discord);
});


client.login(process.env.TOKEN);
