const Discord = require("discord.js");

module.exports = {
  name: "slap",
  aliases: ["bofetada"],
  category: "Interaccion",
  description: "Abofetea a alguien que no te gusta... ¡Usa toda tu fuerza!",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    let url2 = url[Math.floor(url.length * Math.random())];
    var url = [
      "https://cdn.discordapp.com/attachments/399448944889036801/596763241766453248/love-lab-gif.gif",
      "https://cdn.discordapp.com/attachments/399448944889036801/591264924408479754/3cd47d7d79d0da15a7408fea69c8c64c.gif",
    ];
    const user = message.mentions.members.first();
    let author = message.author.username;
    if (!user) return message.reply("Tienes que mencionar a alguien");
    const embed = new Discord.MessageEmbed()
      .setDescription(
        `**${
            message.mentions.users.first().username
        }** ha recibido una bofetada de **${author}**`
      )
      .setColor(color)
      .setImage(url2)
      .setTimestamp();
      message.reply({ embeds: [embed] });
  },
};