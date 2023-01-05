import { updateEventHandlers } from '../../../deps.ts';
import { createCommand, fileLoader, importDirectory } from '../../utils/helpers.ts';
import { PermissionLevels } from '../../types/commands.ts';
import { clearTasks, registerTasks } from '../../utils/task_helper.ts';
import { reloadLang } from '../../utils/i18next.ts';
import { bot } from '../../../cache.ts';

const folderPaths = new Map([
    ['arguments', './src/arguments'],
    ['commands', './src/commands'],
    ['events', './src/events'],
    ['inhibitors', './src/inhibitors'],
    ['monitors', './src/monitors'],
    ['tasks', './src/tasks'],
    ['perms', './src/permissionLevels'],
    ['languages', './src/languages'],
]);

createCommand({
    name: `reload`,
    permissionLevels: [PermissionLevels.BOT_OWNER],
    botChannelPermissions: ['SEND_MESSAGES'],
    arguments: [
        {
            name: 'folder',
            type: 'string',
            literals: ['arguments', 'commands', 'events', 'inhibitors', 'monitors', 'tasks', 'languages'],
            required: false,
        },
    ] as const,
    execute: async function (message, args) {
        // Reload a specific folder
        if (args.folder) {
            const path = folderPaths.get(args.folder);
            if (!path) {
                return message.reply('The folder you provided did not have a path available.');
            }

            if (args.folder === 'tasks') {
                clearTasks();
                await importDirectory(Deno.realPathSync(path));
                await fileLoader();
                registerTasks();
                return message.reply(`The **${args.folder}** have been reloaded.`);
            }

            if (args.folder === 'languages') {
                await reloadLang();
                return message.reply(`The **${args.folder}** have been reloaded.`);
            }

            await importDirectory(Deno.realPathSync(path));
            await fileLoader();
            return message.reply(`The **${args.folder}** have been reloaded.`);
        }

        // Reloads the main folders:
        clearTasks();
        await Promise.all([...folderPaths.values()].map((path) => importDirectory(Deno.realPathSync(path))));
        await fileLoader();
        registerTasks();
        // Reload the languages
        await reloadLang();
        // Updates the events in the library
        updateEventHandlers(bot.eventHandlers);

        return message.reply('Reloaded everything.');
    },
});
