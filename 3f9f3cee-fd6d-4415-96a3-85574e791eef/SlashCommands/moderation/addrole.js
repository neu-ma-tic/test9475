const { MessageEmbed } = require("discord.js");
const ms = require("ms");
module.exports = {
  name: "addrole",
  description: "returns websocket ping",
  type: "CHAT_INPUT",
  permission: "ADMINISTRATOR",
  options: [
    {
      name: "user",
      description: "What bug are u reporting?",
      type: "USER",
      required: true,
    },
    {
      name: "role",
      description: "What bug are u reporting?",
      type: "ROLE",
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
    if (!interaction.member.permissions.has("MANAGE_ROLES"))
      return interaction.followUp({
        content: "You need the `MANAGE_ROLES` permission to use this command!",
      });

    const member = interaction.options.getMember("user");
    const roleto = interaction.options.getRole("role");
    if (member.roles.cache.some((role) => role.name === roleto.name)) {
      return interaction.followUp({
        content: "That user already has that role!",
      });
    }
    if (roleto.managed)
      return interaction.followUp({ content: "That role is managed!" });
    if (roleto.position >= interaction.member.roles.highest.position)
      return interaction.followUp({
        content: `I cannot add the ${roleto} role to ${member}`,
      });
    if (roleto.position >= interaction.guild.me.roles.highest.position)
      return interaction.followUp({
        content: `I cannot add the ${roleto} role to ${member}`,
      });

    member.roles.add(roleto);

    const embed = new MessageEmbed()
      .setTitle(`successfully added role`)
      .setDescription(`✔️ successfully added ${roleto} role to ${member}`)
      .setColor("RANDOM")
      .setTimestamp();

    interaction.followUp({ embeds: [embed] });
  },
};
