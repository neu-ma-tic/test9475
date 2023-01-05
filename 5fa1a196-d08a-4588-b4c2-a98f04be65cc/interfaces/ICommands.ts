import { Client, Message } from "discord.js";

export interface IExecute {
  (client: Client, message: Message, args: any);
}

export interface ICommand {
  name: string;
  description: string;
  aliases?: string[];
  execute: IExecute;
}
