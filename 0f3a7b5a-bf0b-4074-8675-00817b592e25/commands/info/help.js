const { MessageEmbed } = require("discord.js");
const { readdirSync } = require("fs");
const prefix = config.BOT_PREFIX

module.exports = {
  name: "help",
  aliases : ['h'],
  description: "Показва всички налични команди на бота.",
  prefix : "!",

  /**
  * @param {Bot} bot
  * @param {Message} message
  * @param {String[]} args
  */

  run: async (client, message, args) => {


    const roleColor =
      message.guild.me.displayHexColor === "#000000"
        ? "#ffffff"
        : message.guild.me.displayHexColor;

    if (!args[0]) {
      let categories = [];

      readdirSync("./commands/").forEach((dir) => {
        const commands = readdirSync(`./commands/${dir}/`).filter((file) =>
          file.endsWith(".js") && file.indexOf("{ignore}") == -1
        );

        const cmds = commands.map((command) => {
          let file = require(`../../commands/${dir}/${command}`);

          if (!file.name) return "Няма име на команда.";

          let name = file.name.replace(".js", "");

          return `\`${name}\``;
        });

        let data = new Object();

        data = {
          name: dir.toUpperCase(),
          value: cmds.length === 0 ? "В процес на изпълнение..." : cmds.join(" "),
        };

        categories.push(data);
      });

      const embed = new MessageEmbed()
        .setTitle("📬 Нужна е помощ? Ето всички мои команди:")
        .addFields(categories)
        .setThumbnail('https://i.imgur.com/Pr0OBYu.png')
        .setTimestamp()
        .setDescription(
          `Използвай \`${prefix}help\` последвано от името на командата, за да получите повече допълнителна информация за нея. Например: \`${prefix}help ban\`.`
        )
        .setFooter(
          `Заявено от ${message.author.tag}`,
          message.author.displayAvatarURL({ dynamic: true })
        )
        .setTimestamp()
        .setColor('#0099ff');
      return message.channel.send(embed);
    } else {
      const command =
        client.commands.get(args[0].toLowerCase()) ||
        client.commands.find(
          (c) => c.aliases && c.aliases.includes(args[0].toLowerCase())
        );

      if (!command) {
        const embed = new MessageEmbed()
          .setTitle(`Инвалидна команда! Използвай \`${prefix}help\` за всички мои команди!`)
          .setColor("FF0000");
        return message.channel.send(embed);
      }

      const embed = new MessageEmbed()
        .setTitle("Детайли на командата:")
        .addField("ПРЕФИКС:", `\`${prefix}\``)
        .addField(
          "КОМАНДА:",
          command.name ? `\`${command.name}\`` : "Няма име за тази команда."
        )
        .addField(
          "ПСЕВДОНИМ:",
          command.aliases
            ? `\`${command.aliases.join("` `")}\``
            : "Няма псевдоними за тази команда."
        )
        .addField(
          "УПОТРЕБА:",
          command.usage
            ? `\`${prefix}${command.name} ${command.usage}\``
            : `\`${prefix}${command.name}\``
        )
        .addField(
          "ОПИСАНИЕ:",
          command.description
            ? command.description
            : "Няма описание за тази команда."
        )
        .setFooter(
          `Заявено от ${message.author.tag}`,
          message.author.displayAvatarURL({ dynamic: true })
        )
        .setTimestamp()
        .setColor('#0099ff');
      return message.channel.send(embed);
    }
  },
};