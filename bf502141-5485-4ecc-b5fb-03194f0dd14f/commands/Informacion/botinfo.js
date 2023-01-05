const Discord = require("discord.js");
const moment = require("moment");
require("moment-duration-format");
var cpuStat = require("cpu-stat");

module.exports = {
  name: "botinfo",
  aliases: [""],
  category: "Info",
  description: "Iformacion acerca del Bot",
  usage: "",
  cooldown: 5,
  run: async (client, message, args, color) => {
    cpuStat.usagePercent(function (err, percent, seconds) {
      if (err) {
        return console.log(err);
      }

      var totalCores = cpuStat.totalCores();
      var avgClockMHz = cpuStat.avgClockMHz();
      const uptime = moment
        .duration(client.uptime)
        .format(" D [dias], H [hrs], m [mins], s [secs]");
      const botinfo = new Discord.MessageEmbed()
        .setAuthor(`Informacion del bot`, client.user.avatarURL())
        .setDescription("Informacion acerca del Bot")
        .addField("Developer:", `${config}`)
        .addField(
          "Servidores: ",
          "```diff\n- " + client.guilds.cache.size + "\n```",
          true
        )
        .addField("Uptime: ", "```\n" + uptime + "\n```", true)
        .addField(
          "CPU: ",
          "```prolog\n" +
          parseInt(percent) +
          "%\n```",
          true
        )
        .addField(
          "RAM: ",
          "```fix\n" +
          (process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2) +
          "MB\n```",
          true
        )
        .addField("Lenguaje: ", '```json\n"JavaScript"\n```', true)
        .addField("Libreria: ", "```ini\n[Discord.js 13.0.0]\n```", true)
        .setFooter(`Informacion del solicitada por ${message.author.username}`, message.author.avatarURL)
        .setColor(color);

      message.channel.send({
        embeds: [botinfo]
      });
    });
  },
};