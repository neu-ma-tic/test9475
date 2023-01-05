import { Message } from "discord.js";
import { IExecute } from "../../interfaces/IEvents";

export const name: string = "message";
export const execute: IExecute = async (client, message: Message) => {
  if (!message.content.startsWith(client.prefix) || message.author.bot) return;

  const args = message.content.slice(client.prefix.length).split(/ +/);

  const cmd = args.shift().toLowerCase();

  const command =
    client.commands.get(cmd) ||
    client.commands.find((a) => a.aliases && a.aliases.includes(cmd));

  if (command) {
    command.execute(client, message, args);
  } else {
    message.channel.send(
      "Unknown command! Speak to the developers if you think you found a bug!"
    );
  }
};
