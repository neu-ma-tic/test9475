/*-*-coding:utf-8 -*-
 *Auto updated?
 *   Yes
 *File :
 *   DiscordBot/Commands/Admin/cmds.js
 *Author :
 *   The-Repo-Club [wayne6324@gmail.com]
 *Github :
 *   https://github.com/The-Repo-Club/
 *
 *Created:
 *   Wed 23 February 2022, 12:04:54 PM [GMT]
 *Last edited:
 *   Mon 14 March 2022, 09:56:29 PM [GMT]
 *
 *Description:
 *   Cmds Command for Minimal-Mistakes#3775
 *
 *Dependencies:
 *   node, npm, discord.js, ms, cmdsDB
 **/

const { MessageEmbed, CommandInteraction } = require("discord.js");
const DB = require("../../Structures/Schemas/cmdsDB"); //Make sure this path is correct
const ms = require("ms");

module.exports = {
	name: "cmds",
	path: "Admin/cmds.js",
	description: "Setup or reset the cmds channel.",
	permission: "ADMINISTRATOR",
	options: [
		{
			name: "setup",
			description: "Setup the server cmds channel.",
			type: "SUB_COMMAND",
			options: [
				{
					name: "channel",
					description: "Select the channel to run server cmds in.",
					required: true,
					type: "CHANNEL",
					channelTypes: ["GUILD_TEXT"],
				},
			],
		},
		{
			name: "reset",
			description: "Reset the cmds channel.",
			type: "SUB_COMMAND",
		},
	],
	/**
	 * @param {CommandInteraction} interaction
	 */
	async execute(interaction) {
		try {
			const options = interaction.options;
			const { guild } = interaction;

			switch (options.getSubcommand()) {
				case "setup":
					{
						const CmdChannel = options.getChannel("channel");

						await DB.findOneAndUpdate(
							{ GuildID: guild.id },
							{
								ChannelID: CmdChannel.id,
							},
							{
								new: true,
								upsert: true,
							}
						).catch((err) => console.log(err));

						const LogsSetup = new MessageEmbed()
							.setDescription(
								"✅ | Successfully setup the server cmds channel."
							)
							.setColor("#43b581");

						await guild.channels.cache
							.get(CmdChannel.id)
							.send({ embeds: [LogsSetup] })
							.then((m) => {
								setTimeout(() => {
									m.delete().catch(() => {});
								}, ms("5s"));
							});

						await interaction.reply({
							content: "Done",
							ephemeral: true,
						});
					}
					break;
				case "reset":
					{
						const LogsReset = new MessageEmbed()
							.setDescription("✅ | Successfully reset the logging channel.")
							.setColor("#43b581");
						DB.deleteMany({ GuildID: guild.id }, async (err, data) => {
							if (err) throw err;
							if (!data)
								return interaction.reply({
									content: "There is no data to delete",
								});
							return interaction
								.reply({ embeds: [LogsReset], fetchReply: true })
								.then((msg) => {
									setTimeout(() => msg.delete(), ms("5s"));
								});
						});
					}
					return;
			}
		} catch (error) {
			if (error.message === "Missing Access") {
				return interaction.reply({
					embeds: [
						new MessageEmbed()
							.setColor("RED")
							.setDescription(
								`❌ The bot does not have access to this channel.`
							),
					],
				});
			} else {
				return interaction.reply({
					embeds: [
						new MessageEmbed()
							.setColor("RED")
							.setDescription(
								`❌ An error occurred. \n\n \`\`\`${error}\`\`\``
							),
					],
				});
			}
		}
	},
};
