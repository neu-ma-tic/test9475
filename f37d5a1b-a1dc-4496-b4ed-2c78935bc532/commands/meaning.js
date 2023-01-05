const Discord = require('discord.js');

const Dictionary = require('oxford-dictionary');

const config = {
    app_id : 'ENTER-APP-ID',
    app_key : 'ENTER-APP-KEY',
    source_lang : 'ENTER-LANGUAGE'
};

const dict = new Dictionary(config);

module.exports = {
    name: "meaning",
    description: "gives dictionary meaning",

    async run(bot, message, args) {
        let word = Array.from(args).toString().split(',').join(' ');

        if(args.length==0){
            message.reply('Please enter a word.');
        }
        else {
            const lookup = dict.definitions(word);

            lookup.then(dictionary => {
                console.log(JSON.stringify(dictionary));

                let meaning = dictionary['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'];
                console.log(meaning);

                const dictEmbed = new Discord.MessageEmbed()
                .setColor('#ff4267')
                .setTitle('Meaning')
                .setDescription('***' + '"' + meaning + '"' + '***')
                .setThumbnail('https://thumbs.dreamstime.com/b/abc-book-icon-isolated-white-background-school-education-object-language-learning-dictionary-symbol-simple-cartoon-line-art-156729518.jpg')
                .setFooter("Requested By: " + message.author.tag, message.author.displayAvatarURL({ size: 4096, dynamic: true }));

                message.channel.send(dictEmbed);
            })
            .catch(error => {
                console.error(error);
                message.reply('No results were found unfortunately.')
                .then(message => {
                    message.react('🙁');
                });
            });
        }
    }
}