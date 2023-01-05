const { MessageEmbed, CommandInteraction } = require("discord.js");
const ms = require("ms");
const schema = require("../../models/suggestionChannel");

module.exports = {
  name: "suggestdeny",
  description: "Deny the worst suggestions.",
  permission: ["MANAGE_GUILD"],
  options: [
    {
      name: "id",
      type: "STRING",
      description: "The suggestion to deny(ID)",
      required: true,
    },
    {
      name: "reason",
      type: "STRING",
      description: "The reason why the suggestion should be denied.",
      require: true,
    },
  ],

  /**
   *
   * @param {Client} client
   * @param {CommandInteraction} interaction
   * @param {String[]} args
   */

  run: async (client, interaction, args) => {
    const id = interaction.options.getString("id");
    const reason = interaction.options.getString("reason");

    schema.findOne({ Guild: interaction.guildId }, async (err, data) => {
      if (!data)
        return interaction.followUp({
          content: "The servers's suggestion channel could not be found.",
        });

      const channel = client.channels.cache.get(data.Channel);
      const suggestembed = await channel.messages.fetch(id);
      const sdata = suggestembed.embeds[0];

      const Embed = new MessageEmbed()
        .setDescription(`${sdata.description}`)
        .addField("Status (DENNIED)", reason)
        .setColor("RANDOM")
        .setTimestamp();

      suggestembed.edit({ embeds: [Embed] });
      interaction
        .followUp({
          content: `Successfully edited state of suggestion.`,
          ephemeral: true,
        })
        .then((msg) => {
          setTimeout(() => msg.delete(), ms("5 seconds"));
        });
    });
  },
};
