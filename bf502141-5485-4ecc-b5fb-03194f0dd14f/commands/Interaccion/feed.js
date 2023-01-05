const Discord = require("discord.js");

module.exports = {
  name: "feed",
  aliases: ["comer"],
  category: "Interaccion",
  description: "Dale de comer a un usuario, o deja que yo te dé de comer. n.n",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/714431554486665236/anime-cute-gif-4.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/698947614728650832/fcd4180c-5ca8-4014-a022-98ce1c2e386e.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/698947499255398450/848fb821-d633-4319-be36-936ca2cddf8f.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const user = message.mentions.members.first();
      if (!user) {
        const embed = new Discord.MessageEmbed()
          .setDescription(`**${author}** está comiendo.`)
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      } else {
        const embed = new Discord.MessageEmbed()
          .setDescription(
            `**${author}**le da de comer a**${
                message.mentions.users.first().username
            }**.`
          )
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      }
  },
};