const Discord = require("discord.js");

module.exports = {
  name: "cookie",
  aliases: ["galleta"],
  category: "Interaccion",
  description: "Regala galletitas a usuarios",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
      "https://images-ext-1.discordapp.net/external/WtWW2maDjhZOrqak4_pWpL1fMxsRtkI3fhGM03calUA/https/cdn.weebs.cl/images/nSXTZfMp.gif",
    ];
    let url2 = url[Math.floor(url.length * Math.random())];
    let author = message.author.username;
    const user = message.mentions.members.first();
    if (!user) {
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** se comio una galleta`)
        .setColor(color)
        .setImage(url2)
        .setTimestamp();
      message.reply({ embeds: [embed] });
    } else {
      message.channel.send(
        `**${
          message.mentions.users.first().username
        }**, has recibido una :cookie: de **${author}**.`
      );
    }
  },
};
