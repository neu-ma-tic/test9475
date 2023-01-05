import {
    cache,
    DiscordApplicationCommandOptionTypes,
    DiscordenoInteractionResponse,
    DiscordenoMessage,
    sendInteractionResponse,
    snowflakeToBigint,
} from '../../../deps.ts';
import { createCommand } from '../../utils/helpers.ts';
import { sortWordByMinDistance } from 'https://deno.land/x/damerau_levenshtein@v0.1.0/mod.ts';
import { bot } from '../../../cache.ts';
import { addSoundToQueue, addSoundToQueueInteraction } from '../../utils/voice.ts';
import { addPlaylistToQueue } from '../../utils/voice.ts';
import { Radios, Try } from '../../utils/constants/radios.ts';
import { byString } from '../../utils/object_by_string.ts';

createCommand({
    name: 'radio',
    aliases: ['r'],
    guildOnly: true,
    slash: {
        enabled: true,
        guild: true,
        options: [
            {
                required: true,
                name: 'radio_name',
                description: 'radio_desc',
                type: DiscordApplicationCommandOptionTypes.String,
                choices: Try,
            },
        ],
        execute: async (message, member) => {
            let payload = '';

            const guild = cache.guilds.get(snowflakeToBigint(message.guildId!));

            if (typeof guild === 'undefined' || typeof member === 'undefined') {
                return;
            }
            const userID = member.id;

            const voiceState = guild.voiceStates.get(userID);

            if (!voiceState?.channelId) {
                payload = 'Join a voice channel you dweeb';
            }
            let radio: IRadio | null = null;

            let closestMatch = '';

            if (message.data && message.data.options && message.data.options.length > 0) {
                const { value } = message.data!.options![0];

                closestMatch = value;
            }

            var radiolink: string;

            var keys = [];
            for (var k in Radios) keys.push(k);
            closestMatch = sortWordByMinDistance(closestMatch, keys)[0].compared;
            radio = byString(Radios, closestMatch);
            radiolink = radio!.link;

            if (radio) {
                // Get player from map (Might not exist)
                const player = bot.lavadenoManager.players.get(message.guildId!.toString());

                if (player) {
                    player.connect(voiceState!.channelId!.toString(), {
                        selfDeaf: true,
                    });
                } else {
                    const newPlayer = bot.lavadenoManager.create(message.guildId!.toString());
                    newPlayer.connect(voiceState!.channelId!.toString(), {
                        selfDeaf: true,
                    });
                }
            }

            const result = await bot.lavadenoManager.search(radiolink);

            switch (result.loadType) {
                case 'TRACK_LOADED':
                case 'SEARCH_RESULT': {
                    payload = result.tracks[0].info.title;
                    addSoundToQueueInteraction(message, result.tracks[0]);
                    break;
                }

                default:
                    payload = `Could not find any song with that name!`;
            }

            var test: DiscordenoInteractionResponse = {
                data: { content: payload },
                type: 4,
            };
            return sendInteractionResponse(snowflakeToBigint(message.id), message.token, test);
        },
    },
    arguments: [{ type: '...strings', name: 'query', required: true }],
    userServerPermissions: ['SPEAK', 'CONNECT'],

    async execute(message: DiscordenoMessage, args) {
        const voiceState = message.guild?.voiceStates.get(message.authorId);

        if (!voiceState?.channelId) {
            return message.reply('Join a voice channel you dweeb');
        }

        let radio: IRadio | null = null;

        let closestMatch: string = args.query.toUpperCase();

        var radiolink: string;

        var keys = [];
        for (var k in Radios) keys.push(k);

        closestMatch = sortWordByMinDistance(closestMatch, keys)[0].string;
        radio = byString(Radios, closestMatch);
        radiolink = radio!.link;

        message.reply(radiolink);

        // break;
        // }

        if (radio) {
            // Get player from map (Might not exist)
            const player = bot.lavadenoManager.players.get(message.guildId.toString());

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

        const result = await bot.lavadenoManager.search(radiolink);

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

export interface IRadio {
    name: string;
    id: string;
    link: string;
}
interface IRadios {
    radios: IRadio[];
}
