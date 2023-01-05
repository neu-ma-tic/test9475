const Discord = require("discord.js")

exports.run = async (client, message, args) => {

    var list = [
       'https://pa1.narvii.com/5939/782acffee3146d7cb23561cc6ba03a5af4aefa48_hq.gif',
       'https://i.pinimg.com/originals/2f/0f/82/2f0f82e4fb0dee8efd75bee975496eab.gif',
       'https://i.pinimg.com/originals/b6/e3/9e/b6e39e693be3968d212b0fe5754f85db.gif'
    ]
    var rand = list[Math.floor(Math.random() * list.length)];
let user = message.mentions.users.first() || client.users.cache.get(args[0]);
if (!user) {
return message.reply('lembre-se de mencionar um usuário válido para dar um tapa!');
}
let avatar = message.author.displayAvatarURL({format: "png"});
  const embed = new Discord.MessageEmbed()
        .setTitle('Tapa')
        .setColor('#000000')
        .setDescription(`${message.author} acaba de dar um tapa em ${user}`)
        .setImage(rand)
        .setTimestamp()
        .setThumbnail(avatar)
        .setFooter('Bily and Dark22')
        .setAuthor(message.author.tag, avatar);
  await message.channel.send(embed)
}