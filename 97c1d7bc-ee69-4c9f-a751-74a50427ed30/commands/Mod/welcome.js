const { MessageEmbed } = require("discord.js")

module.exports = (client) => {
    const welcomechannelId = '996142451616141383'
    const targetChannelId = `996142452488556564` //Channel For Rules

    client.on('guildMemberAdd', (member) => {
        console.log(member)
        const channel = member.guild.channels.cache.get(welcomechannelId)

        const embed = new MessageEmbed()
        .setTitle(``)
        .setThumbnail(member.user.displayAvatarURL({dynamic: true, size: 512}))
        .setDescription(`Vítej u nás, <@${member.user.id}>!\n\nPřečti si prosím ${member.guild.channels.cache.get(targetChannelId).toString()} a dodržuj je.\nPřijď si s náma povídat do <#996142473434898432>`)
        .setFooter('twitch.tv/tiltlive')
        .setColor('#313131')
    channel.send(embed)
        
  })
}