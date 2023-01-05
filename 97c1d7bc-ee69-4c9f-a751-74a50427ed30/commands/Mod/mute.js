const { MessageEmbed } = require("discord.js")

module.exports = {
    commands: ['mute', 'm'], // You Can Keep Any Name
    description: 'Mutes A User.', // Optinal
    permissions: 'MANAGE_CHANNELS', // You Can Keep Any Permission
    permissionError: 'NMusíte označit hráče ,kterému chcete udělit mute', 
    expectedArgs: '+mute @User', // Optinal

    callback: (message, args) => {
        message.delete()
        const member = message.mentions.members.first()
        if(!member) return message.reply('Please Mention A User To Mute.')
        .then(msg => {
            msg.delete({ timeout: 10000 });
        })
.catch();
        member.roles.add('996797462574534657') // Add Mute Role to User
        if(member.roles.cache.has('996797462574534657')) return message.reply('Uživatel ,již je Muted.') // If User Is Already Muted.
        .then(msg => {
            msg.delete({ timeout: 10000 });
        })
.catch();
        message.delete()

        const embed = new MessageEmbed()
        .setTitle('Uživatel je Muted')
        .setDescription(`<@${member.user.id}> Byl umlčen.`)
        .addField('Uživatelem', message.author)
        .setColor('#313131')
        .setImage('https://c.tenor.com/SJQEik5SpKAAAAAd/end.gif')
        message.channel.send(embed)
    }
}