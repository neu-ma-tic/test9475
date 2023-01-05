const Command = require('../../structures/Command');
const { CommandInteraction, CommandInteractionOptionResolver, MessageEmbed } = require('discord.js');
const moment = require('moment');

module.exports = class extends Command {
    constructor(client) {
        super(client, {
            name: 'userinfo',
            description: 'Displays information of a user',
            category: 'general',
            cooldown: 2,
            userPermissions: [],
            options: [
                {
                    name: "user",
                    description: "The user u want the information from.",
                    type: "USER",
                    required: false,
                },
            ],
        });
    }
    /**
     * @param {CommandInteraction} interaction
     * @param {CommandInteractionOptionResolver} options
    */
    async run(interaction, options) {
        const member = options.getMember("user") || interaction.member;
        const roles = member.roles;
        let presence = member.presence?.status;
        const userFlags = member.user.flags;

        const embed = new MessageEmbed()
            .setColor(this.client.colors.maincolor)
            .setAuthor({ name: `${member.user.username}'s Information`, iconURL: member.user.displayAvatarURL({ dynamic: true })})
            .setThumbnail(member.user.displayAvatarURL({ dynamic: true }))
            .setDescription(`
:bust_in_silhouette: **User:** ${member} (\`${member.user.tag}\`)
:calendar: **Created:** ${moment(member.user.createdTimestamp).format("DD MMM YYYY")} (${moment(member.user.createdAt).fromNow()})
:inbox_tray: **Joined server:** ${moment(member.joinedAt).format("DD MMM YYYY")}
:star: **Presence:** ${statuses[presence]}
:triangular_flag_on_post: **Flags:** \`${userFlags.length ? userFlags.map(flag => flags[flag]).join(', ') : 'None'}\`
`) 

        .addField(`:pushpin: Roles (${roles.cache.size})`, `${roles.cache.size < 25 ? roles.cache.sort((a, b) => b.position - a.position).map(role => role.toString()).slice(0, -1) : roles.cache.size > 25 ? trimArray(roles.cache) : 'None'}`, false)
    return interaction.reply({ embeds: [embed] })
    }
}

const flags = {
	DISCORD_EMPLOYEE: 'Discord Employee',
	DISCORD_PARTNER: 'Discord Partner',
	BUGHUNTER_LEVEL_1: 'Bug Hunter (Level 1)',
	BUGHUNTER_LEVEL_2: 'Bug Hunter (Level 2)',
	HYPESQUAD_EVENTS: 'HypeSquad Events',
	HOUSE_BRAVERY: 'House of Bravery',
	HOUSE_BRILLIANCE: 'House of Brilliance',
	HOUSE_BALANCE: 'House of Balance',
	EARLY_SUPPORTER: 'Early Supporter',
	TEAM_USER: 'Team User',
	SYSTEM: 'System',
	VERIFIED_BOT: 'Verified Bot',
	VERIFIED_DEVELOPER: 'Verified Bot Developer'
};

function trimArray(arr, maxLen = 25) {
  if (arr.array().length > maxLen) {
    const len = arr.array().length - maxLen;
    arr = arr.array().sort((a, b) => b.rawPosition - a.rawPosition).slice(0, maxLen);
    arr.map(role => `<@&${role.id}>`)
    arr.push(`${len} more...`);
  }
  return arr.join(", ");
}
const statuses = {
  "online" : "🟢 Online",
  "idle" : "🟠 Idle",
  "dnd" : "🔴 Dnd",
  "offline" : "⚫️ Ofline",
}
