const Discord = require("discord.js");

module.exports = {
  name: "like",
  aliases: [""],
  category: "Reaccion",
  description: "Te gusta.",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
        var url = [
          "https://cdn.discordapp.com/attachments/399448944889036801/701455116460359711/dcbe9fd2-3c2b-4ff2-877b-2815e2cef577.gif",
          "https://cdn.discordapp.com/attachments/399448944889036801/677607434109321262/1522111812_tenor.gif",
          "https://cdn.discordapp.com/attachments/399448944889036801/677210104545804307/57a68efd6d89926fb8a4d4a44131fff3.gif",
        ];
        let url2 = url[Math.floor(url.length * Math.random())];
        let author = message.author.username;
        const embed = new Discord.MessageEmbed()
          .setDescription(`A **${author}** le gusta eso :D`)
          .setColor(0xf7b4b4)
          .setImage(url2)
          .setTimestamp();
    
          message.channel.send({ embed });
  },
};