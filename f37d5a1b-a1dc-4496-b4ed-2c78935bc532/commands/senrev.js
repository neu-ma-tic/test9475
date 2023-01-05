const Discord = require('discord.js');

module.exports = {
    name: "senrev",
    description: "reverses a sentence",

    async run(bot, message, args) {
        if(args.length==0){
            message.reply('Please mention the sentence you would like me to reverse!');
        }
        else {
            let word = Array.from(args).toString().split(',').join(' ');
            console.log('Word: ' + word);
            let reversedWord = '';
            for(var i = word.length - 1; i >= 0; i--)
            {
                reversedWord += word[i];
            }
            let finalReverse = reversedWord.split(',').join(' ');
            console.log('Reversed Word: ' + finalReverse);
            let user = message.author;
            let revEmbed = new Discord.MessageEmbed()
            .setTitle('Reversed Word')
            .setColor('#ff4267')
            .setDescription('```' + 'Reversed Word: ' + finalReverse + '```')
            .setThumbnail('https://thumbs.dreamstime.com/b/keyboard-icon-vector-sign-symbol-isolated-white-background-logo-concept-your-web-mobile-app-design-134067880.jpg')
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));

            message.channel.send(revEmbed);

            if(finalReverse==word){
                message.reply('Nice word 😏');
            }
        }
    }
}