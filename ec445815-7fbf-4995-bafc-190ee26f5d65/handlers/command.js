const { readdirSync } = require('fs');
const ascii = require('ascii-table');
let table = new ascii("commands");

table.setHeading('Command', 'Load status');

module.exports = (bot) => {


    readdirSync(`./commands/`).forEach(dir => {
        const commands = readdirSync(`./commands/${dir}/`).filter(file => file.endsWith('js'));

        for (let file of commands) {
            let pull = require(`../commands/${dir}/${file}`);

            if (pull.name) {
                bot.commands.set(pull.name, pull);
                table.addRow(file, `✅`);

            } else {
                table.addRow(file, `❌`);
                continue;
            }

            if (pull.aliases) pull.aliases.forEach(alias => bot.aliases.set(alias, pull.name));


        }
    });
    console.log(table.toString());

};