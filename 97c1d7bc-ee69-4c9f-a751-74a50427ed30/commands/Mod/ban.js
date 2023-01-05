const { MessageEmbed } = require('discord.js')

module.exports = {
    commands: 'ban', // You Can Keep Any Name
    description: 'Bans A User.', // Optional 
    permissions: 'BAN_MEMBERS', // You Can Keep Any Permissions
    permissionError: 'Nemáte dostatečné permise na udělení banu!',
    expectedArgs: '+ban @User', // Optional

    callback: (message, args) => {
        message.delete()
        const member = message.mentions.members.first()
        if(!member) return message.reply('Musíte označit hráče ,kterému chcete udělit ban.')
        .then(msg => {
            msg.delete({ timeout: 10000 });
        })
.catch();
        member.ban()

        const embed = new MessageEmbed()
        .setTitle('Uživatel byl Zabanovaný')
        .setDescription(`<@${member.user.id}> Byl zabanován.`)
        .addField('Uživatelem', message.author)
        .setColor('#313131')
        .setImage('https://c.tenor.com/u53w---Rf9EAAAAM/when-your-team-too-good-ban.gif')
        message.channel.send(embed)
    }
}
