const Discord = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
    name: "picsearch",
    description: "sends a pic",

     async run(bot, message, args) {
        var user = message.author;
        if(args.length==0){
            message.reply('Please mention an image you would like me to search for.');
        }
        else {
            let status; 
                  fetch('https://api.unsplash.com/photos/random?client_id=ACCESS-KEY&query=' + args)
                        .then((res) => { 
                            status = res.status; 
                            return res.json()
                        })
                        .then((searchpic) => {
                            console.log(searchpic);
                            console.log(status);
                            var image = searchpic['urls']['regular'];
                            let picEmbed = new Discord.MessageEmbed()
                            .setColor('#ff4267')
                            .setURL(image)
                            .setTitle('here is your pic')
                            .setImage(image)
                            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
                            message.channel.send(picEmbed);
                        });
        }
    }
}