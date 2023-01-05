const Discord = require("discord.js");

module.exports = {
  name: "8ball",
  aliases: [""],
  category: "Divercion",
  description:
    "Hazle preguntas de sí/no a Chocolat y ella te responderá. Ten en cuenta que por cuestiones de coherencia entre la pregunta y respuesta, debes preguntar algo que se pueda contestar con Sí o No",
  usage: "",
  run: async (client, message, args, color) => {
    var rpts = [
      "Si",
      "No",
      "Tal vez",
      "No se",
      "Claro!",
      "Si <3",
      "No >:(",
      "Por supuesto que no",
      "Claro",
      "No lo se",
      "Pregunta otra cosa, si?",
      "Eso no se pregunta",
    ];
    const pregunt = args.join(" ");
    let author = message.author.username;
    if (!pregunt) return message.channel.send(":x: | Falta la pregunta.");
    const embed = new Discord.MessageEmbed()
      .setTitle(":8ball: Pregunta 8ball.")
      .addField(`${author} pregunta:`, `${pregunt}`)
      .addField(
        "Mi respuesta es:",
        rpts[Math.floor(Math.random() * rpts.length)],
        true
      )
      .setColor(color);
      message.channel.send( { embeds: [embed] } );
  },
};
