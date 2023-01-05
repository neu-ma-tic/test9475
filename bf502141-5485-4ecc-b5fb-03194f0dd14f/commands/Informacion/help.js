const {MessageEmbed, MessageActionRow, MessageButton} = require("discord.js");
const fs = require("fs");

module.exports = {
  category: "Informacion",
  name: "help",
  aliases: ["ayuda", "commands"],
  description: "Para ver la lista de comandos.",
  run: async (client, message, args, prefix) => {
    // Botones
    const button = new MessageActionRow().addComponents(
      new MessageButton()
      .setURL("https://discord.com/api/oauth2/authorize?client_id=868205294096887890&permissions=8&scope=bot")
      .setLabel("Invitame")
      .setStyle("LINK"),
      new MessageButton()
      .setURL("https://discord.gg/Y93Dad7")
      .setLabel("Soporte")
      .setStyle("LINK")
    );
    // Comando Help
    if (!args[0]) {
      let categories = [];
      fs.readdirSync("./commands/").forEach((dir) => {
        const commands = fs.readdirSync(`./commands/${dir}/`).filter((file) =>
          file.endsWith(".js")
        );
        const cmds = commands.map((command) => {
          let file = require(`../../commands/${dir}/${command}`);
          if (!file.name) return "Comando sin nombre.";
          let name = file.name.replace(".js", "");
          return `\`${name}\``;
        });
        let data = new Object();
        if (dir === "Secreto") return;
        data = {
          name: `${dir} (${commands.length})`,
          value: cmds.length === 0 ? "En desarollo..." : cmds.join(" "),
        };
        categories.push(data);
      });
      //EMBED DE HELP
      const embed = new MessageEmbed()
        .setTitle("📬 Lista de Comandos:")
        .setDescription(`**Hola me llamo ${client.user.username} y estos son mis comandos.**`)
        .addFields(categories)
        .setColor(config.color)
        .setFooter(`Escribe ${config.prefix}help <comando> para ayuda detallada. | Desarrollado por ${config.developer}`);
      return message.channel.send({
        embeds: [embed],
        components: [button]
      });
    } else {
      const command =
        client.commands.get(args[0].toLowerCase()) ||
        client.commands.find(
          (c) => c.aliases && c.aliases.includes(args[0].toLowerCase())
        );
      if (!command) {
        const embed = new MessageEmbed()
          .setTitle(`¡Comando no valido! Use \`${prefix}help\` para ver todos los comandos`)
          .setColor("FF0000");
        return message.channel.send({
          embeds: [embed]
        });
      }
      const embed = new MessageEmbed()
        .setTitle(`Ayuda detallada del comando "${command.name}"`, client.user.avatarURL())
        .addField("Categoria:", command.category ? `\`${command.category}\`` : "El comando no tiene Categoria")
        .addField("Comando:", command.name ? `\`${command.name}\`` : "El comando no tiene nombre.")
        .addField("Aliases:", command.aliases ? `\`${command.aliases.join("` `")}\`` : "El comando no tiene aliases.")
        .addField("Descripcion:", command.description ? command.description : "El comando no tiene descripcion.")
        .addField("Uso:", command.usage ? `\`${config.prefix}${command.name} ${command.usage}\`` : `\`${config.prefix}${command.name}\``)
        .setFooter(`<> = obligatorio | [] = opcional. | No incluyas estos símbolos al momento de ejecutar el comando.`)
        .setColor(config.color);
      return message.channel.send({
        embeds: [embed]
      });
    }
  },
};