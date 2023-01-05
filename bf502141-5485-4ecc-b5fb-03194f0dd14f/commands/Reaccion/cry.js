const Discord = require("discord.js");

module.exports = {
  name: "cry",
  aliases: [""],
  category: "Reaccion",
  description: "¿Por qué estas llorando?",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/716738621838852116/Que_sad_wey.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/697473340348039248/cfcb18a3eb4ebc28c5ddc3665c83c8824e2d24be_00.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/650318672321052682/8T101PL.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** ha dejado caer sus lágrimas...`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};