const Discord = require('discord.js');

module.exports = {
    name: "gifhelp",
    description: "sends gif related help",

     async run(bot, message, args) {
        var user = message.author;
        let gifhelpEmbed = new Discord.MessageEmbed()
        .setColor('#ff4267')
        .setTitle('GIF Commands')
        .addFields(
        { name: '1) Random GIF' ,  value:  "+gif"                   },
        { name: '2) GIF Search'  ,  value:  "+gifsearch"      }
        )
        .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
        message.channel.send(gifhelpEmbed);
    }
}