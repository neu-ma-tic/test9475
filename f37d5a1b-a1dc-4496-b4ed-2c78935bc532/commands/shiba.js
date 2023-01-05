const Discord = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
    name: "shiba",
    description: "sends cute shiba inu pics",

     async run(bot, message, args) {
        var user = message.author;
        let status; 
        fetch('http://shibe.online/api/shibes?count=[1]')
        .then((res) => { 
            status = res.status; 
            return res.json()
        })
        .then((shiba) => {
            console.log(shiba);
            console.log(status);
            var image = shiba['0'];
            let shibaEmbed = new Discord.MessageEmbed()
            .setColor('#ff4267')
            .setURL(image)
            .setTitle("here's your cute shiba-inu pic")
            .setImage(image)
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
            message.channel.send(shibaEmbed);
        });
    }
}