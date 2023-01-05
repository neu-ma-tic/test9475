const Discord = require("discord.js");

module.exports = {
  name: "eval",
  aliases: [""],
  category: "secreto",
  description: "Comando para evaluar (solo para desarroladores)",
  usage: "<evaluacion>",
  run: async (client, message, args, color) => {
    if (message.author.id !== "615254840586797067") {
      let embed = new Discord.MessageEmbed()
        .setDescription(
          "Mmm, no tienes los permisos suficientes para hacer esto"
        );
      message.channel.send({ embeds: [embed] });
      return 0;
    }

    let toEval = args.join(" "); //Definimos toEval con argumentos
    if (!toEval) {
      //Creamos un if para que diga
      let embed = new Discord.MessageEmbed()
        .setDescription("Necesitas evaluar __*ALGO*__")
        .setColor(color);
      message.channel.send({ embeds: [embed] }).then((m) => m.delete(10000));
    }
    try {
      //Hacemos un try
      if (args.join(" ").toLowerCase().includes("token")) {
        return;
      }
      let evaluated = eval(toEval); //"evaluated" va a evaluar el comando

      let beautify = require("beautify"); //Se usa beautify para que funcione
      let embed = new Discord.MessageEmbed() //Creamos otro embed
        .setColor(color)
        .setTimestamp() //Usamos un Timestamp
        .setFooter(client.user.username, client.user.displayAvatarURL)
        .setTitle(":desktop: Eval")
        .setDescription("Este comando sirve para ejecutar codigos")
        .addField(
          "Codigo:",
          "```js\n" + beautify(args.join(" "), { format: "js" }) + "```"
        )
        .addField("Lo evaluado:", "```js\n" + evaluated + "```"); //Aca aparecera lo que se evalua
      message.channel.send({ embeds: [embed] });
    } catch (err) {
      //Hacemos un catch y que defina err
      let beautify = require("beautify");
      let embed2 = new Discord.MessageEmbed()
        .setTimestamp()
        .setFooter(client.user.username, client.user.displayAvatarURL)
        .addField(
          "Hubo un error con el codigo que evaluaste",
          "```js\n" + err + "```"
        ) //Va a aparecer el error
        .setColor(color);
      message.channel.send({ embeds: [embed2] });
    }
  },
};
