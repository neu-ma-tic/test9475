const Discord = require('discord.js');

exports.run = async (client, message, args) => {

var list = [
  'https://i.pinimg.com/originals/be/1f/d3/be1fd3b9ce4580bb31cb376eccf5e315.gif',
  'https://i.imgur.com/d06TkOU.gif'
];

var rand = list[Math.floor(Math.random() * list.length)];
let user = message.mentions.users.first() || client.users.cache.get(args[0]);
if (!user) {
return message.reply('Escolha um usuário válido para casar !');
}
/*
message.channel.send(`${message.author.username} **acaba de beijar** ${user.username}! :heart:`, {files: [rand]});
*/
let avatar = message.author.displayAvatarURL({format: 'png'});
  const embed = new Discord.MessageEmbed()
        .setTitle('Casamento ! ')
        .setColor('#ffe4e1')
        .setDescription(`${message.author} Acaba de se casar com ${user}`)
        .setImage(rand)
        .setTimestamp()
        .setThumbnail(avatar)
        .setFooter('Aaaaaa, eu sempre soube que vocês formavam um lindo casal ! 💜')
        .setAuthor(message.author.tag, avatar);
  await message.channel.send(embed);
}