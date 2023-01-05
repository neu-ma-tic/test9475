const { Client, Collection } = require("discord.js");
const fs = require("fs");

function setup() {
    const client = new Client({
        disableEveryone: false
    });

    // Config
    client.config = module.exports = {
        owner: '929933466819252284',
        prefix: 'm-',
        defaultGuildSettings: {
            prefix: 'm-',
            welcomeMessage: {
                enabled: false,
                welcomeMessage: "Welcome **{{member}}** to **{{server}}**!",
                channelID: '1019094385486471188'
            },
            soundboardRole: "Soundboard DJ",
            modRole: "Moderator",
            adminRole: "Co-owner",
            logChannel: "⌠😂⌡logs"
        }
    }

    client.mongoose = require("./utils/mongoose");
    require("./utils/mongooseFunctions")(client);

    client.commands = new Collection();
    client.aliases = new Collection();

    client.categories = fs.readdirSync("./commands/");

    ["commands", "events"].forEach(handler => {
        require(`./handlers/${handler}`)(client);
    });

    module.exports.client = client;
    module.exports.commands = client.commands;

    // Map with guilds playing music ?
    client.musicGuilds = new Map();

    // Map with guilds playing soundboard effects
    client.soundboardGuilds = new Map();

    // Map with members playing games
    client.gameMembers = new Map();

    // Set of people currently stealing emojis in a server
    // `${guildID}${userID}
    client.activeEmojiStealing = new Set();

    // Set of people we are currently waiting on a response from so that we can ignore any further commands until we get it
    client.waitingResponse = new Set();

    // Map with invites for each guild
    client.guildInvites = new Map();

    client.mongoose.init();

    client.databaseCache = {};
    client.databaseCache.settings = new Collection();
    client.databaseCache.events = new Collection();
    client.databaseCache.roleMenus = new Collection();
    client.databaseCache.soundEffects = new Collection();
    client.databaseCache.memberSoundEffects = new Collection();

    client.login('MTAxOTg3NDcwOTgzMzI3MzQxNQ.Gcun8b.AEiUtL6afNzHOEjYVJ0McrH9OWb6wgnkRo5Xaw').catch((err) => console.error(err));

    // Start dashboard server
    require("./dashboard/server");

    // Keep Heroku dyno alive
    setInterval(() => {
        require("node-fetch")(process.env.DASHBOARD_URL);
        console.log("Reviving");
    }, 25 * 60 * 1000);
}

// if there is an unhandledRejection, log them
process.on("unhandledRejection", (err) => {
    console.error("unhandledRejection:\n", err);
});

setup();