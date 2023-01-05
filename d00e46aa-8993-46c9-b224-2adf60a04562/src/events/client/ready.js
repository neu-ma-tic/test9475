const chalk = require("chalk");
const settings = require("../../assets/settings.json");
const { updateMembers, updatePlayerCount, updateChangeLog} = require("../../utils/Intervals");

module.exports.run = async (client) => {
    client.logger.log(`Connected into ${chalk.redBright(client.user.tag)}`)
    client.initializeSlash(settings.guildID);

    updateMembers(client);
    updatePlayerCount(client);
    updateChangeLog(client);
}