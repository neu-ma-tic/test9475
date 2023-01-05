const Discord = require('discord.js');

module.exports = {
    name: "sendmsg",
    description: "sends msgs to mentioned users",

    async run(bot, message, args) {
        let target = message.mentions.users.first();
        let arguments = Array.from(args).toString().split(',').join(' ');
        
        let newstr;

        if(!target){
            message.reply('Please mention a valid user.');
        }
        else {
            if(target.id==message.author.id||target.id==bot.user.id){
                message.reply('You cannot send messages to yourself or to me.');
            }
            else {
                console.log(arguments);
                for(var i=0; i<=23; i++)
                {
                    if(arguments[i]==' ')
                    {
                        newstr = arguments.substr((i+1), (arguments.length-(i+1)));
                    }
                }
                console.log(newstr);

                if(newstr==undefined||newstr==null||newstr==''||newstr==' '){
                    message.reply('Please enter a valid message.');
                }
                else {
                    message.delete();
                    const msgEmbed = new Discord.MessageEmbed()
                    .setTitle('You have a message!')
                    .setColor('#ff4267')
                    .setDescription('***' + '"' + newstr + '"' + '***')
                    .setThumbnail('https://static.vecteezy.com/system/resources/previews/002/323/432/original/mail-icon-message-sms-email-flat-style-outline-symbol-free-vector.jpg')
                    .setFooter('Message Author: ' + message.author.username);

                    var user = bot.users.cache.get(target.id); 
                    user.send(msgEmbed)
                    .then(() => {
                        console.log('Message was successfully sent to ' + target.username + ' by ' + message.author.username);
                        message.reply('**Your message was successfully sent!**');
                    });
                }
            }
        }
    }
}