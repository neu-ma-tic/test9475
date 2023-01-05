import { MessageEmbed, TextChannel } from "discord.js";
import { IExecute } from "../interfaces/ICommands";

export const execute: IExecute = async (client, message, args) => {
  try {
    const id = message.guild.channels.cache.find(
      (channel) => channel.name === "suggestions"
    ).id;

    let messageArgs = args.join(" ");

    const embed = new MessageEmbed()
      .setColor("FADF2E")
      .setAuthor(
        message.author.tag,
        message.author.displayAvatarURL({ dynamic: true })
      )
      .setDescription(messageArgs);

    const channel = client.channels.cache.get(id);
    (channel as TextChannel)
      .send(embed)
      .then((msg) => {
        msg.react("👍");
        msg.react("👎");
        message.delete();
      })
      .catch((err) => {
        throw err;
      });
  } catch (error) {
    return message.channel.send("create a suggestion channel");
  }
};

export const name = "suggestions";
export const description = "do suggestions";
export const alias = "suggest";
