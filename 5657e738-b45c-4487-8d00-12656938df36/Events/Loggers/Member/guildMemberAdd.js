// -*-coding:utf-8 -*-
// -------------------------------------------------------------------------
// Path          - DiscordBot/Events/Loggers/Member/guildMemberAdd.js
// Git           - https://github.com/The-Repo-Club
// Author        - The-Repo-Club [wayne6324@gmail.com]
// Start On      - Wed 23 February 2022, 12:04:54 pm (GMT)
// Modified On   - Mon 14 March 2022, 03:27:51 pm (GMT) 
// -------------------------------------------------------------------------

const { MessageEmbed, GuildMember, MessageAttachment } = require("discord.js");
const DB = require("../../../Structures/Schemas/logsDB"); //Make sure this path is correct
const Canvas = require("../../../Systems/Canvas/index");

module.exports = {
	name: "guildMemberAdd",
	path: "Member/guildMemberAdd.js",
	/**
	 * @param {GuildMember} member
	 */
	async execute(member) {
		const Data = await DB.findOne({
			GuildID: member.guild.id,
		});
		if (!Data || !Data.MemberLogs) return;

		const logsChannel = member.guild.channels.cache.get(Data.MemberLogs);
		const logs = await member.guild.fetchAuditLogs({
			limit: 1,
		});
		const log = logs.entries.first(); // Fetches the logs and takes the last entry

		if (log.action == "BOT_ADD") {
			// If the last entry fetched is of the type "BOT_ADD" it means a bot has joined
			const botJoinedEmbed = new MessageEmbed()
				.setTitle(
					"<:icons_unbanmember:949376464388784138> A Bot Joined The Server"
				)
				.setColor("GREEN")
				.setTimestamp()
				.setFooter({ text: member.guild.name })
				.setDescription(
					`> The bot ${member} has been added by \`${log.executor.tag}\` to this server`
				);

			logsChannel
				.send({ embeds: [botJoinedEmbed] })
				.catch((err) => console.log(err));
		} else {
			// Else it means a normal user joined
			const userJoinedEmbed = new MessageEmbed()
				.setColor("GREEN")
				.setTitle(
					"<:icons_unbanmember:949376464388784138> An User Just Joined The Server"
				)
				.setTimestamp()
				.setFooter({ text: member.guild.name })
				.setDescription(`> The user ${member} just joined the guild`);

			logsChannel
				.send({ embeds: [userJoinedEmbed] })
				.catch((err) => console.log(err));
		}
	},
};
