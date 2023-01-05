const Discord = require('discord.js');

module.exports = {
    name: "dp",
    description: "sends dp of mentioned user",

    async run(bot, message, args) {
        let target = message.mentions.users.first();
        if(!target){
            target = message.author; 
        }
        let avatarURL = target.displayAvatarURL({
            size: 4096,
            dynamic: true
        });
        
        const displayEmbed = new Discord.MessageEmbed()
        .setTitle(target.username + "'s Avatar")
        .setURL(avatarURL)
        .setColor('#ff4267')
        .setImage(avatarURL)
        .setFooter("Requested By: " + message.author.tag, message.author.displayAvatarURL({ size: 4096, dynamic: true }));

        message.channel.send(displayEmbed);
    }
}