import { botId, cache, DiscordActivityTypes, editBotStatus, upsertSlashCommands } from '../../deps.ts';
import { Command } from '../types/commands.ts';
import { Milliseconds } from '../utils/constants/time.ts';
import { translate } from '../utils/i18next.ts';
import { registerTasks } from './../utils/task_helper.ts';
import { sweepInactiveGuildsCache } from './dispatch_requirements.ts';
import { bot } from '../../cache.ts';
import { log } from '../utils/logger.ts';
import { sendWebhook, snowflakeToBigint } from '../../deps.ts';
import { cron } from 'https://deno.land/x/deno_cron/cron.ts';
import { configs } from '../../configs.ts';
import axiod from 'https://deno.land/x/axiod/mod.ts';

bot.eventHandlers.ready = async function () {
    editBotStatus({
        status: 'dnd',
        activities: [
            {
                name: 'Looking for Gohan 👀',
                type: DiscordActivityTypes.Game,
                createdAt: Date.now(),
            },
        ],
    });

    log.info(`Loaded ${bot.arguments.size} Argument(s)`);
    log.info(`Loaded ${bot.commands.size} Command(s)`);
    log.info(`Loaded ${Object.keys(bot.eventHandlers).length} Event(s)`);
    log.info(`Loaded ${bot.inhibitors.size} Inhibitor(s)`);
    log.info(`Loaded ${bot.monitors.size} Monitor(s)`);
    log.info(`Loaded ${bot.tasks.size} Task(s)`);

    // Special task which should only run every hour AFTER STARTUP
    setInterval(sweepInactiveGuildsCache, Milliseconds.HOUR);

    registerTasks();

    await bot.lavadenoManager.init(botId.toString());

    bot.fullyReady = true;

    log.info(`[READY] Bot is online and ready in ${cache.guilds.size} guild(s)!`);

    log.info(`Preparing Slash Commands...`);

    const globalCommands = [];
    // deno-lint-ignore no-explicit-any
    const perGuildCommands: Command<any>[] = [];

    for (const command of bot.commands.values()) {
        if (!command.slash?.enabled) continue;

        // THIS COMMAND NEEDS SOME SLASH COMMAND STUFF
        if (command.slash.global) globalCommands.push(command.slash);
        if (command.slash.guild) perGuildCommands.push(command);
    }

    // GLOBAL COMMANDS CAN TAKE 1 HOUR TO UPDATE IN DISCORD
    if (globalCommands.length) {
        log.info(`Updating Global Slash Commands... Any changes will take up to 1 hour to update on discord.`);
        await upsertSlashCommands(globalCommands).catch(log.info);
    }

    // GUILD COMMANDS WILL UPDATE INSTANTLY
    await Promise.all(
        cache.guilds.map(async (guild) => {
            await upsertSlashCommands(
                perGuildCommands.map((cmd) => {
                    // USER OPTED TO USE BASIC VERSION ONLY
                    if (cmd.slash?.advanced === false) {
                        return {
                            name: cmd.name,
                            description: cmd.description || 'No description available.',
                            options: cmd.slash?.options,
                        };
                    }

                    // ADVANCED VERSION WILL ALLOW TRANSLATION
                    const name = translate(guild.id, `commands/${cmd.name}:SLASH_NAME`);
                    const description = translate(guild.id, `commands/${cmd.name}:SLASH_DESCRIPTION`);

                    return {
                        name: name === 'SLASH_NAME' ? cmd.name : name,
                        description:
                            description === 'SLASH_DESCRIPTION'
                                ? cmd.description || 'No description available.'
                                : description,
                        options: cmd.slash?.options?.map((option) => {
                            const optionName = translate(guild.id, option.name);
                            const optionDescription = translate(guild.id, option.description);

                            return {
                                ...option,
                                name: optionName,
                                description: optionDescription || 'No description available.',
                            };
                        }),
                    };
                }),
                guild.id
            ).catch(log.warn);
            log.info(`Updated Guild ${guild.name} (${guild.id}) Slash Commands...`);
        })
    );

    log.info(`[READY] Slash Commands loaded successfully!`);

    log.info(`[READY] Slash Commands loaded successfully!`);

    log.info('Loading the bois');

    function sendMufasa() {
        const fridays = [
            'https://www.youtube.com/watch?v=kL62pCZ4I3k', //yakuza
            ' https://www.youtube.com/watch?v=1AnG04qnLqI', //mufasa
            'https://www.youtube.com/watch?v=UjJY8X7d9ZY', // mufasa
            'https://cdn.discordapp.com/attachments/381520882608373761/824981469591634020/friday.mp4', //big boi tommy
            'https://cdn.discordapp.com/attachments/381520882608373761/913769811526418442/VID_20560324_124823_231.mp4',
        ];
        sendWebhook(snowflakeToBigint(configs.webhooks.mufasa.id!), configs.webhooks.mufasa.token!, {
            content: `It's friday! ${fridays[Math.floor(Math.random() * fridays.length)]}`,
        });
    }

    async function sendAOTD() {
        const { data } = await axiod.get('https://1001albumsgenerator.com/api/v1/groups/pepegas-do-preco-certo');

        let stuff = data.currentAlbum;
        let album: string = `https://open.spotify.com/album/${stuff.spotifyId}`;
        sendWebhook(snowflakeToBigint(configs.webhooks.AOTD.id!), configs.webhooks.AOTD.token!, {
            content: `@here Today's album of the day is ${stuff.name} by ${stuff.artists[0].name}! ${album}`,
        });

        sendWebhook(snowflakeToBigint(configs.webhooks.AOTD.id!), configs.webhooks.AOTD.token!, {
            content: `Don't forget to rate the previous one!`,
        });
    }

    cron('00 00 13 * * 5', () => {
        sendMufasa();
    });

    cron('00 00 8 * * *', () => {
        sendAOTD();
    });

    log.info('[READY] Bois are ready!');
};
