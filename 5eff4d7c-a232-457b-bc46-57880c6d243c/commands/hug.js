const Discord = require('discord.js');

exports.run = async (client, message, args) => {

var list = [
  'https://i.pinimg.com/originals/6e/6e/53/6e6e53fb69d7b74286c9d2817e1fc3ca.gif',
  'https://acegif.com/wp-content/uploads/anime-hug.gif',
  'https://i.pinimg.com/originals/32/09/15/320915992153abde2070a076552344e7.gif'
];

var rand = list[Math.floor(Math.random() * list.length)];
let user = message.mentions.users.first() || client.users.cache.get(args[0]);
if (!user) {
return message.reply('lembre-se de mencionar um usuário válido para abraçar!');
}
/*
message.channel.send(`${message.author.username} **acaba de beijar** ${user.username}! :heart:`, {files: [rand]});
*/
let avatar = message.author.displayAvatarURL({format: "png"});
  const embed = new Discord.MessageEmbed()
        .setTitle('Hug')
        .setColor('#000000')
        .setDescription(`${message.author} acaba de abraçar ${user}`)
        .setImage(rand)
        .setTimestamp()
        .setThumbnail(avatar)
        .setFooter('Bily and Dark22')
        .setAuthor(message.author.tag, avatar);
  await message.channel.send(embed);
}