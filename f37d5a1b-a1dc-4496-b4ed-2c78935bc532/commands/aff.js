const Discord = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
    name: "aff",
    description: "sends affirmation",

     async run(bot, message, args) {
        var user = message.author;
        let status; 
        fetch('https://www.affirmations.dev/')
        .then((res) => { 
            status = res.status; 
            return res.json()
        })
        .then((affirmation) => {
            console.log(status);
            console.log(affirmation);
            const embed = new Discord.MessageEmbed()
            .setColor('#ff4267')
            .setThumbnail('https://thumbs.dreamstime.com/b/affirmations-positive-statement-suitable-packaging-web-designs-advertising-products-label-hand-drawn-black-white-symbol-197709274.jpg')
            .setTitle("here's your affirmation")
            .setDescription(affirmation['affirmation'])
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
            message.channel.send(embed);
        });
    }
}