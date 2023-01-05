import { Client, Collection } from "discord.js";
import dotenv = require("dotenv");
import { Bot } from "./Bot";
import keepAlive from "./server";
dotenv.config();

new Bot().init();

console.log("I'm alive");

keepAlive();

// var commands = new Collection();
// var events = new Collection();

// ["command_handler", "event_handler"].forEach((handler) => {
//   require(`./handlers/${handler}`)(client);
// });
