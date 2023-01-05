// slash command 등록
// 커맨드 등록할 때 처음만 실행하면 됨.

const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');
const { clientId, token } = require(__dirname + '/config.json');
const fs = require('fs');

const commands = [];
const commandFiles = fs.readdirSync(__dirname + '/commands')
    .filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
    const command = require(__dirname + `/commands/${file}`);
    commands.push(command.data.toJSON());
}

const rest = new REST({ version: '9' }).setToken(token);

(async () => { // commands[]를 이용해 slash command 등록
    try {
        console.log('Started refreshing application (/) commands.');

        await rest.put(
            Routes.applicationCommands(clientId),
            { body: commands }, // commands
        );

        console.log('Successfully reloaded application (/) commands.');

        // console.log(commands); // commands[] 확인
    } catch (error) {
        console.error(error);
    }
})();