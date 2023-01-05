const Discord = require("discord.js");

module.exports = {
  name: "disgust",
  aliases: [""],
  category: "Reaccion",
  description: "¿Estas disgustado?",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
        var url = [
          "https://media.discordapp.net/attachments/399448944889036801/518918137220038673/1504176020_perv.gif?width=400&height=225",
          "https://media.discordapp.net/attachments/399448944889036801/518917912493293568/tenor.gif?width=400&height=225",
          "https://cdn.discordapp.com/attachments/399448944889036801/601061564212183060/disgust.gif",
        ];
        let url2 = url[Math.floor(url.length * Math.random())];
        let author = message.author.username;
        const embed = new Discord.MessageEmbed()
          .setDescription(`**${author}** se ha disgustado de eso`)
          .setColor(0xf7b4b4)
          .setImage(url2)
          .setTimestamp();
    
          message.channel.send({ embed });
  },
};