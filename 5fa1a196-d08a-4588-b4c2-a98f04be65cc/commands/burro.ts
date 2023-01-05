import { IExecute } from "../interfaces/ICommands";

export const name = "burro";
export const description = "";
export const execute:IExecute = async (client, message, args) => {
    message.channel.send('burro és tu!');
}