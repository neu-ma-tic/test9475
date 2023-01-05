const Discord = require("discord.js");

module.exports = {
  name: "kickbutts",
  aliases: [""],
  category: "Interaccion",
  description: "Patea a un usuario.",
  usage: "[usuario]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/541474138569834506/unnamed.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      const user = message.mentions.members.first();
      if (!user) return message.reply("Tienes que mencionar a alguien");
      if (message.author.id == message.mentions.users.first().id)
        return message.channel.send(
          "no creo que te puedas patear a ti mismo, sería absurdo."
        );
      if (message.mentions.users.first().id == NatsumiID)
        return message.channel.send("N-no me hagas eso D:");
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(
          `**${author}** pateó a **${message.mentions.users.first().username}**`
        )
        .setColor(color)
        .setImage(url2)
        .setTimestamp();
        message.reply({ embeds: [embed] });
  },
};