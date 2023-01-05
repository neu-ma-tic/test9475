const { MessageEmbed } = require('discord.js');

module.exports = {
    name: 'proposition',
    category: 'proposition',
    description: '',
    run: async (bot, message, args, config) => {


        if (!(message.channel.id === config.propositionChannelID)) {

            const embed = new MessageEmbed()
                .setTitle(`Mauvais channel !`)
                .setDescription(`Merci d'envoyer vos propositions dans <#${config.propositionChannelID}>`)
                .setFooter(config.footer)
                .setColor(`FFA500`);

            message.reply(embed).then(msg => msg.delete({ timeout: config.timeout }))
            message.delete();
            return;
        }


        const toSend = args.toString().split(",").join(" ");

        if (toSend.length <= 30) {


            const embed = new MessageEmbed()
                .setTitle(`Nombre de caractères insuffisant !`)
                .setDescription(`Minium 30 caractères.`)
                .setColor(`FFA500`);

            message.reply(embed).then(msg => msg.delete({ timeout: config.timeout }))
            return;
        }


        const embed = new MessageEmbed()
            .setTitle(`Proposition de ${message.author.username}`)
            .setDescription(`${toSend}`)
            .addField(`Débats`, `Merci de débattre des propositions dans <#${config.generalServeurChannelID}>`)
            
            .setColor(`FFA500`);

        message.channel.send(embed).then(message => {
            message.react(`577530406312869929`);
            message.react(`577530421521285151`);
        });

        message.delete();

    }
}