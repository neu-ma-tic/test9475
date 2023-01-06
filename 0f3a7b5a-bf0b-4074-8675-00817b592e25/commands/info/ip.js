const { MessageEmbed } = require('discord.js')
module.exports = {
    name : "ip",
    category : 'info',
    description : "Връща IP-то на #",
    prefix : "!",

    /**
     * @param {Bot} bot
     * @param {Message} message
     * @param {String[]} args
     */

    run : async(client, message, args) => {
        // message.channel.send("play-rp.moonlabs.studio")

        const embed = new MessageEmbed()
            .setTitle('Title')
            .setThumbnail('URL')
            .setTimestamp()
            .setDescription("**description**")
            .setColor('#0099ff')
            await message.channel.send(embed)
    }
}