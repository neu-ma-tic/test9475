const client = require("../index");

client.on("ready", () =>
  console.log(
    `Logged in as ${client.user.username}. Ready on ${client.guilds.cache.size} servers, for a total of ${client.users.cache.size} users`
  )
);
