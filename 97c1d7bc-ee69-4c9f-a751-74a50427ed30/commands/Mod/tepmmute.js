const { MessageEmbed } = require('discord.js')
const ms = require('ms') // npm i ms

module.exports = {
    commands: ['tempmute', 'tempm'], // You Can Keep Any Name
    description: 'Temp Mutes A User.', // Optinal
    permissions: 'MANAGE_CHANNELS', // You Can Keep Any Permission
    permissionError: 'Nemáte dostatečné permisse na dočasné umlčení uživatele!',
    expectedArgs: '+tempmute @User', // Optinal

    callback: async(message, args) => {
        const member = message.mentions.members.first()
        const time = args[1]
        if(!member) return message.reply('Musíte označit hráče ,kterému chcete udělit timeout.')
        .then(msg => {
            msg.delete({ timeout: 10000 });
        })
.catch();
        member.roles.add('996797462574534657')
        if(!time) return message.reply('Musíte určit dobu trvání timeoutu!')
        .then(msg => {
            msg.delete({ timeout: 10000 });
        })
.catch();

        if(member.roles.cache.has('996797462574534657')) return message.reply('Uživatel ,již je Muted.') // If User Is Already muted.
        .then(msg => {
            msg.delete({ timeout: 10000 });
        })
.catch();
        await member.roles.add('996797462574534657')

        const embed = new MessageEmbed()
        .setTitle('Uživatel je umlčen')
        .setDescription(`<@${member.user.id}> Mute je na ${time}.`)
        .addField('Uživatelem', message.author)
        .setColor('#313131')
        .setImage('https://c.tenor.com/SJQEik5SpKAAAAAd/end.gif')
        message.channel.send(embed)

        // Remove  Muted Role After Time Is Finished.
        setTimeout(async () => {
            await member.roles.remove('996797462574534657')
            message.channel.send(`<@${member.user.id}> Is Unmuted After ${time} Of Mute.`)
        }, ms(time))
    } 
}