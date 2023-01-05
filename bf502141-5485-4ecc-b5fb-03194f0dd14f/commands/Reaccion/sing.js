const Discord = require("discord.js");

module.exports = {
  name: "sing",
  aliases: [""],
  category: "Reaccion",
  description: "canta",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
        var url = [
          "https://cdn.discordapp.com/attachments/399448944889036801/595823457225277446/tenor_3.gif",
          "https://cdn.discordapp.com/attachments/399448944889036801/656901092872814592/d5b97fc0-34eb-4367-9b0b-541adf9d6420.gif",
          "https://cdn.discordapp.com/attachments/399448944889036801/595823181827407903/f189cf296e54467abeb1bed6034402ab03e3c12b3acbc3e1c6bf41bfe7810cd6.gif",
        ];
        let url2 = url[Math.floor(url.length * Math.random())];
        let author = message.author.username;
        const embed = new Discord.MessageEmbed()
          .setDescription(`**${author}** está cantando`)
          .setColor(0xf7b4b4)
          .setImage(url2)
          .setTimestamp();
    
          message.channel.send({ embed });
  },
};