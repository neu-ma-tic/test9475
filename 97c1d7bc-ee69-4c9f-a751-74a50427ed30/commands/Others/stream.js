const { MessageEmbed } = require('discord.js')
const moment = require('moment') // npm i moment
moment.locale('ENG')

module.exports ={
    commands: ['stream'], 
    permissions: 'ADMINISTRATOR', // You Can Keep Any Permissions

    callback: (message, args) => {

        message.delete()
        message.channel.send('||@everyone||')

        const embed = new MessageEmbed()
        .setColor('#313131')
        .setTitle(`LiveStream`)
        .setDescription("Tilt is live on twitch!\n\n\[Watch Stream](https://twitch.tv/isnottilt)")
        .setImage('https://cdn.discordapp.com/attachments/996142457286824108/996460764896440440/Screenshot_18.png')
        .setFooter('twitch.tv/isnottilt')
        // Add More Fields If Want
        message.channel.send(embed)
    }
}
