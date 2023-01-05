const { MessageEmbed, CommandInteraction } = require("discord.js");
const ms = require("ms");
const schema = require("../../models/suggestionChannel");

module.exports = {
  name: "suggest",
  description: "Suggest something!",
  permission: [""],
  options: [
    {
      name: "suggestion",
      type: "STRING",
      description: "Suggest something!",
      required: true,
    },
  ],

  /**
   *
   * @param {Client} client
   * @param {CommandInteraction} interaction
   * @param {String[]} args
   */

  run: async (client, interaction, message, args) => {
    const suggestion = interaction.options.getString("suggestion");

    schema.findOne({ Guild: interaction.guildId }, async (err, data) => {
      if (!data)
        return interaction.followUp({
          content: "The servers's suggestion channel could not be found.",
        });

      const channel = client.channels.cache.get(data.Channel);

      const Embed = new MessageEmbed()
        .setAuthor(
          interaction.user.tag,
          interaction.user.displayAvatarURL({ dynamic: true })
        )
        .setDescription(`**Suggestion**: ${suggestion}`)
        .addField("Status", "PENDING")
        .setColor("RANDOM")
        .setTimestamp();

      channel.send({ embeds: [Embed] });
      interaction
        .followUp({
          content: `Your suggestion has been sent.`,
          ephemeral: true,
        })
        .then((msg) => {
          setTimeout(() => msg.delete(), ms("5 seconds"));
        });
    });
  },
};
