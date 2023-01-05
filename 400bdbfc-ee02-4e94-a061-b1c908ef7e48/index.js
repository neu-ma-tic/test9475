const Discord = require("discord.js")
const client = new Discord.Client({partials: ["MESSAGE","CHANNEL","REACTION"]})
const prefix = '-'


client.commands = new Discord.Collection();
client.events = new Discord.Collection();

['command_handler'].forEach(handler =>{require(`./handlers/${handler}`)(client, Discord);
})


client.login("OTEyMzg4NDkwNTg1NjAwMDIx.YZvN_w.plCG2rS_AnkfRF496fbrJurPgmk")