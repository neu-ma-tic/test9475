const Discord = require("discord.js");

module.exports = {
  name: "happy",
  aliases: [""],
  category: "Reaccion",
  description: "Demuestra tu felicidad con una sonrisa.",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/586593020741156874/happy_ngnl_15.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/715944429202178078/a5b34e01b953b80d7877fa508263bde8.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/651510686161305630/90a4e174-527e-445f-be80-3cf49010b0bb.gif",
        "https://imgur.com/Dl9OgKn.gif",
        "https://cdn.discordapp.com/attachments/399448944889036801/600528806041747527/tumblr_ntepjt6u9i1ta7pubo2_500.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** anda muy alegre.`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};