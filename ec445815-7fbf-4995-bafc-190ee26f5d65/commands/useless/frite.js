const { MessageEmbed } = require('discord.js');

module.exports = {
    name: 'frite',
    category: 'useless',
    description: 'frite',
    run: async (bot, message, args, config) => {



        const embed = new MessageEmbed()
            .setTitle(`Des frites pour ${message.author.username} !`)
            .setImage("http://www.twofatbellies.com/wp-content/uploads/2011/03/SLR-Feb-March-387.jpg")
            .setColor(`FFA500`);

        message.channel.send(embed).then(msg => msg.delete({ timeout: config.timeout }));

        message.delete();
    }
}