const { MessageEmbed } = require('discord.js');
const moment = require('moment');
let settings = require('../../assets/settings.json')

module.exports.run = async (client, member) => {

    if (member.partial) member = await member.fetch()
    if(member.user.bot) return;
    
    let welcomeChannel = member.guild.channels.cache.get(settings.welcome_ID);

    if(welcomeChannel) {
        let embed = new MessageEmbed()
            .setColor(client.colors.maincolor)
            .setThumbnail(member.user.displayAvatarURL({ dynamic: true }))
            .setDescription(`👋 Welcome ${member} to __**${member.guild.name}**__\n\nMake sure to check out the following channels! Enjoy your stay!\n\n▸ **Rules**  | <#${settings.rules_ID}>\n▸ **Info**  | <#${settings.info_ID}>\n▸ **Roles**  | <#${settings.roles_ID}>`)
        welcomeChannel.send({ embeds: [embed ]})
    }
    return;
}