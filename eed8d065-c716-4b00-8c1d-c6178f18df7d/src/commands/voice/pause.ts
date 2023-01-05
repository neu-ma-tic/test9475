import { bot } from '../../../cache.ts';
import { DiscordenoInteractionResponse, sendInteractionResponse, snowflakeToBigint } from '../../../deps.ts';
import { createCommand } from '../../utils/helpers.ts';
import { checkIfUserInMusicChannel } from '../../utils/voice.ts';

createCommand({
    name: 'pause',
    guildOnly: true,
    slash: {
        enabled: true,
        guild: true,
        execute: async (message) => {
            var payload;

            const player = bot.lavadenoManager.players.get(message.guildId!.toString());

            if (!player) {
                payload = `The bot is not playing right now`;
            } else {
                await player.pause();
                payload = 'Paused!';
            }

            var data: DiscordenoInteractionResponse = {
                data: { content: payload },
                type: 4,
            };
            return sendInteractionResponse(snowflakeToBigint(message.id), message.token, data);
        },
    },
    async execute(message) {
        const player = bot.lavadenoManager.players.get(message.guildId.toString());

        if (!player || !(await checkIfUserInMusicChannel(message, player))) {
            return message.reply(`The bot is not playing right now`);
        }

        await player.pause();

        return message.reply(`The music has now been paused.`);
    },
});
