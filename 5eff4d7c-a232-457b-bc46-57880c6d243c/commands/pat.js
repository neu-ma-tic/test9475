const Discord = require("discord.js")

exports.run = async (client, message, args) => {

    var list = [
       'https://pa1.narvii.com/6664/725dc89e753464fef940ea554e999b5bdcdb1c45_hq.gif',
       'https://68.media.tumblr.com/3ade742e12f149eb3cb80ce670755d95/tumblr_mqr4z6eAcI1r2nulro1_500.gif',
       'https://pa1.narvii.com/6723/a62c58fa264cb92a3ba5b2f50446a0541307e528_hq.gif'
    ]
    var rand = list[Math.floor(Math.random() * list.length)];
let user = message.mentions.users.first() || client.users.cache.get(args[0]);
if (!user) {
return message.reply('lembre-se de mencionar um usuário válido para fazer cafuné!');
}
let avatar = message.author.displayAvatarURL({format: "png"});
  const embed = new Discord.MessageEmbed()
        .setTitle('Cafuné')
        .setColor('#000000')
        .setDescription(`${message.author} acaba de fazer cafuné em ${user}`)
        .setImage(rand)
        .setTimestamp()
        .setThumbnail(avatar)
        .setFooter('Bily and Dark22')
        .setAuthor(message.author.tag, avatar);
  await message.channel.send(embed);
}