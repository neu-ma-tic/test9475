module.exports = async (client, delay) =>{
    const guild = client.guilds.cache.get(config.STATS.guild_ID); // server id
    setInterval(() =>{
        const memberCount = guild.memberCount;
        const userCount = guild.members.cache.filter((m) => !m.user.bot).size;
        // const botsCount = guild.members.cache.filter(member => member.user.bot).size;   

        const totalUsersChannel = guild.channels.cache.get(config.STATS.totalUsersChannel_ID);
        const usersChannel = guild.channels.cache.get(config.STATS.usersChannel_ID);
        // const botsChannel = guild.channels.cache.get(config.STATS.botsChannel_ID);

        totalUsersChannel.setName(`All Members: ${memberCount.toLocaleString()}`);
        usersChannel.setName(`Members: ${userCount.toLocaleString()}`);
        // botsChannel.setName(`Bots: ${botsCount.toLocaleString()}`);

    }, delay);
}