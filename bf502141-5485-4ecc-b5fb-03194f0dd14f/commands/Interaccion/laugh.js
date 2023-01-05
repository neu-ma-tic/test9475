const Discord = require("discord.js");

module.exports = {
  name: "laugh",
  aliases: ["reir"],
  category: "Interaccion",
  description: "Expresa que algo te causó gracia o te burlas de alguien.",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/615272530130763836/laugh11.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/615272494621917213/laugh9.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/650317867417337876/tumblr_ojj6neLV8B1vj5j9co1_500.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/594608754360713258/1542693744_e4e7550d5206aa77578bf68aac829580663c4f0a_hq.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      const user = message.mentions.members.first();
      let author = message.author.username;
      if (!user) {
        const embed = new Discord.MessageEmbed()
          .setDescription(`**${author}** está riendose.`)
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      } else {
        const embed = new Discord.MessageEmbed()
          .setDescription(
            `**${author}** se ríe de  **${message.mentions.users.first().username}**.`
          )
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      }
  },
};