import { bot } from '../../cache.ts';
import { configs } from '../../configs.ts';
import { snowflakeToBigint } from '../../deps.ts';
import { Embed } from '../utils/Embed.ts';
import { sendEmbed } from '../utils/helpers.ts';

bot.eventHandlers.discordLog = function (error: Error) {
    // Your code goes here

    const embed = new Embed().setDescription(['```ts', error, '```'].join('\n')).setTimestamp();

    return sendEmbed(snowflakeToBigint(configs.channelIDs.errorChannelID), embed);
};
