import { IExecute } from "../interfaces/ICommands";
import { readFile } from "fs";
import data from "../radios.json";

export interface Radio {
  name: string;
  id: string;
  link: string;
}
interface Radios {
  radios: Radio[];
}

export const name = "radios";
export const description = "List all radios";
export const execute: IExecute = async (client, message, args) => {
  const da = data;
  var str = "";

  for (let radio in da) {
    str += radio + "\n";
  }
  message.channel.send(str);
};
