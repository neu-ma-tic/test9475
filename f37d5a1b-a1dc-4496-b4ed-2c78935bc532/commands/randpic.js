const Discord = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
    name: "randpic",
    description: "sends randpic",

     async run(bot, message, args) {
        var user = message.author;
        let status; 
              fetch('https://api.unsplash.com/photos/random?client_id=ACCESS-KEY')
                    .then((res) => { 
                        status = res.status; 
                        return res.json()
                    })
                    .then((randpic) => {
                        console.log(randpic);
                        console.log(status);
                        var image = randpic['urls']['regular'];
                        let picEmbed = new Discord.MessageEmbed()
                        .setColor('#ff4267')
                        .setURL(image)
                        .setTitle('here is your random pic')
                        .setImage(image)
                        .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
                        message.channel.send(picEmbed);
                    })
    }
}