module.exports = async (client) =>{
    const welcomeChannelId = config.WELCOMER.welcomeChannel_ID; // welcome chanel where to welcome user
    const introChannelId = config.WELCOMER.introChannel_ID; // introduction for server
    const memberRoleId = config.WELCOMER.memberRole_ID; // member role id
    

    client.on('guildMemberAdd', (member) => {
        if (member.bot) return;
        let channel = member.guild.channels.cache.get(welcomeChannelId);
        let memberRole = member.guild.roles.cache.get(memberRoleId);
        const message = `Здравей <@${member.id}>, Добре дошъл в ${member.guild.name}! За да се запознаете с нашият сървър, проверете ${member.guild.channels.cache.get(introChannelId).toString()}! Надяваме се да ви хареса тук и да се забавлявате!`;

        // member.addRole(memberRole) // this will add the role to that member!
        // Add the role!
        // member.roles.add(memberRole).catch(console.error);
        member.roles.add(memberRole);

        channel.send(message);
    });
}