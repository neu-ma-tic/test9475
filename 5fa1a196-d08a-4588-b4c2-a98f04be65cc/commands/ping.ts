import { IExecute } from "../interfaces/ICommands";

export const name = "ping";
export const description = "ping pong";
export const execute:IExecute = async (client, message, args) => {
    message.channel.send('pong!');
}
