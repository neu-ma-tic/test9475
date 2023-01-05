const Discord = require("discord.js");

module.exports = {
  name: "kiss",
  aliases: ["besar"],
  category: "Interaccion",
  description: "Besa a alguien.",
  usage: "<usuario>",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/664504519572324384/63198070-51aa-4435-8b42-c8078768c9f8.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/601062382986330133/kiss.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      const user = message.mentions.members.first();
      let author = message.author.username;
      if (!user) return message.reply("Tienes que mencionar a alguien");
      if (message.author.id == message.mentions.users.first().id)
        return message.channel.send("¿te besarás a ti mismo? o.O");
      if (message.mentions.users.first().id == NatsumiID)
        return message.channel.send("n-no puedo hacerlo >u<");
      const embed = new Discord.MessageEmbed()
        .setDescription(
          `**${
            message.mentions.users.first().username
          }** ha recibido un beso de **${author}**`
        )
        .setColor(color)
        .setImage(url2)
        .setTimestamp();
        message.reply({ embeds: [embed] });
  },
};