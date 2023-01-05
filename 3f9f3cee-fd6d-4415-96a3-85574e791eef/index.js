const { Client, Collection, MessageEmbed } = require("discord.js");

const client = new Client({
  partials: [
    "GUILDS",
    "GUILD_MESSAGES",
    "GUILD_MEMBERS",
    "GUILD_PRESENCES",
    "GUILD_MESSAGE_REACTIONS",
    "CHANNEL",
  ],
  intents: [32767],
});
module.exports = client;

// Global Variables
client.commands = new Collection();
client.slashCommands = new Collection();
client.config = require("./config.json");

// Initializing the project
require("./handler")(client);

client.on("ready", () => {
  console.log("Ready!");
  setInterval(() => {
    const aA = ["dark-mc.xyz", "VIDEO ON YOUTUBE", "Omelan BlazePxly", `&help`];

    const aS = aA[Math.floor(Math.random() * aA.length)];

    const aB = ["LISTENING", "LISTENING", "LISTENING", "LISTENING"];
    const aD = aB[Math.floor(Math.random() * aA.length)];
    client.user.setActivity(aS, { type: aD });
  }, 5000);
});

client.login(client.config.token);
