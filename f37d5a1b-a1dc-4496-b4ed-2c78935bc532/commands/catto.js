const Discord = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
    name: "catto",
    description: "sends cute catto pics",

     async run(bot, message, args) {
        let status; 
        fetch('https://api.thecatapi.com/v1/images/search')
        .then((res) => { 
            status = res.status; 
            return res.json()
        })
        .then((catto) => {
            console.log(catto);
            console.log(status);
            var user = message.author;
            var imageUrl = catto['0']['url'];
            const embed = new Discord.MessageEmbed()
            .setColor('#ff4267')
            .setURL(imageUrl)
            .setTitle("here's your cute catto pic")
            .setImage(imageUrl)
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
            message.channel.send(embed);
        });
    }
}
