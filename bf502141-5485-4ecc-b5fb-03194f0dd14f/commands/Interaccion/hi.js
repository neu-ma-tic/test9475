const Discord = require("discord.js");

module.exports = {
  name: "hi",
  aliases: ["hola"],
  category: "Interaccion",
  description: "Saluda al servidor o a alguién en especifico.",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/596153280845840386/tenor_4.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/640233105260806174/tumblr_pngf9vVXzN1tm1dgio4_500.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/596153281294893087/3923f5e63b610771803e0d49a6283ecfb3430f56_00.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/719567461372002344/388cc0b4-c7a7-4b9c-baf6-07200357e039.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/596153392662052885/d5f1211e39769dac1af0bd316de32185715d356e_hq.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const user = message.mentions.members.first();
      if (!user) {
        const embed = new Discord.MessageEmbed()
          .setDescription(`**${author}** está saludando a todos.`)
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      } else {
        const embed = new Discord.MessageEmbed()
          .setDescription(
            `**${author}** saluda a **${message.mentions.users.first().username}**.`
          )
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      }
  },
};