const Discord = require('discord.js');

const disbut = require('discord-buttons');

module.exports = {
    name: "feedback",
    description: "allows users to send bot related feedback",

     async run(bot, message, args) {
        const feedbackButton = new disbut.MessageButton()
        .setStyle('url')
        .setLabel('Send Feedback')
        .setURL('USE-A-GOOGLE-FORMS-LINK-OR-SOMETHING');

        let user = message.author;
        
        const feedbackEmbed = new Discord.MessageEmbed()
        .setColor('#ff4267')
        .setTitle('Feedback')
        .setDescription('Click on the button below to send a feedback!')
        .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
        
        try
        {
            message.channel.send({embed: feedbackEmbed, button: feedbackButton});
        } 
        catch(error)
        {
            console.error(error);
        }
    }
}