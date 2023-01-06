const Discord = require('discord.js');
require('dotenv').config();
const client = new Discord.Client({ partials: ["MESSAGE",
 "CHANNEL", "REACTION"]});

const fs = require('fs');

const memberCounter = require('./counters/member-counter');

client.commands = new Discord.Collection();
client.event = new Discord.Collection();

['command_handler', 'event_handler'].forEach(handler => {
    require(`./handlers/${handler}`)(client, Discord)
})

memberCounter(client);

client.on('guildMemberAdd', guildMember => {
    let welcomeRole = guildMember.guild.roles.cache.get('811437686363389982');
 
    guildMember.roles.add(welcomeRole);
    const message = guildMember.guild.channels.cache.get('820387822879375360')
    const exampleEmbed = new Discord.MessageEmbed()
        .setColor('#0A6FD3')
        .setAuthor(guildMember.user.tag, guildMember.user.displayAvatarURL({ dynamic: true }))
        .setTitle(`${guildMember.user.tag} Joined.`)
        .setDescription(`𝘞𝘦𝘭𝘤𝘰𝘮𝘦 𝘵𝘰 **GxmingWithCxllum's Community Hub** 𝘠𝘰𝘶’𝘳𝘦 𝘵𝘩𝘦 ${guildMember.guild.memberCount} Member that joined.`)
        .setFooter(`Created by: @TheDrCallum_#9982`)
        .setImage('https://static-cdn.jtvnw.net/jtv_user_pictures/4f51ad4d-5fa7-4506-87b0-a06aebebbc35-profile_image-70x70.png')
        .setTimestamp()
        .addField(`Channels`, `• <#811384124068855838> - Agree to send messages.\n• <#811424487152418856> - More access to the server.\n• <#821580999577042964> - Need help.`)

        message.send(exampleEmbed)
    
})

client.on ("guildMemberRemove", guildMember => {
    const exampleEmbed = new Discord.MessageEmbed()
        .setColor('#d12d21')
        .setTitle(`Goodbye`)
        .addFields(
        { name: `Thanks for tuning in ${guildMember.user.tag}`, value: `It was fun while it lasted, hope to see you again soon!`}

        )

    guildMember.guild.channels.cache.get('820387822879375360').send(exampleEmbed);
})

const mySecret = process.env['token']
