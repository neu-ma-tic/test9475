const Discord = require("discord.js");

module.exports = {
  name: "avatar",
  aliases: [""],
  category: "Utilidad",
  description: "Comando para ver el avatar un un usuario",
  usage: "[usuario o ID]",
  cooldown: 2,
  run: async (client, message, args, color) => {
    let usuario;
    if (message.mentions.users.first()) {
      usuario = message.mentions.users.first().id;
    } else if (args[0]) {
      usuario = args[0];
    } else {
      usuario = message.author.id;
    }
    try {
      let user = await client.users.fetch(usuario);
      const embed = new Discord.MessageEmbed()
        .setTitle(`Avatar de ${user.tag}`)
        .setColor(color)
        .setImage(user.displayAvatarURL({ size: 4096, dynamic: true }))
        .setFooter(
          message.author.tag,
          message.author.displayAvatarURL({ dynamic: true })
        );
        message.reply({ embeds: [embed] });
    } catch {
      const error = new Discord.MessageEmbed()
        .setAuthor(client.user.username, client.user.displayAvatarURL())
        .setTitle(`Error! <a:no:868260948299878502>`)
        .setColor("RED")
        .setDescription(
          `${usuario} No es una ID valida, asegurate de que sea de un usuario!`
        );
        message.channel.send({ embeds: [error]});
    }
  },
};
