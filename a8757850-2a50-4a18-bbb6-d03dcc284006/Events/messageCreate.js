const Event = require("../Structres/Event.js");

module.exports = new Event("messageCreate", (client, message) => {
  if (message.author.bot) return;

  if (!message.content.startsWith(client.prefix)) return;

  const args = message.content.substring(client.prefix.length).split(/ +/);

  const command = client.commands.find(cmd => cmd.name == args[0].toLowerCase()) || client.aliases.get(args[0].toLowerCase());

  if (!command) return message.reply(`${args[0]} 不是有效的指令`);

  const permission = message.member.permissions.has(command.permission, true);

  if (!permission) return message.reply(
    `你沒有\`${command.permission}\`的權限執行這個指令`
  );

  command.run(message, args, client);
});