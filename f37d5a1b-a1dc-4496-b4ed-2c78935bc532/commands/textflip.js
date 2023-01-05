const Discord = require('discord.js');

const weky = require('weky');

module.exports = {
    name: "tf",
    description: "flips text",

    async run(bot, message, args) {
        if(args.length=='0'){
            message.reply('Please type the text that you would like me to flip');
        }
        else if((args.length)>0){
            let argumentsArray = Array.from(args);
            let user = message.author;
            let flipEmbed = new Discord.MessageEmbed()
            .setColor('#ff4267')
            .setTitle('Flipped Text: ')
            .setThumbnail('https://vividesigning.com/wp-content/uploads/2020/09/flip-text-effect-in-illustrator.jpg')
            .setDescription(weky.flip(argumentsArray.toString().split(',').join(' ')))
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));
            message.channel.send(flipEmbed);
        }
        else {
            message.reply('Error!');
        }
    }
}