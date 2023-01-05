const Discord = require("discord.js");

module.exports = {
  name: "bored",
  aliases: [""],
  category: "Reaccion",
  description: "Expresa que estas aburrido/a.",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/698943729276289055/image0.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/715638444793266288/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/659844219900526612/QuaintNeedyCapeghostfrog-size_restricted.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** Ser aburre mucho.`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};