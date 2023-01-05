const { MessageEmbed } = require('discord.js')
const moment = require('moment') // npm i moment
moment.locale('ENG')

module.exports ={
    commands: ['userinfo', 'user-info', 'ui', 'memberinfo', 'member-info', 'mi'], 
    permissions: 'ADMINISTRATOR', // You Can Keep Any Permissions
    permissionError: 'Nemáte dostatečné permise na udělení banu!',
    description: 'Shows User Info About A User or Pinged User.', // Optional

    callback: (message, args) => {

        const member = message.mentions.members.first() || message.member
        // For Status Of User, We Will Use Emoji To Look Nice
        const status = {
            online: '🟢:- Online',
            idle: '🟡:- Idle',
            dnd: '🔴:- DND',
            offline: '⚫:- Offline'
        }

        const embed = new MessageEmbed()
        .setColor('#313131')
        .setTitle(`User Info Of ${member.user.username}`, member.user.displayAvatarURL())
        .setThumbnail(member.user.displayAvatarURL({dynamic: true, size: 512}))
        .addField('⚫ **User-Name**', `${member.user.username}#${member.user.discriminator}`) // We Use Emojis Also
        .addField('⚫ **User ID**', `${member.id}`)
        .addField('⚫ **Account Created**', `${moment.utc(member.user.createdAt).format('LLLL')}`)
        .addField('⚫ **Joined Server**', `${moment.utc(member.joinedAt).format('LLLL')}`)
        .addField('⚫ **VC**', member.voice.channel ? member.voice.channel.name + `(${member.voice.channel.id})` : 'Not In A VC')
        .addField('⚫ **Roles**', `${member.roles.cache.map(role => role.toString())}`, true)
        // Add More Fields If Want
        message.channel.send(embed)
    }
}
