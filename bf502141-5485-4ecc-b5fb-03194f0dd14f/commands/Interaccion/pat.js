const Discord = require("discord.js");

module.exports = {
  name: "pat",
  aliases: ["..."],
  category: "Interaccion",
  description: "Acaricia a alguien del servidor.",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/698947637851717743/7c999f2c-98f8-4b0d-a9e4-2bf114caf8f9.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/662984154341965825/27baa0fed882b3b494f832c21bb5492e.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/628658545570873344/pat2.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/628658584116264960/pat7.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      const user = message.mentions.members.first();
      let author = message.author.username;
      if (!user) return message.reply("Tienes que mencionar a alguien");
      if (message.author.id == message.mentions.users.first().id)
        return message.channel.send("No puedes acariciarte a ti mismo :C");
      const embed = new Discord.MessageEmbed()
        .setDescription(
          `**${author}** acaricia a **${message.mentions.users.first().username}**`
        )
        .setColor(color)
        .setImage(url2)
        .setTimestamp();
        message.reply({ embeds: [embed] });
  },
};