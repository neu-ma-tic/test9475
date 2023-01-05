const Discord = require("discord.js");

module.exports = {
  name: "game",
  aliases: [""],
  category: "Reaccion",
  description: "Estas jugando",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/694005107083313252/701490847333482627/19.gif",
        "https://cdn.discordapp.com/attachments/694005107083313252/701490701367771166/7.gif",
        "https://cdn.discordapp.com/attachments/694005107083313252/701490642525749288/10.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${authorcanvas}** está jugando algo divertido.`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};