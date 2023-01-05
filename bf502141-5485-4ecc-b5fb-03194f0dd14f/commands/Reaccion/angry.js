const Discord = require("discord.js");

module.exports = {
  name: "angry",
  aliases: [""],
  category: "Reaccion",
  description: "Expresa que estás enfadado.\nSi mencionas a alguién darás a entender que estás enfadado/a con esa persona.",
  usage: "",
  cooldown: 2,
  run: async (client, message, args, color) => {
    var url = [
        "https://media1.tenor.com/images/cfbc067a1445d5baa5ca36cc2642a6c4/tenor.gif?itemid=5664724",
        "https://media1.tenor.com/images/3424df822494d78bc184aae3e14d84e3/tenor.gif?itemid=4675166",
        "https://cdn.discordapp.com/attachments/399448944889036801/609026412354994176/angry2.gif",
      ];
      let url2 = url[Math.floor(url.length * Math.random())];
      let author = message.author.username;
      const embed = new Discord.MessageEmbed()
        .setDescription(`**${author}** se ha molestado mucho.`)
        .setColor(color)
        .setImage(url2)
        .setTimestamp();
  
        message.channel.send({ embed });
  },
};
