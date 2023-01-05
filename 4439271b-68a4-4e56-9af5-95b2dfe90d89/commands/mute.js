module.exports = {
  name: 'mute',
  description: 'e',
  execute(message, args) {
    let target = message.mentions.users.first();
    let muteRole = message.guild.roles.cache.find(role => role.name === 'muted');
    let memberTarget = message.guild.members.cache.get(target.id);
    if (!message.member.hasPermission("ADMINISTRATOR")) return message.channel.send("Invalid Permissions")
    if (!message.member.hasPermission("KICK_MEMBERS")) return message.channel.send("You dont have permissions!")
    if (!message.mentions.users.size) {
			return message.reply('you need to tag a user in order to mute them!');
		}
    if (!args[1]) {
      memberTarget.roles.remove(mainRole.id);
      memberTarget.roles.add(muteRole.id);
      message.channel.send(`<@${memberTarget.user.id}> has been muted`);
      return
      }
  }
};