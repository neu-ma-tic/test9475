const Discord = require("discord.js");

module.exports = {
  name: "run",
  aliases: ["correr"],
  category: "Interaccion",
  description: "Correeeeeeee.",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
      var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/699752298296901662/c9adaa5c-d218-47b4-b734-80dcf735e6c3.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/541467280391929856/tenor.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      const user = message.mentions.members.first();
      if (!user) {
        let author = message.author.username;
        const embed = new Discord.MessageEmbed()
          .setDescription(`**${author}** está corriendo.`)
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      } else {
        let author = message.author.username;
        var rpt = [
          `**${author}** corre de **${message.mentions.users.first().username}**`,
          `**${author}** está corriendo de  **${
            message.mentions.users.first().username
          }**`,
        ];
        var mensaje = rpt[Math.floor(rpt.length * Math.random())];
        const embed = new Discord.MessageEmbed()
          .setDescription(`${mensaje}`)
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      }
  },
};