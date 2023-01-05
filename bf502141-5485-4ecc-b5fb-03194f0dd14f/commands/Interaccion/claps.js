const Discord = require("discord.js");

module.exports = {
  name: "claps",
  aliases: ["aplaudir"],
  category: "Interaccion",
  description: "Aplaude de algo o aplaude a alguien.",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/702884057578602617/47a5495f775c6b673ade2484869d9ae2.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/576925143188635668/unnamed_10.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/596164319494799370/dc6n3aa-aa554e6e-7ea6-43ad-966f-7814b8ff91e9.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/576914174668439563/unnamed_1.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const user = message.mentions.members.first();
      if (!user) {
        const embed = new Discord.MessageEmbed()
          .setDescription(`**${author}** está aplaudiendo.`)
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.channel.send({ embed });
      } else {
        const embed = new Discord.MessageEmbed()
          .setDescription(
            `**${author}** felicita a **${message.mentions.users.first().username}**`
          )
          .setColor(color)
          .setImage(url2)
          .setTimestamp();
          message.reply({ embeds: [embed] });
      }
  },
};