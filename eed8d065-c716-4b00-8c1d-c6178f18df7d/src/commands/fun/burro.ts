import { createCommand } from '../../utils/helpers.ts';

createCommand({
    name: 'burro',
    guildOnly: false,
    execute(message) {
        return message.reply('burro és tu');
    },
});
