const Discord = require('discord.js');

module.exports = {
    name: "setnickname",
    description: "sets nicknames",

    async run(bot, message, args) {
        if(args.length==0){
            message.reply('Please mention a user!');
        }

        let target = message.mentions.users.first();
        if(target==undefined||target==null||target==' '){
            message.reply('Please mention a valid user!');
        }

        let member = message.guild.members.cache.get(target.id);

        let nickname;
        let argsString = Array.from(args).toString().split(',').join(' ');
        for(var i=0; i<=23; i++){
            if(argsString[i]==' '){
                nickname = argsString.substr((i+1), (argsString.length-(i+1)));
            }
        }

        if((target.id==bot.user.id)){
            message.reply('Who do you think you are?');
        }
        else if(!nickname||nickname==undefined||nickname==null){
            message.reply('Please mention a nickname!');
        }
        else {
            await member.setNickname(nickname)
            .then(() => {
                let user = message.author;
                const changeEmbed = new Discord.MessageEmbed()
                .setTitle('Nickname Changed ✅')
                .setColor('#ff4267')
                .setFooter("Requested By: " + user.tag, user.displayAvatarURL({size: 4096, dynamic: true }));

                message.channel.send(changeEmbed);
            })
            .catch(error => { 
                console.error(error); 
                message.reply('Error encountered!')
                .then(message => {
                    message.react('☠️');
                }); 
            });
            
        }
    }
}