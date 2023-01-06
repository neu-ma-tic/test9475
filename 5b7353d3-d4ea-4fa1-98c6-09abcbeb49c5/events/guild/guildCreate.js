const { PREFIX } = process.env;

module.exports = async (client, guild) => {
  let channel = guild.channels.cache.find(
    channel =>
    channel.type === "text" &&
    channel.permissionsFor(guild.me).has("SEND_MESSAGES")
  );
  channel.send(`**__Thank you for adding me!__**
  • **My prefix here is \`${PREFIX}\`**
  • **You can see a list of commands by typing \`${PREFIX}help\`**
  • **You can change my prefix with \`${PREFIX}config <New Prefix>\`**
  • **If you need help, feel free to join our support server, just type \`${PREFIX}invite\`**`);
}