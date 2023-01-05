module.exports = {
    name: 'unmute',
    description: "This unmutes a member",
    execute(message, args){
        const target = message.mentions.users.first();
        if(target){
          if (!message.member.hasPermission("ADMINISTRATOR")) return message.channel.send("Invalid Permissions")
          if (!message.member.hasPermission("KICK_MEMBERS")) return message.channel.send("You dont have permissions!")
           
            let muteRole = message.guild.roles.cache.find(role => role.name === 'muted');
 
            let memberTarget= message.guild.members.cache.get(target.id);
 
            memberTarget.roles.remove(muteRole.id);
            memberTarget.roles.add(mainRole.id);
            message.channel.send(`<@${memberTarget.user.id}> has been unmuted`);
        } else{
            message.channel.send('Cant find that member!');
        }
    }
}