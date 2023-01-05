const Discord = require("discord.js");

module.exports = {
  name: "blush",
  aliases: [""],
  category: "Reaccion",
  description: "Te sonrojas.",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/615280157246095470/7296895b-6a3a-49b7-ac0d-69b8c72fcc73.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/600528806733676545/454f4feec7fb8b447d4c3763d39f5ee6938a88da_00.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/564139779520987146/unnamed_1.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** se ha sonrojado.`)
        .setColor(color)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};