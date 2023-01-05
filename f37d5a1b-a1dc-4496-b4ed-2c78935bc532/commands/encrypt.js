const Discord = require('discord.js');

const Cryptr = require('cryptr');

module.exports = {
    name: "encrypt",
    description: "encrypts messages",

    async run(bot, message, args) {
        let user = message.author;
        
        if(args.length==0){
            message.reply('please enter the text you would like me to encrypt!');
        }
        else {
            message.delete();
            const cryptr = new Cryptr('myTotalySecretKey');
            let stuffToEncrypt = Array.from(args).toString().split(',').join(' ');
            const encryptedString = cryptr.encrypt(stuffToEncrypt);
            const decryptedString = cryptr.decrypt(encryptedString);
            console.log(encryptedString);
            console.log('decrypted: ' + decryptedString);

            const embed = new Discord.MessageEmbed()
            .setTitle('your encrypted text')
            .setColor('#ff4267')
            .setThumbnail('https://www.freeiconspng.com/thumbs/encryption-icon/encryption-icon-11.png')
            .setDescription('```' + encryptedString + '```')
            .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));

            message.author.send(embed);

            message.reply('**Message was encrypted successfully.**');
        }
    }
}