const Discord = require("discord.js");

module.exports = {
  name: "shurg",
  aliases: [""],
  category: "Reaccion",
  description: "shurg",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://cdn.discordapp.com/attachments/399448944889036801/707748897195294780/ae9a6fce1c6a83d35d85b11eb34ecddc.jpg",
        "https://i.pinimg.com/originals/83/ce/94/83ce948166a598c00b08fb558b07f224.gif",
        "https://78.media.tumblr.com/0cf5b8479cc687456e29e23287910445/tumblr_p1edjjqx7m1wn2b96o1_500.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`Parece que a **${author}** no le importa.`)
        .setColor(0xf7b4b4)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};