const Discord = require('discord.js');

const Cryptr = require('cryptr');

module.exports = {
    name: "decrypt",
    description: "decrypts messages",

    async run(bot, message, args) {
        let user = message.author;
        
        if(args.length==0){
            message.reply('please enter the text you would like me to decrypt!');
        }
        else {
            async function decrypt(){
                try{
                    message.delete();
                    const cryptr = new Cryptr('myTotalySecretKey');
                    let stuffToDecrypt = Array.from(args).toString().split(',').join(' ');
                    const decryptedString = cryptr.decrypt(stuffToDecrypt);
                    console.log(decryptedString);

                    const embed = new Discord.MessageEmbed()
                    .setTitle('your decrypted text')
                    .setColor('#ff4267')
                    .setThumbnail('https://www.freeiconspng.com/thumbs/encryption-icon/encryption-icon-11.png')
                    .setDescription('```' + decryptedString + '```')
                    .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));

                    message.author.send(embed);

                    message.reply('**Message was decrypted successfully.**');

                } catch(error){
                    console.error(error);
                    message.reply('I do not decrypt strings using this kind of encryption method unfortunately.')
                    .then(message => {
                        message.react('🙁');
                    });
                }
            }
            decrypt();
        }
    }
}