module.exports.run = async (client, guild) => {
    client.logger.log(`${guild.name}(${guild.id}) just removed me!`);
    return;
}