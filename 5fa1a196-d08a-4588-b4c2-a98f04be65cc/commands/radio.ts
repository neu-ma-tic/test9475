import ytdl from "ytdl-core";
import { IExecute } from "../interfaces/ICommands";
import data from "../radios.json";

import { Radio } from "./radios";

import stringSimilarity from "string-similarity";

export const name = "radio";
export const description = "radio stuff";
export const aliases = ["r"];

export const execute: IExecute = async (client, message, args: string[]) => {
  const voiceChannel = message.member.voice.channel;

  if (!voiceChannel)
    return message.channel.send("Join a voice channel you dweeb");

  const permissions = voiceChannel.permissionsFor(message.client.user);

  if (!permissions.has("CONNECT") || !permissions.has("SPEAK"))
    return message.channel.send("you don't have permissions");

  if (!args.length) return message.channel.send("Wrong number of args");

  // console.log(video.url);

  let radio: Radio;

  let closestMatch: string = args.join(" ").toUpperCase();

  var radiolink: string;

  if (isLink(args[0]))
    // Let user radio for links
    radiolink = args[0];
  else {
    var keys = [];
    for (var k in data) keys.push(k);

    closestMatch = stringSimilarity.findBestMatch(closestMatch, keys).bestMatch
      .target;
    radio = data[closestMatch];
    radiolink = radio.link;
  }
  // break;
  // }

  if (radio) {
    const connection = await voiceChannel.join();
    connection
      .play(radiolink, { seek: 0, volume: 1, bitrate: "auto" })
      .on("finish", () => {
        voiceChannel.leave();
      });

    await message.reply(`Radio ${closestMatch} is playing`);
  }
};

const isLink = (link: string) => {
  var pattern = new RegExp(
    "^(https?:\\/\\/)?" + // protocol
      "((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" + // domain name
      "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
      "(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" + // port and path
      "(\\?[;&a-z\\d%_.~+=-]*)?" + // query string
      "(\\#[-a-z\\d_]*)?$",
    "i"
  ); // fragment locator

  return !!pattern.test(link);
};
