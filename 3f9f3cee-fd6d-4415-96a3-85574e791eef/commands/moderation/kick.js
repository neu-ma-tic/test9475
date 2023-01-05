const { Client, CommandInteraction } = require("discord.js");

module.exports = {
  name: "kick",
  description: "kick a member",
  permission: ["ADMINISTRATOR"],
  options: [
    {
      name: "target",
      description: "target to kick",
      type: "USER",
      required: true,
    },
    {
      name: "reason",
      description: "reason for this ban",
      type: "STRING",
      required: "false",
    },
  ],

  /**
   * @param {Client} client
   * @param {CommandInteraction} interaction
   * @param {String[]} args
   */
  run: async (client, interaction, args) => {
    const target = interaction.options.getMember("target");
    const reason =
      interaction.options.getString("reason") || "No reason provided";

    if (
      target.roles.highest.position >= interaction.member.roles.highest.position
    )
      return interaction.followUp({ content: "You cant kick this member" });

    await target.send(
      `You have been kicked from ${interaction.guild.name}, reason: ${reason}`
    );

    target.kick(reason);

    interaction.followUp({ content: `successfully kick ${target.user.tag}` });
  },
};
