const Discord = require("discord.js");

module.exports.run = async (client, message, args) => {

  const embed = new Discord.MessageEmbed()
    .setTitle(`**Upvote Discord Bot List**`)
    .setThumbnail("https://images.discordapp.net/avatars/705455105339818034/994cccf3c0dbed18a86b3d401a1c4922.png?size=512")
    .setColor("#FF0000")
    .setDescription(`Ajude meu criador dando upvote em mim, não custa nada, é grátis.
    
    https://top.gg/bot/705455105339818034/vote`)
    .setImage("https://i.imgur.com/L9RDO7y.gif")
    .setTimestamp()

  message.channel.send(embed);
};