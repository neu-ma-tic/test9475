import { cache, ChannelTypes, snowflakeToBigint } from '../../deps.ts';
import { bot } from '../../cache.ts';

bot.arguments.set('categorychannel', {
    name: 'categorychannel',
    execute: function (_argument, parameters, message) {
        const [id] = parameters;
        if (!id) return;

        const guild = cache.guilds.get(message.guildId);
        if (!guild) return;

        const channelIdOrName = id.startsWith('<#') ? id.substring(2, id.length - 1) : id.toLowerCase();

        const channel = /^[\d+]{17,}$/.test(channelIdOrName)
            ? cache.channels.get(snowflakeToBigint(channelIdOrName))
            : cache.channels.find((channel) => channel.name === channelIdOrName && channel.guildId === guild.id);

        if (channel?.type !== ChannelTypes.GuildCategory) return;

        return channel;
    },
});
