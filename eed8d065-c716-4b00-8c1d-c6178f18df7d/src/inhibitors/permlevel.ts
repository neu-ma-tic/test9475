import { bot } from '../../cache.ts';

bot.inhibitors.set('permlevel', async function (message, command) {
    // This command doesnt require a perm level so allow the command.
    if (!command.permissionLevels?.length) return false;

    // If a custom function was provided
    if (typeof command.permissionLevels === 'function') {
        // The function returns a boolean.
        const allowed = await command.permissionLevels(message, command);
        // We reverse the boolean to allow the command if they meet the perm level.
        return !allowed;
    }

    // If an array of perm levels was provided
    for (const permlevel of command.permissionLevels) {
        const hasPermission = bot.permissionLevels.get(permlevel);
        if (!hasPermission) continue;

        const allowed = await hasPermission(message, command);
        // If this user has one of the allowed perm level, the loop is canceled and command is allowed.
        if (allowed) return false;
    }

    // None of the perm levels were met. So cancel the command
    return true;
});
