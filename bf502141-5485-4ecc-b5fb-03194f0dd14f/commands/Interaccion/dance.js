const Discord = require("discord.js");

module.exports = {
  name: "dance",
  aliases: ["bailar"],
  category: "Interaccion",
  description: "Baila",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://media.discordapp.net/attachments/742623599558524941/747932197217894430/tenor_1.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/570373865008660540/chikadance5.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/644551801588154398/398757aeeeda71f41e82091fcf0496f3.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/570373874391449600/chikadance6.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = messages.author.username;
      const user = message.mentions.members.first();
      if (!user) {
        const embed = new Discord.MessageEmbed()
          .setDescription(`**${author}** se puso a bailar.`)
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      } else {
        const embed = new Discord.MessageEmbed()
          .setDescription(
            `**${
              message.mentions.users.first().username
            }**, parece que **${author}** quiere bailar contigo o.o`
          )
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      }
  },
};