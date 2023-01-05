const { MessageEmbed } = require("discord.js")

module.exports = {
    commands: ['unmute', 'um'], // You Can Keep ANy Name
    description: 'Unmutes A User.', // Optinal
    permissions: 'MANAGE_CHANNELS', // You Can Keep Any Permission
    permissionError: 'You Dont Have Perms To Mute Someone',
    expectedArgs: '+unmute @User', // Optinal

    callback: (message, args) => {
        message.delete()
        const member = message.mentions.members.first()
        if(!member) return message.reply('Please Mention A User To Mute.')
        .then(msg => {
            msg.delete({ timeout: 10000 });
        })
.catch();
        member.roles.remove('996797462574534657') // Removes Mute Role to User
        if(!member.roles.cache.has('996797462574534657')) return message.reply('User Is Already Unmuted.') // If User Is Already Unmuted.
        .then(msg => {
            msg.delete({ timeout: 10000 });
        })
.catch();

        const embed = new MessageEmbed()
        .setTitle('Uživatel je unmuted.')
        .setDescription(`<@${member.user.id}> Je momentálně odmlčen.`)
        .addField('Uživatelem', message.author)
        .setColor('#313131')
        message.channel.send(embed)
    }
}