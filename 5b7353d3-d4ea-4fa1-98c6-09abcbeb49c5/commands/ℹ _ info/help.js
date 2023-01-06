const { MessageEmbed } = require('discord.js');
const { stripIndents } = require('common-tags');
const ms = require('ms');
const { PREFIX } = process.env;

module.exports = {
	name: 'help',
	aliases: ['h'],
	category: 'ℹ | info',
	description: 'Returns all commands, or one specific command info',
	usage: '[command | alias]',
	run: async (client, message, args) => {
		if (args[0]) {
			return getCMD(client, message, args[0]);
		}
		return getAll(client, message);
	},
};

function getAll(client, message) {
	const embed = new MessageEmbed().setAuthor(`${client.user.username}'s commands`).setColor('#19a0d6').setThumbnail(client.user.displayAvatarURL());

	const commands = (category) => client.commands
		.filter((cmd) => cmd.category === category)
		.map((cmd) => `\`${cmd.name}\`,`)
		.join(' ');

	const info = client.categories
		.map(
			(cat) => stripIndents`**${cat[0].toUpperCase() + cat.slice(1)}** **[${client.commands.filter((cmd) => cmd.category === cat).size}]** \n${commands(
				cat,
			)}`,
		)
		.reduce((string, category) => `${string}\n${category}`);
	embed.setFooter(`Type ${PREFIX}help <command> for command info`);
	return message.channel.send(embed.setDescription(info));
}

function getCMD(client, message, input) {
	const embed = new MessageEmbed();

	const cmd = client.commands.get(input.toLowerCase())
        || client.commands.get(client.aliases.get(input.toLowerCase()));

	let info = `No information found for command **${input.toLowerCase()}**`;

	if (!cmd) {
		return message.channel.send(embed.setColor('#fb644c').setAuthor(`${message.author.username}, Requested Commands:`).setDescription(info));
	}

	if (cmd.name) info = `**__Command name__**: \`${cmd.name}\``;
	if (cmd.aliases) info += `\n**__Aliases__**: ${cmd.aliases.map((a) => `\`${a}\``).join(', ')}`;
	if (cmd.description) info += `\n**__Description__**: \`${cmd.description}\``;
	if (cmd.usage) {
		info += `\n**Usage**: \`${cmd.usage}\``;
		embed.setFooter('Syntax: <> = required, [] = optional');
	}
	if (cmd.timeout) info += `\n**Timeout**: \`${ms(cmd.timeout)}\``;
	return message.channel.send(embed.setColor('#19a0d6').setAuthor(`Command help`).setDescription(info));
}
