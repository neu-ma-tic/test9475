import { bot } from '../../../cache.ts';

import { createCommand } from '../../utils/helpers.ts';
import { addPlaylistToQueue, addSoundToQueue, validURL } from '../../utils/voice.ts';

createCommand({
    name: 'play',
    aliases: ['p'],
    guildOnly: true,
    // slash: {
    //   enabled: true,
    //   guild: true,
    //   options: [
    //     {
    //       required: true,
    //       name: "commands/play:USER_NAME",
    //       description: "commands/play:USER_DESCRIPTION",
    //       type: DiscordApplicationCommandOptionTypes.String,
    //     },
    //   ],
    //   execute: (data, member) => {

    //     var payload;

    //     const arg = data.data?.options?.[0];

    //     if(arg?.type !== DiscordApplicationCommandOptionTypes.String)
    //       return;

    //     const player = bot.lavadenoManager.players.get(
    //       data.guildId!.toString(),
    //       );

    //       var toSend: DiscordenoInteractionResponse = {
    //         data: { content: payload },
    //         type: 4,
    //       };

    //     if (!player || !player.connected) {

    //       const guild = cache.guilds.get(BigInt(data.guildId));
    //       const voiceState = guild!.voiceStates.get(BigInt(member?.id));
    //       if (!voiceState?.channelId) {
    //         payload = (`You first need to join a voice channel!`);
    //       }
    //       else{

    //       if (player) {
    //         player.connect(voiceState.channelId.toString(), {
    //           selfDeaf: true,
    //         });
    //       } else {
    //         const newPlayer = bot.lavadenoManager.create(
    //           data.guildId!.toString(),
    //         );
    //         newPlayer.connect(voiceState.channelId.toString(), {
    //           selfDeaf: true,
    //         });
    //       }

    //       payload = (`Successfully joined the channel!`);
    //     }

    //     return sendInteractionResponse(
    //       snowflakeToBigint(data.id),
    //       data.token,
    //       toSend,
    //       );
    //     }
    //   },
    // },
    arguments: [{ type: '...strings', name: 'query', required: true }],
    async execute(message, args) {
        const player = bot.lavadenoManager.players.get(message.guildId.toString());

        if (!player || !player.connected) {
            const voiceState = message.guild?.voiceStates.get(message.authorId);
            if (!voiceState?.channelId) {
                return message.reply(`You first need to join a voice channel!`);
            }

            if (player) {
                player.connect(voiceState.channelId.toString(), {
                    selfDeaf: true,
                });
            } else {
                const newPlayer = bot.lavadenoManager.create(message.guildId.toString());
                newPlayer.connect(voiceState.channelId.toString(), {
                    selfDeaf: true,
                });
            }

            await message.reply(`Successfully joined the channel!`);
        }

        const trackSearch = validURL(args.query) ? args.query : `ytsearch:${args.query}`;
        const result = await bot.lavadenoManager.search(trackSearch);

        switch (result.loadType) {
            case 'TRACK_LOADED':
            case 'SEARCH_RESULT': {
                return addSoundToQueue(message, result.tracks[0]);
            }
            case 'PLAYLIST_LOADED': {
                return addPlaylistToQueue(message, result.playlistInfo!.name, result.tracks);
            }
            default:
                return message.reply(`Could not find any song with that name!`);
        }
    },
});
