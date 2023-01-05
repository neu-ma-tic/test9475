const Discord = require("discord.js");

module.exports = {
  name: "sip",
  aliases: [""],
  category: "Reaccion",
  description: "toma algo",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/579116795059765265/is-the-order-a-rabbit-01.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/615268654677753926/sip3.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/579117803366383636/849f3962b7b13c8e1bd0f250575c03c044fcbfc7_hq.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`Parece que **${author}** andaba con mucha sed...`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};