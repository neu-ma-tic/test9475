const { MessageEmbed } = require("discord.js");

module.exports = {
  name: "helpm",
  aliases: ["hm"],
  description: "کامند مشترک موزیک و چت را نشان میدهد",
  execute(message) {
    let commands = message.client.commands.array();

    let helpEmbed = new MessageEmbed()
      .setTitle(`${message.client.user.username} Help`)
      .setDescription("__**یه نگاه به کامند های موزیک من بنداز**__")
      .setColor("RED")
      .setTimestamp();
      
    commands.forEach((cmd) => {
      helpEmbed.addField(
        `**${message.client.prefix}${cmd.name} ${cmd.aliases ? `(${cmd.aliases})` : ""}**`,
        `${cmd.description}`,
        true
      );
    });

    helpEmbed.setTimestamp();

    return message.channel.send(helpEmbed).catch(console.error);
  }
};
