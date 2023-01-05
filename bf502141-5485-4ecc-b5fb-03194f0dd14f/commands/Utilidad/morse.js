const Discord = require("discord.js");
const morse = require("morse");

module.exports = {
  name: "morse",
  aliases: [""],
  category: "Utilidad",
  description: "Comando para encriptar y desencriptar codigo morse",
  usage: "de <texto> | en <texto>",
  cooldown: 2,
  run: async (client, message, args, color) => {
    if (!args[0])
      return message.channel.send(
        "Opciones: `en` (Cifra un codigo morse) o `de` (Decifrar un codigo morse)"
      );
    let Options = ["de", "en"];
    if (!Options.includes(args[0].toLowerCase()))
      return message.channel.send(":x: Opcion incorrecta!");
    let texto = args.slice(1).join(" ");

    if (args[0] == "de") {
      let decode = morse.decode(texto);
      if (!texto) return message.channel.send("Escribe algo a decifrar");
      //EMBED
      const embed = new Discord.MessageEmbed()
        .addField("Entrada:", `\`\`\`js\n${texto}\`\`\``, false) // Te da el calculo
        .setTitle("🤫 Decifrar Morse")
        .addField("Salida", `\`\`\`js\n${decode}\`\`\``, false)
        .setColor(color);
      message.channel.send({ embeds: [embed] });
    } else if (args[0] == "en") {
      let encode = morse.encode(texto);
      if (!texto) return message.channel.send("Escribe algo a cifrar");
      //EMBED
      const embed = new Discord.MessageEmbed()
        .addField("Entrada:", `\`\`\`js\n${texto}\`\`\``, false) // Te da el calculo
        .setTitle("🤫 Cifrar Morse")
        .addField("Salida", `\`\`\`js\n${encode}\`\`\``, false)
        .setColor(color);
      message.channel.send({ embeds: [embed] });
    }
  },
};
