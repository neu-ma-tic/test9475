const { Message, MessageFlags } = require("discord.js");
const { MessageEmbed } = require('discord.js')

module.exports = {
    commands: ['ping'],
    permissions: 'ADMINISTRATOR',
    callback: (message, arguments, text, client) => {
        message.delete()
        message.channel.send('Loading...').then(resultMessage => {
            const ping = resultMessage.createdTimestamp - message.createdTimestamp

            resultMessage.edit(`Loading...`)
            . then(msg => {
                msg. delete({ timeout: -1 /*time unitl delete in milliseconds*/});
                })
            const embed = new MessageEmbed()
            .setColor('#313131')
            .setTitle(``)
            .addFields(
                { name: '🗡️︱Latence Otce', value: `${client.ws.ping}ms`, inline: true },
                { name: '🗡️︱Tvůj Ping:', value: `${ping}ms`, inline: true },
              )  
            .setFooter('twitch.tv/tiltlive')
            
            message.channel.send(embed)
        })
    },
}
