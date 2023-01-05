const { Client, Collection } = require("discord.js");

const fs = require("fs");
const client = new Client({
    intents: 32767,
});
module.exports = client;

// Global Variables
client.commands = new Collection();
client.aliases = new Collection();
client.categories = fs.readdirSync("./commands/");
client.config = require("./config.json");

// Initializing the project
require("./handler")(client);

client.login(client.config.token);