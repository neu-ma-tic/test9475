const Discord = require("discord.js");

module.exports = {
  name: "clear",
  aliases: ["purge"],
  category: "Moderacion",
  description: "Comando para borrar cierta cantidad de mensajes",
  usage: "<numero>",
  cooldown: 2,
  run: async (client, message, args, color) => {
    if (
      !message.guild.me.permissionsIn(message.channel).has("MANAGE_MESSAGES")
    ) {
      return message.channel.send("Perdon, pero no tengo permisos");
    }

    if (!message.member.permissionsIn(message.channel).has("MANAGE_MESSAGES")) {
      return message.channel.send("Perdon, pero no tienes permisos");
    }

    if (!args)
      return message.channel.send("Escriba la cantidad de mensajes a eliminar");
    let cantidad = parseInt(args[0]);

    if (!cantidad || isNaN(cantidad))
      return message.reply("Introduce un numero por favor");

    if (cantidad < 1) {
      message.channel.send(
        "El minimo de mensajes que puedo borrar es 1, Xd"
      );
    }else if (cantidad > 100) {
      message.channel.send(
        "El maximo de mensajes que puedo borrar es 100, por lo tanto lo establecere automaticamente ahi"
      );
      cantidad = 100;
    }

    message.channel.bulkDelete(cantidad + 1).then(() => {
      message.channel
        .send(`<a:yes:868260831756963861> Has borrado ${cantidad} mensajes!`)
        .then((message) => message.delete({ timeout: 3000 }));
    });
  },
};
