const Discord = require("discord.js")

module.exports = {
    name: "lock",
    alias: [],

    execute(client, message, args) {

        const everyone = message.guild.roles.cache.find(r => r.name === "@everyone")

        message.channel.permissionOverwrites.edit(everyone, { SEND_MESSAGES: false})

        message.channel.send({ content: "Se a bloqueado este canal correctamente." })

    }
}