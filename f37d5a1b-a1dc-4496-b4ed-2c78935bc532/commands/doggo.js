const Discord = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
    name: "doggo",
    description: "sends cute doggo pics",

     async run(bot, message, args) {
        let status; 
        fetch('https://dog.ceo/api/breeds/image/random')
        .then((res) => { 
            status = res.status; 
            return res.json() 
        })
        .then((doggo) => {
            var user = message.author;
            console.log(doggo);
            console.log(status);
            var imageUrl = doggo.message;
            const embed = new Discord.MessageEmbed()
            .setURL(imageUrl)
            .setColor('#ff4267')
            .setTitle("here's your cute doggo pic")
            .setImage(imageUrl)
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
            message.channel.send(embed);
        });
    }
}