const Discord = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
    name: "gifsearch",
    description: "sends gifs as per search query",

    async run(bot, message, args) {
        if(args.length==0){
            message.reply('Please provide a search input!')
            .then(message => {
                message.react('😤');
            });
        }
        else {
            let status; 
            fetch('https://api.giphy.com/v1/gifs/search?api_key=YOUR-API-KEY&q=' + args + '&limit=50')
            .then((res) => { 
                status = res.status; 
                return res.json()
            })
            .then((giphy) => {
                console.log(giphy);
                console.log(status);

                let searchResults = giphy['pagination']['total_count'];
                let searchCount = giphy['pagination']['count'];
                if(searchResults=='0'||searchResults==0||searchResults==undefined||searchResults==null||searchCount=='0'||searchCount==0||searchCount==undefined||searchCount==null){
                    message.reply('unfortunately no results were found')
                    .then(message => {
                        message.react('☹️');
                    });
                }
                else {
                    var user = message.author;
                    let randnum = Math.floor(Math.random()*50);
                    console.log(randnum);
                    var imageUrl = giphy['data'][randnum]['images']['original']['url'];
                    const embed = new Discord.MessageEmbed()
                    .setColor('#ff4267')
                    .setURL(imageUrl)
                    .setTitle("here's the gif you searched for")
                    .setImage(imageUrl)
                    .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
                    message.channel.send(embed);
                }
            });
        }
    }
}