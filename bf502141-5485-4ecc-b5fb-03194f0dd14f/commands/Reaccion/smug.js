const Discord = require("discord.js");

module.exports = {
  name: "smug",
  aliases: [""],
  category: "Reaccion",
  description: "Engreído.",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/664076424411348992/14e462f8-22d5-4779-bb4d-675c9ce1a246.gif",
        "https://i.kym-cdn.com/photos/images/newsfeed/000/928/760/db8.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/564139289303056393/unnamed_4.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** está presumiendo.`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};