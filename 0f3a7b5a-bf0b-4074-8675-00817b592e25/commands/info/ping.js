const { MessageEmbed } = require('discord.js')
module.exports = {
    name : 'ping',
    category : 'info',
    description : 'Връща бързината на отговор и API пинг на бота',
    prefix : "!",

    /**
     * @param {Client} client
     * @param {Message} message
     * @param {String[]} args
     */

    run : async(client, message, args) => {
        const msg = await message.channel.send(`Pinging...`)
        const embed = new MessageEmbed()
            .setTitle('Pong!')
            .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
            .setTimestamp()
            .setDescription(`WebSocket ping is ${client.ws.ping}MS\nMessage edit ping is ${Math.floor(msg.createdAt - message.createdAt)}MS!`)
            .setColor('#0099ff')
            await message.channel.send(embed)
            msg.delete()

    }
}