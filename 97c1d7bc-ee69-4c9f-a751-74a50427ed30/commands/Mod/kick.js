const { MessageEmbed } = require('discord.js')

module.exports = {
    commands: 'kick', // You Can Keep Any Name
    description: 'Kicks A User.', // Optional 
    permissions: 'KICK_MEMBERS', // You Can Keep Any Permissions
    permissionError: 'Nemáte dostatečné permise na kick!',
    expectedArgs: '+Kick @User', // Optional

    callback: (message, args) => {
        message.delete()
        const member = message.mentions.members.first()
        if(!member) return message.reply('Musíte označit hráče ,kterému chcete udělit kick.') // Mention To Kick.
        .then(msg => {
            msg.delete({ timeout: 10000 });
        })
.catch();
        member.kick()
        message.delete()

        const embed = new MessageEmbed()
        .setTitle('Uživatel byl vyhozen')
        .setDescription(`<@${member.user.id}> Byl vyhozen.`)
        .addField('Uživatelem', message.author)
        .setColor('#313131')
        .setImage('https://c.tenor.com/wlkObO9mljwAAAAC/kicked-persona.gif')
        message.channel.send(embed)
    }
}