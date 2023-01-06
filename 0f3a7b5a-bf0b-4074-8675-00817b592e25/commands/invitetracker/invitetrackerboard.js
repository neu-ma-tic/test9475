const { MessageEmbed } = require('discord.js')
module.exports = {
    name : 'invitesboard',
    category : 'invitetracker',
    description : 'Връща ВСИЧКИ покани, сортирани по низходящ ред',
    prefix : "!",

    /**
    * @param {Bot} bot
    * @param {Message} message
    * @param {String[]} args
    */

    run : async(client, message, args) => {
      const { guild } = message

      guild.fetchInvites().then((invites) => {
        const inviteCounter = {

        }
  
        invites.forEach((invite) => {
          const { uses, inviter } = invite
          const { username, discriminator } = inviter
  
          const name = `${username}#${discriminator}`
  
          inviteCounter[name] = (inviteCounter[name] || 0) + uses
        })
  
        let replyText = ''
  
        const sortedInvites = Object.keys(inviteCounter).sort(
          (a, b) => inviteCounter[b] - inviteCounter[a]
        )
  
        sortedInvites.length = 10

        let i = 0
        for (const invite of sortedInvites) {
          i++
          const count = inviteCounter[invite]
          if (invite == null || count == null) {
            replyText += `**${i}**: \`Празно!\`\n ` // decide here 2 spaces or 1 /n /n
          } else {
            replyText += `**${i}**: \`${invite}\` е поканил **${count}** космонавт/а!\n ` // decide here 2 spaces or 1 /n /n
          }
         
        }
        // message.reply(replyText)

        const Embed = new MessageEmbed()
          .setColor('#0099ff')
          .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
          .setTimestamp()
          .setTitle('Top 10 Табло за Покани')
          .setDescription(replyText)
        
        message.channel.send(Embed);

      })

    }
}