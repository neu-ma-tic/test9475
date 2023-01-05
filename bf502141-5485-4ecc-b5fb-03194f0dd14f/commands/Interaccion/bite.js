const Discord = require("discord.js");

module.exports = {
  name: "bite",
  aliases: ["morder"],
  category: "Interaccion",
  description: "Muerde al usuario mencionado",
  usage: "<usuario>",
  cooldown: 2,
  run: async (client, message, args, color) => {
    let author = message.author.username;
    const user = message.mentions.members.first();    if (!user)
    return message
      .reply("Tienes que mencionar a alguien")
      .then((m) => m.delete({ timeout: 5000 }));
    var url = [
      "https://cdn.discordapp.com/attachments/399448944889036801/659834490365149184/19b60975-71f6-4217-8159-8494d79fcfb4.gif",
      "https://cdn.discordapp.com/attachments/399448944889036801/659834318327382016/dc2.gif",
    ];
    let url2 = url[Math.floor(url.length * Math.random())];
    var rpt = [
      `**${author}** mordió a **${message.mentions.users.first().username}**`,
      `**${author}** piensa que **${
        message.mentions.users.first().username
      }** es comida O.o`,
    ];
    var mensaje = rpt[Math.floor(url.length * Math.random())];

    if (message.author.id == message.mentions.users.first().id)
      return message.channel.send("¿te vas a morder a ti mismo? o.O");
    const embed = new Discord.MessageEmbed()
      .setDescription(mensaje)
      .setColor(color)
      .setImage(url2)
      .setTimestamp();
      message.reply({ embeds: [embed] });
  },
};
