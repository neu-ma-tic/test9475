// -*-coding:utf-8 -*-
// -------------------------------------------------------------------------
// Path          - DiscordBot/Structures/Handlers/loggers.js
// Git           - https://github.com/The-Repo-Club
// Author        - The-Repo-Club [wayne6324@gmail.com]
// Start On      - Wed 23 February 2022, 12:04:54 pm (GMT)
// Modified On   - Mon 14 March 2022, 07:59:33 pm (GMT) 
// -------------------------------------------------------------------------

const { Event, Events } = require("../Validation/eventNames");

/**
 * @param {Client} client
 */
module.exports = async (client, PG, Ascii) => {
	const Table = new Ascii("Loggers Loaded");

	(await PG(`${process.cwd()}/Events/Loggers/*/*.js`)).map(async (file) => {
		const event = require(file);

		if (!Events.includes(event.name) || !event.name) {
			await Table.addRow(
				`${event.name || "MISSING"}`,
				`🟥 Loggers Event name is either invalid or missing: ${event.path}`
			);
			return;
		}

		if (event.once) {
			client.once(event.name, (...args) => event.execute(...args, client));
		} else {
			client.on(event.name, (...args) => event.execute(...args, client));
		}

		await Table.addRow(event.path, "🟩 SUCCESSFUL");
	});

	console.log(Table.toString());
};
