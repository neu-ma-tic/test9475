const Discord = require("discord.js");

module.exports = {
  name: "facepalm",
  aliases: [""],
  category: "Reaccion",
  description: "Facepaaaaaaalm",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/393558002726338561/464506153108373525/unnamed.gif",
        "https://cdn.discordapp.com/attachments/393558002726338561/464506153846439938/unnamed_2.gif",
        "https://cdn.discordapp.com/attachments/393558002726338561/464506152676491265/unnamed_1.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** se ha decepcionado...`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};