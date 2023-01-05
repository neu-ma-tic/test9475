const Schema = require("../../models/suggestionChannel");
const { MessageEmbed, CommandInteraction } = require("discord.js");

module.exports = {
  name: "suggestionsetchannel",
  description: "Set the server's suggestion channel",
  permission: ["MANAGE_GUILD"],
  options: [
    {
      name: "channel",
      type: "CHANNEL",
      description: "Channel for the suggestions",
      required: true,
    },
  ],

  /**
   *
   * @param {Client} client
   * @param {CommandInteraction} interaction
   * @param {String[]} args
   */

  run: async (client, interaction, args) => {
    const channel = interaction.options.getChannel("channel");

    if (channel.type !== "GUILD_TEXT")
      return interaction.followUp({ content: "Please choose a text channel" });

    Schema.findOne({ Guild: interaction.guildId }, async (err, data) => {
      if (data) {
        data.Channel = channel.id;
        data.save();
      } else {
        new Schema({
          Guild: interaction.guildId,
          Channel: channel.id,
        }).save();
      }
      interaction.followUp({
        content: `${channel} has been saved as the suggestion channel`,
      });
    });
  },
};
