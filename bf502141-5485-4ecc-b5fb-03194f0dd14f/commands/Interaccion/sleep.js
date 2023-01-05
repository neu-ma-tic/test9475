const Discord = require("discord.js");

module.exports = {
  name: "sleep",
  aliases: ["dormir"],
  category: "Interaccion",
  description: "Duermes.",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/722410047791038594/23eb0f95-63e9-467f-9972-b2c731d1795b.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/573630233203310650/tenor.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      const user = message.mentions.members.first();
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** está durmiendo.`)
        .setColor(color)
        .setImage(url2)
        .setTimestamp();
  
        message.reply({ embeds: [embed] });
  },
};