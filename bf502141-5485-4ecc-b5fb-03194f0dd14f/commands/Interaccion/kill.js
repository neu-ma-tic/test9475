const Discord = require("discord.js");

module.exports = {
  name: "kill",
  aliases: ["matar"],
  category: "Interaccion",
  description: "Mata a alguien. D:",
  usage: "<usuario>",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/758840053316714508/758864371383402556/tenor.gif",
        "https://cdn.discordapp.com/attachments/758840053316714508/762750158031028224/source.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const user = message.mentions.members.first();
      if (!user) return message.reply("Tienes que mencionar a alguien");
      if (message.author.id == message.mentions.users.first().id)
        return message.channel.send("No hagas eso D:");
      if (message.mentions.users.first().id == client.id)
        return message.channel.send("N-no quiero morir...");
      const embed = new Discord.MessageEmbed()
        .setDescription(
          `**${author}** mató a **${message.mentions.users.first().username}**`
        )
        .setColor(color)
        .setImage(url2)
        .setTimestamp();
        message.reply({ embeds: [embed] });
  },
};