const Discord = require("discord.js");

module.exports = {
  name: "boom",
  aliases: [""],
  category: "Reaccion",
  description: "BooM!",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/651487903998017536/35102faf-8640-4a47-bdf6-d32f1de870bc.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/550426150560595981/CapitalImpeccableKingfisher-size_restricted.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/550389012641349663/tenor.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      const embed = new Discord.MessageEmbed()
        .setDescription(`**¡BOOM!** .`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};