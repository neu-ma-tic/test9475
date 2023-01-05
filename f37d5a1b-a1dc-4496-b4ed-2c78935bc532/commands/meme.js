const Discord = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
    name: "meme",
    description: "sends memes",

    async run(bot, message, args) {
        let status; 
        fetch('https://reddit-meme-api.herokuapp.com/')
            .then((res) => { 
               status = res.status; 
               return res.json() 
           })
            .then((meme) => {
                var user = message.author;
                console.log(meme);
                console.log(status);
                const embed = new Discord.MessageEmbed()
               .setColor('#ff4267')
               .setTitle(meme['title'])
               .setURL(meme['post_link'])
               .setImage(meme['url'])
               .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
                message.channel.send(embed);
            });
            //yay it finally works!
    }
}