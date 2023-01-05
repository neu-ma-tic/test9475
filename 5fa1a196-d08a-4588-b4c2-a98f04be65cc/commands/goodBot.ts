import { MessageAttachment } from "discord.js";
import { IExecute } from "../interfaces/ICommands";

export const name = "goodbot";
export const description = "Good bot";
export const execute:IExecute = async (client, message, args) => {
    //message.channel.send('pong!');
    const attachment = new MessageAttachment('./images/bot_icon.gif');
    message.channel.send('', attachment);
}