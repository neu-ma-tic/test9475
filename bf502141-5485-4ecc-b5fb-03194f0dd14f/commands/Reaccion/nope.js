const Discord = require("discord.js");

module.exports = {
  name: "nope",
  aliases: [""],
  category: "Reaccion",
  description: "No te gusta.",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://pa1.narvii.com/5709/283cd338d17bccabdcffe4022200bce33de9a26f_hq.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/597190816024494100/jGYMqAy.gif",
        "https://i.kym-cdn.com/photos/images/original/001/087/918/e5c.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**NOPE!**`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};