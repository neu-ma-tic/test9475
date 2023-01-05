const { MessageActionRow, MessageButton, MessageEmbed } = require("discord.js");

module.exports = {
  name: "invite",
  description: "Returns bot latency!",
  type: "CHAT_INPUT",

  run: async (client, interaction, args) => {
    const server = new MessageActionRow().addComponents(
      new MessageButton()
        .setLabel("Support server")
        .setStyle("LINK")
        .setURL("https://discord.io/DarkMcID")
    );

    const embed = new MessageEmbed()
      .setColor("RANDOM")
      .setTitle("Hello")
      .setDescription("This is my link")
      .setFooter("Thank youu");

    interaction.channel.send({
      embeds: [embed],
      components: [server],
    });
  },
};
