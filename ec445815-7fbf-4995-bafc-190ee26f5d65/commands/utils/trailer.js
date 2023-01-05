const { MessageEmbed } = require('discord.js');

module.exports = {
    name: 'trailler',
    category: 'trailler',
    description: 'trailler',
    run: async (bot, message, args, config) => {

        const embed = new MessageEmbed()
            .setTitle(`Le trailler n'est pas encore disponible !`)
            .setDescription(`Une annonce sera faites lors de la sortie du trailler.`)
            .setFooter(config.footer)
            .setColor(`FFA500`);
        message.channel.send(embed);

        message.delete();
    }
}