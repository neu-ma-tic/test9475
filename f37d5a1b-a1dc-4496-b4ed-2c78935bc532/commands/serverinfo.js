const Discord = require('discord.js');

module.exports = {
    name: "serverinfo",
    description: "gives server info",

    async run(bot, message, args) {
        let user = message.author;
        const { guild } = message;
        const icon = guild.iconURL();

        let infoEmbed = new Discord.MessageEmbed()
        .setColor('#ff4267')
        .setTitle('Server Information: ')
        .setThumbnail(icon)
        .addFields(
        { name: 'Server Name'   , value:  message.guild.name                       },
        { name: 'Server Owner'  , value:  message.guild.owner                      },  
        { name: 'Category Name' , value:  message.channel.parent                   },    
        { name: 'Channel Name'  , value:  message.channel.name                     },      
        { name: 'Bot Ping'      , value:  bot.ws.ping +  ' ms'          },
        )
        .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));

        if(message.guild.owner==null){
            infoEmbed = new Discord.MessageEmbed()
            .setColor('#ff4267')
            .setTitle('Server Information ')
            .setThumbnail(icon)
            .addFields(
            { name: 'Server Name'   , value:  message.guild.name                       },
            { name: 'Server Owner'  , value:  'Owner Not Found!'                     },  
            { name: 'Category Name' , value:  message.channel.parent                   },    
            { name: 'Channel Name'  , value:  message.channel.name                     },      
            { name: 'Bot Ping'      , value:  bot.ws.ping +  ' ms'          },
            )
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));

            message.channel.send(infoEmbed);
        }
        else {
            message.channel.send(infoEmbed);
        }
    }
}
