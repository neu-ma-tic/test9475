const Discord = require("discord.js");
const { MessageEmbed } = require("discord.js");

module.exports = {
  name: "clear",
  aliases: ["purge", "clearmsgs"],
  description: "Clear Your Messages!",
  usage: "Clear <Message Amount>",
  run: async (message, args) => {
    //Start
    message.delete();
    if (!message.member.hasPermission("MANAGE_MESSAGES"))
      return message.channel.send(
        "you don't have permission to use this command!"
      );

    if (!args[0])
      return message.channel.send("please give a message amount!");

    if (isNaN(args[0]))
      return message.channel.send("give a number of messages to delete!");

    if (args[0] < 4)
      return message.channel.send(
        "you can delete ${args[0]} by your self!"
      );

    if (args[0] > 100)
      return message.channel.send(
        "i can\'t Delete ${args[0]} due to discord's limits!"
      );

    //End
  }
};