const { MessageEmbed } = require('discord.js')
module.exports = {
    name : 'invitelink',
    category : 'invitetracker',
    description : 'Връща реферал линк за покана на потребител или препращане.',
    prefix : "!",

    /**
    * @param {Bot} bot
    * @param {Message} message
    * @param {String[]} args
    */

    run : async(client, message, args) => {
      const { guild } = message

      guild.fetchInvites().then((invites) => {

        const userInvites = invites.array().filter(o => o.inviter.id === message.author.id);
        // var userReferral = `https://discord.gg/${userInvites}`;

        if (userInvites) {
          const Embed = new MessageEmbed()
          .setColor('#0099ff')
          .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
          .setTimestamp()
          .setTitle('Invite Link')
          .setDescription(`Хей <@${message.author.id}>, Твоят реферал линк е: \`${userInvites}\``)
        
        message.channel.send(Embed);
        } else {
          message.channel.createInvite({ 
            maxAge: 0, // maximum time for the invite, in milliseconds
            unique: true
             })
              .then(invite => {
                console.log(`Created an invite with a code of https://discord.gg/${invite.code}`)
                const Embed = new MessageEmbed()
                  .setColor('#0099ff')
                  .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
                  .setTimestamp()
                  .setTitle('Invite Link')
                  .setDescription(`Хей <@${message.author.id}>, Ето твоят Invite линк: ${invite}`)
                
                  message.channel.send(Embed);
              })
              .catch(error => {
                console.log(error)
                const Embed = new MessageEmbed()
                  .setColor('#0099ff')
                  .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
                  .setTimestamp()
                  .setTitle('Invite Link')
                  .setDescription(`Хей <@${message.author.id}>, Не успях да направя Invite линк, опитай отново!`)
                
                  message.channel.send(Embed);
              });         
        }
        

      })

    }
}