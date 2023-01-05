// -*-coding:utf-8 -*-
// -------------------------------------------------------------------------
// Path          - DiscordBot/Commands/Admin/ping.js
// Git           - https://github.com/The-Repo-Club
// Author        - The-Repo-Club [wayne6324@gmail.com]
// Start On      - Wed 23 February 2022, 12:04:54 pm (GMT)
// Modified On   - Wed 23 February 2022, 12:06:14 pm (GMT)
// -------------------------------------------------------------------------

const { CommandInteraction } = require("discord.js");
const ms = require("ms");

const cd = ms("5m");

module.exports = {
	name: "ping",
	path: "Admin/ping.js",
	description: "Ping",
	permission: "ADMINISTRATOR",
	cooldown: cd,
	/**
	 *
	 * @param {CommandInteraction} interaction
	 */
	execute(interaction) {
		interaction.reply({ content: "PONG" });
	},
};
