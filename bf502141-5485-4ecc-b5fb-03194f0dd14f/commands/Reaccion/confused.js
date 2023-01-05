const Discord = require("discord.js");

module.exports = {
  name: "confused",
  aliases: [""],
  category: "Reaccion",
  description: "Estas confundido.",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/608119519151521847/0a83428471cfe28ed541434addf9421b.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/656908484931092480/9042993c-f4da-420a-ae78-1043e5a60ba4.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/709989987633987604/b3181177dac21a998054ec31aab71e721f34cfc6_hq.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** No entiende nada.`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};