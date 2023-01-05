const Discord = require("discord.js");

module.exports = {
  name: "hug",
  aliases: ["abrazo"],
  category: "Interaccion",
  description: "Con este comando puedes abrazar a alguien.",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/717887765567766580/desconocido.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/719774180207362048/19180666-0db6-484e-80ff-923a59e3e3d3.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/689268674535882754/69c9962c573362b73750cf3152b598ce.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/708686505320906762/ea72ec71-dec0-4931-9f12-876c84a164ac.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      const user = message.mentions.members.first();
      let author = message.author.username;
      if (!user)
        return message
          .reply("Tienes que mencionar a alguien")
          .then((m) => m.delete({ timeout: 5000 }));
      if (message.author.id == message.mentions.users.first().id)
        return message.channel
          .send("no puedes abrazarte a ti mismo. :c ")
          .then((m) => m.delete({ timeout: 5000 }));
      const embed = new Discord.MessageEmbed()
        .setDescription(
          `**${author}** abrazo a **${message.mentions.users.first().username}**`
        )
        .setColor(color)
        .setImage(url2)
        .setTimestamp();
        message.reply({ embeds: [embed] });
  },
};