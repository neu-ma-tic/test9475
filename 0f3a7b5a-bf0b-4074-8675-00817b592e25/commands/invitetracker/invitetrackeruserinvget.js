const { MessageEmbed } = require('discord.js')
module.exports = {
    name : 'invitesget',
    category : 'invitetracker',
    description : 'Връща конкретните покани, които потребителят е направил до момента.',
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
        var userInviteCount = 0;

        for(var i=0; i < userInvites.length; i++)
        {
            var invite = userInvites[i];
            userInviteCount += invite['uses'];
        }

        const Embed = new MessageEmbed()
          .setColor('#0099ff')
          .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
          .setTimestamp()
          .setTitle('Табло за Покани')
          .setDescription(`Хей <@${message.author.id}>, Ти имаш ${userInviteCount} Покани!`)
        
        message.channel.send(Embed);

      })

    }
}