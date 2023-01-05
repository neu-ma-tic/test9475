const Discord = require("discord.js");

module.exports = {
  name: "vomit",
  aliases: [""],
  category: "Reaccion",
  description: "Vomita",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/541472143481765888/unnamed_12.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/541472145805410360/unnamed_13.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/541472204886638602/unnamed_5.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** no pudo contenerse y vomitó`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};