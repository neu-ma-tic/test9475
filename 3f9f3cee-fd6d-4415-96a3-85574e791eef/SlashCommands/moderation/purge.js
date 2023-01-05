const ms = require("ms");
module.exports = {
  name: "purge",
  description: "Remove a messages",
  permissions: ["ADMINISTRATOR"],
  options: [
    {
      name: "amount",
      description: "amount message that u want to deleted",
      type: "INTEGER",
      required: true,
    },
  ],

  run: async (client, interaction, message, args) => {
    const amount = interaction.options.getInteger("amount");

    if (amount > 100)
      return interaction.followUp({
        content: "The maximum amount is 100 messages",
      });

    const messages = await interaction.channel.messages.fetch({
      limit: amount + 1,
    });

    const filtered = messages.filter(
      (msg) => Date.now() - msg.createdTimestamp < ms("14 days")
    );

    await interaction.channel.bulkDelete(filtered);

    interaction.channel
      .send({ content: `Deleted ${filtered.size - 1} messages` })
      .then((msg) => {
        setTimeout(() => msg.delete(), ms("10 seconds"));
      });
  },
};
