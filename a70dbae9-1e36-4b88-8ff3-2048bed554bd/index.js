const { Client } = require("discord.js");
const client = new Client({intents: 32767});
const { Token } = require("./config.json");

require("./Handlers/Events")(client);

client.login(Token);