const Discord = require('discord.js');

const disbut = require('discord-buttons');

var genEmbed;

module.exports = {
    name: "randnum",
    description: "generates a random number between 0-9",

     async run(bot, message, args) {
        let user = message.author;
        var randembed = new Discord.MessageEmbed()
        .setTitle('Random Number Generator')
        .setThumbnail('https://www.seekpng.com/png/detail/114-1144413_question-mark-png-image-transparent-white-question-mark.png')
        .setColor('#ff4267')
        .setDescription('Click on the button to generate random a number between 0-9')
        .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));

        var randbutton = new disbut.MessageButton()
            .setStyle('blurple')
            .setLabel('Generate')
            .setID('generate')
            .setDisabled(false);

        var disabledbutton = new disbut.MessageButton()
            .setStyle('blurple')
            .setLabel('Generate')
            .setID('generate')
            .setDisabled(true);

        message.channel.send('You want to generate a random number I see', { button: randbutton, embed: randembed });
        bot.on('clickButton', async (button) => {
            if(button.clicker.user.id == message.author.id){
                if (button.id == 'generate') {
                  button.defer();
                  randnumber = Math.floor(Math.random() * 10);
                }
                if (button.message.editable){
                    button.message.edit({
                        embed: genEmbed = new Discord.MessageEmbed()
                               .setTitle('Generated Number')
                               .setThumbnail('https://www.seekpng.com/png/detail/114-1144413_question-mark-png-image-transparent-white-question-mark.png')
                               .setColor('#ff4267')
                               .setDescription('```' + 'The number that you have generated is: ' + randnumber + '```')
                               .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true })),

                        button: disabledbutton
                    })
                }
            }
            else {return message.reply('Only the person who has started the command can interact using the button :/');}
        });
    }
}