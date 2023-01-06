const Discord = require('discord.js');
const config = require('../../config.json');

module.exports = {
    name: "invite",
    aliases: ["inv", "add"],
    category: "Others",
    description: "Pegue aqui seu convite para me adicionar ao seu servidor",
    example: `${config.Prefix}invite`,

    run: async (client, message, args) => {
        const embed = new Discord.MessageEmbed()
        .setTitle('Me adicione')
        .setDescription(`Me adicione no seu servidor : https://discord.com/api/oauth2/authorize?client_id=825382628713562182&permissions=8&scope=bot`)
        .setTimestamp()

        message.channel.send(embed)
    }
}