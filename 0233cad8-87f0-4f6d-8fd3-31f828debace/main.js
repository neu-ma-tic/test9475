const Discord = require('discord.js');
const client = new Discord.Client();
const fs = require('fs');

client.commands = new Discord.Collection();
client.events = new Discord.Collection();


['command_handler', 'event_handler'].forEach(handler =>{
    require(`./handlers/${handler}`)(client, Discord);

    client.on('guildMemberAdd', guildMember =>{
        let welcomeRole = guildMember.guild.roles.cache.find(role => role.name === 'Member');
    
        guildMember.roles.add(welcomeRole);
    })
    



})


client.login('ODY2ODc0MjM2NDQ5ODQ5Mzg1.YPY5iw.aJaT9Wc7z_DXQI11W5D_s_s35H0');