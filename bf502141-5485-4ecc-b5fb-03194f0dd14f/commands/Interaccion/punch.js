const Discord = require("discord.js");

module.exports = {
  name: "punch",
  aliases: ["golpear"],
  category: "Interaccion",
  description: "Golpea a alguien. D:",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/711618898130370641/20200517_112437_1.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/597190734302412810/f3a.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      const user = message.mentions.members.first();
      let author = message.author.username;
      if (!user) return message.reply("Tienes que mencionar a alguien");
      if (message.author.id == message.mentions.users.first().id)
        return message.channel.send("no creo que te puedas golpear a ti mismo.");
      if (message.mentions.users.first().id == NatsumiID)
        return message.channel.send("N-no me hagas eso D:");
      const embed = new Discord.MessageEmbed()
        .setDescription(
          `**${author}** golpeá a **${message.mentions.users.first().username}**`
        )
        .setColor(color)
        .setImage(url2)
        .setTimestamp();
        message.reply({ embeds: [embed] });
  },
};