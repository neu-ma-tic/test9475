import { DiscordenoInteractionResponse, sendInteractionResponse, snowflakeToBigint } from '../../../deps.ts';
import { Embed } from '../../utils/Embed.ts';
import { createCommand } from '../../utils/helpers.ts';

createCommand({
    name: 'radios',
    guildOnly: true,
    slash: {
        enabled: true,
        guild: true,
        execute: (message) => {
            const payload = new Embed();
            let str = '';

            const radios = JSON.parse(Deno.readTextFileSync('./src/commands/voice/radios.json'));

            payload.setTitle('Radio Stations');
            for (let radio in radios) {
                str += radio + '\n';
            }

            payload.setDescription(str);

            var data: DiscordenoInteractionResponse = {
                data: { embeds: [payload] },
                type: 4,
            };
            return sendInteractionResponse(snowflakeToBigint(message.id), message.token, data);
        },
    },
    execute(message) {
        const radios = JSON.parse(Deno.readTextFileSync('./src/commands/voice/radios.json'));
        var str = '';

        for (let radio in radios) {
            str += radio + '\n';
        }
        message.reply(str);
    },
});
