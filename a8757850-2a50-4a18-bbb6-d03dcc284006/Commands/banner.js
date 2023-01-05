const Command = require("../Structres/Command.js");
const Discord = require('discord.js')

module.exports = new Command({
    name: "banner",
    description: "顯示使用者橫幅",
    aliases: [],
    permission: "SEND_MESSAGES",
    async run(message, args, client) {

        const embed = new Discord.MessageEmbed()
            .setTitle("使用者橫幅")
            .setAuthor(message.author.username,
                message.author.avatarURL({ dynamic: true }))
            .setThumbnail(message.author.avatarURL({ size: 2048, dynamic: true }))

            .setFields(
                {
                    name: "Bot Version",
                    value: "1.0.0",
                    inline: true
                },
                {
                    name: "Bot Name",
                    value: client.user.username,
                    inline: true
                }
            )

            


        message.reply({ embeds: [embed] })
    }
})