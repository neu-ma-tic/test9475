const { MessageEmbed } = require('discord.js');

module.exports = {
    name: 'macos',
    category: 'macos',
    description: 'get latency',
    run: async (bot, message, args, config) => {


        const embed = new MessageEmbed()
            .setTitle(`Version de java 8 pour MACOS`)
            .setDescription(`https://javadl.oracle.com/webapps/download/AutoDL?BundleId=242051_3d5a2bb8f8d4428bbe94aed7ec7ae784`)
            .setColor(`FFA500`);
        message.channel.send(embed);

        message.delete();
    }
}