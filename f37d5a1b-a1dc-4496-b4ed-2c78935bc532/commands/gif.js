const Discord = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
    name: "gif",
    description: "sends gifs",

     async run(bot, message, args) {
        let status; 
        fetch('https://api.giphy.com/v1/gifs/random?api_key=YOUR-API-KEY')
        .then((res) => { 
            status = res.status; 
            return res.json()
        })
        .then((giphy) => {
            console.log(giphy);
            console.log(status);
            var user = message.author;
            var imageUrl = giphy['data']['images']['original']['url'];
            const embed = new Discord.MessageEmbed()
            .setColor('#ff4267')
            .setURL(imageUrl)
            .setTitle("here's your gif")
            .setImage(imageUrl)
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
            message.channel.send(embed);
        });
    }
}