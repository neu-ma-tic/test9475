const Command = require('../../structures/Command');
const { CommandInteraction, CommandInteractionOptionResolver, MessageEmbed } = require('discord.js');
const moment = require("moment");

module.exports = class extends Command {
    constructor(client) {
        super(client, {
            name: 'serverinfo',
            description: 'No description provided',
            category: 'general',
            cooldown: 2,
            userPermissions: [],
            options: [],
        });
    }
    /**
     * @param {CommandInteraction} interaction
     * @param {CommandInteractionOptionResolver} options
    */
    async run(interaction, options) {
        const guild = interaction.guild;
        const { channels, ownerId } = interaction.guild;
        const owner = await guild.members.fetch(ownerId);
        const createdAt = moment(guild.createdAt);
    
        const totalChannels = channels.cache.size;
        const categories = channels.cache.filter((c) => c.type === "GUILD_CATEGORY").size;
        const textChannels = channels.cache.filter((c) => c.type === "GUILD_TEXT").size;
        const voiceChannels = channels.cache.filter((c) => c.type === "GUILD_VOICE" || c.type === "GUILD_STAGE_VOICE").size;
      
        const memberCache = guild.members.cache;
        const all = memberCache.size;
        const bots = memberCache.filter((m) => m.user.bot).size;
        const onlineUsers = memberCache.filter((m) => !m.user.bot && m.presence?.status === "online").size;
        const onlineBots = memberCache.filter((m) => m.user.bot && m.presence?.status === "online").size;
        const onlineAll = onlineUsers + onlineBots;
        const users = all - bots;
    
        const roles = [...guild.roles.cache.sort((a, b) => b.position - a.position).values()];
		while (roles.join(', ').length >= 1021) {
			roles.pop();
		}
    
        const verificationLevels = {
            NONE: 'None',
            LOW: 'Low',
            MEDIUM: 'Medium',
            HIGH: 'High',
            VERY_HIGH: 'Very High'
        };
    
        const boostLevels = {
            NONE: '0',
            TIER_1: '1',
            TIER_2: '2',
            TIER_3: '3',
        }
      
        const embed = new MessageEmbed()
            .setColor(this.client.colors.maincolor)
            .setAuthor({ name: guild.name, iconURL: guild.iconURL({ dynamic: true }) })
            .setThumbnail(guild.iconURL({ dynamic: true}))
            .setDescription(`:crown: **Guild owner:** ${owner} (\`${owner.user.tag}\`)\n:busts_in_silhouette: **${users}** members [${bots} bots] | **${onlineAll}** online\n:calendar: **Created:** ${moment(guild.createdAt).format("MM/DD/YYYY")} (${createdAt.fromNow()})\n:lock: **Security** ${verificationLevels[guild.verificationLevel]}\n:rocket: **Boosts:** ${guild.premiumSubscriptionCount} (Tier **${boostLevels[guild.premiumTier]}**)\n**${totalChannels}** Channels | **${textChannels}** Text | **${voiceChannels}** Voice | **${categories}** Categories`)
            .addField(`:pushpin: Roles (${roles.length - 1})`, roles.size > 20 ? trimArray(roles, 20) : roles.join(', '))      
        if (guild.splashURL) embed.setImage(guild.splashURL);
        return interaction.reply({ embeds: [embed] })
    }
}

function trimArray(arr, maxLen = 25) {
    if (arr.array().length > maxLen) {
      const len = arr.array().length - maxLen;
      arr = arr.array().sort((a, b) => b.rawPosition - a.rawPosition).slice(0, maxLen);
      arr.map(role => `<@&${role.id}>`)
      arr.push(`${len} more...`);
    }
    return arr.join(", ");
  }