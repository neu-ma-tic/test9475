import { IExecute } from "../interfaces/ICommands";

export const name = "leave";
export const description = "leave the channel";
export const execute: IExecute = async (client, message, args) => {
  const voiceChannel = message.member.voice.channel;

  if (!voiceChannel)
    return message.channel.send("You need to be in a voice channel sir");

  voiceChannel.leave();
  await message.channel.send("Im leaving");
};
