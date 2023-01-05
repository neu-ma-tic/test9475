const Discord = require('discord.js');

const WikiFakt = require('wikifakt');

module.exports = {
    name: "rf",
    description: "sends random facts",

    async run(bot, message, args) { 

        let user = message.author;
        WikiFakt.getRandomFact().then((fact) => {
            console.log("Random fact generated: " + fact);

            const embed = new Discord.MessageEmbed()
            .setTitle("did you know?")
            .setColor('#ff4267')
            .setThumbnail('https://thumbs.dreamstime.com/b/did-you-know-symbol-special-offer-question-sign-vector-speech-bubble-banner-interesting-facts-thought-dialogue-balloon-shape-203413038.jpg')
            .setDescription(fact)
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));

            message.channel.send(embed);
        });
    }
}