const Discord = require("discord.js");

module.exports = {
  name: "pout",
  aliases: [""],
  category: "Reaccion",
  description: "Haces puchero.",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/701454589261512744/97d9b111-2796-429a-863e-86b252bffbdd.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/564137951504629781/unnamed_9.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/692934907608957018/Anime-Tsuujou-kougeki-ga-zentai-kougeki-de-ni-kai-kougeki-no-okaasan-wa-suki-desu-ka-Re-Zero-Kara-Ha.png",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** no parece estar feliz por ello e.e`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};