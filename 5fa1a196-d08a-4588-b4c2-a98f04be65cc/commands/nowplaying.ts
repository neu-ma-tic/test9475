import axios from "axios";
import stringSimilarity from "string-similarity";
import { IExecute } from "../interfaces/ICommands";
import data from "../radios.json";

export const name = "nowplaying";
export const description = "get what is playing";
export const aliases = ["np"];
export const execute: IExecute = async (client, message, args) => {
  //message.channel.send('pong!');

  let closestMatch = args.join(" ").toUpperCase();
  var keys = [];
  for (var k in data) keys.push(k);

  closestMatch = stringSimilarity.findBestMatch(closestMatch, keys).bestMatch
    .target;

  let radio = data[closestMatch];
  let radioId = radio.id;

  const url: string = `https://prod.radio-api.net/stations/now-playing?stationIds=${radioId}`;

  try {
    const response = await axios.get(url);
    message.channel.send(
      `Right now on ${closestMatch} it's playing ${response.data[0].title}`
    );
  } catch (exception) {
    process.stderr.write(`ERROR received from ${url}: ${exception}\n`);
  }
};
