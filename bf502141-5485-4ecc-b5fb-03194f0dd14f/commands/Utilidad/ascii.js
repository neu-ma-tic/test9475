const Discord = require("discord.js");
const figlet = require("figlet");

module.exports = {
  name: "ascii",
  aliases: [""],
  category: "Utilidad",
  description: "Convierte un texto en un textart ascii",
  usage: "<texto>",
  cooldown: 2,
  run: async (client, message, args, color) => {
    let data = args.join(" ");
    if (data.length > 15)
      return message.reply("Solo se permite hasta 15 carácteres.");
    if (!data) return message.reply("Escribe algo.");
    figlet(data, (err, data) =>
      message.channel.send("**Texto Generado:**\n" + "```" + data + "```" + "")
    );
  },
};
