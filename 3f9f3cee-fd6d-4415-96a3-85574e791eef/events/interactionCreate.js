const { MessageEmbed } = require("discord.js");
const client = require("../index");

client.on("interactionCreate", async (interaction) => {
  // Slash Command Handling
  if (interaction.isCommand()) {
    await interaction.deferReply({ ephemeral: false }).catch(() => {});

    const cmd = client.slashCommands.get(interaction.commandName);
    if (!cmd) return interaction.followUp({ content: "An error has occured " });

    if (cmd.permission) {
      const authorPerms = interaction.channel.permissionsFor(
        interaction.member
      );
      if (!authorPerms || !authorPerms.has(cmd.permission)) {
        const Error1 = new MessageEmbed()
          .setColor("RANDOM")
          .setDescription(
            `⛔ You do not have the required permissions to run this commands: ${cmd.permission}`
          );
        return interaction.editReply({ embeds: [Error1] }).then((sent) => {
          setTimeout(() => {
            sent.delete();
          }, 10000);
        });
      }
    }

    const args = [];

    for (let option of interaction.options.data) {
      if (option.type === "SUB_COMMAND") {
        if (option.name) args.push(option.name);
        option.options?.forEach((x) => {
          if (x.value) args.push(x.value);
        });
      } else if (option.value) args.push(option.value);
    }
    interaction.member = interaction.guild.members.cache.get(
      interaction.user.id
    );

    cmd.run(client, interaction, args);
  }

  // Context Menu Handling
  if (interaction.isContextMenu()) {
    await interaction.deferReply({ ephemeral: false });
    const command = client.slashCommands.get(interaction.commandName);
    if (command) command.run(client, interaction);
  }
});
