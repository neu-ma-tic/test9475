const { MessageEmbed } = require('discord.js')
module.exports = {
    name : "ticket-system",
    category : 'Ticket System',
    description : "Създава нов канал за комуникации между потребителя и екипа.",
    prefix : "!",

    /**
     * @param {Bot} bot
     * @param {Message} message
     * @param {String[]} args
     */

    run : async(client, message, args) => {
        const ticketsystemchannelId = config.TICKET_SYSTEM.supportChannelID
        const embed = new MessageEmbed()
            .setColor('#0099ff')
            .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
            .setTimestamp()
            .setTitle('Информация за системата за билети')
            .setDescription(`За да създадете билет, реагирайте с 📩 в ${client.channels.cache.get(ticketsystemchannelId).toString()}.`)
            await message.channel.send(embed)


    }
}