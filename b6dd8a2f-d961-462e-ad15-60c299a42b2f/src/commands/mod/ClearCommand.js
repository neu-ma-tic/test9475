const BaseCommand = require('../../utils/structures/BaseCommand');

module.exports = class ClearCommand extends BaseCommand {
  constructor() {
    super('clear', 'mod', ['purge', 'prune', 'delete'], 'clear [number]');
  }

  run(client, message, args) {
    //check if the user has permissions to manage messages and is an admin
    if(!message.member.hasPermission(["MANAGE_MESSAGES", "ADMINISTRATOR"])) return message.channel.send("You do not have permission to use this command!");
      
    //check if they included a number of messages to delete
    if(!args[0]) return message.reply('You forgot to include a number!');
    message.channel.bulkDelete(args[0]); //bulk delete the specified number of messages
  }
}