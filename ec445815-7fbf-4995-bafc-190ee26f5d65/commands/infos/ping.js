const { MessageEmbed } = require('discord.js');

module.exports = {
    name: 'ping',
    category: 'info',
    description: 'get latency',
    run: async (bot, message, args, config) => {

        const msg = await message.channel.send(`ping en cours...`);

        const embed = new MessageEmbed()
            .setTitle(`Pong !`)
            .setDescription(`Latence du bot : ${Math.floor(new Date() - message.createdTimestamp)}MS \n Latence de l'API : ${Math.round(bot.ws.ping)}MS`)
            .setColor(`FFA500`);
        msg.edit(embed);

        message.delete();
    }
}