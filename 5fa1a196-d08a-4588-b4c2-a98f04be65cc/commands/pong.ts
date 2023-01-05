import { IExecute } from "../interfaces/ICommands";

export const name = "pong";
export const description = "pong ping";
export const execute:IExecute = async (client, message, args) => {
    message.channel.send('ping!');
}