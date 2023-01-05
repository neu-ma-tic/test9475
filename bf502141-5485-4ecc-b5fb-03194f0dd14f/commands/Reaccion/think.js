const Discord = require("discord.js");

module.exports = {
  name: "think",
  aliases: [""],
  category: "Reaccion",
  description: "Piensa",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/734827870161076264/c0a7c479f149011b88fe3df460d01e95.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/575804921111379968/large.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/615264368937926656/think6.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** se puso a pensar. Hmm...`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};