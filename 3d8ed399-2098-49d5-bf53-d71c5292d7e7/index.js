const ownerOnly = ["727608168041021591", "702237464219353118"];
const {Client, MessageEmbed} = require("discord.js");
const {get} = require("snekfetch");
const bot = new Client();
const prefix = "/";

bot.login("ODMzMzE5MTczNzE4Mjc4MTU0.YHwm9Q.IS6I3cxudQa8mINzCU7Gmif65ms");

bot.on("ready", () => {
  console.clear();
  console.log(`${bot.user.tag} : ${new Date(Date.now() + 7200000).toUTCString()}`); // for winter time use: + 3600000
});

bot.on("message", (message) => {
  if(message.author.bot || !message.content.startsWith(prefix)) return;

  let args = message.content.slice(prefix.length).trim().split(/ +/g);
  let path = `./commands/${args.shift().toLowerCase()}.js`;

  if(!require("fs").existsSync(path)) return;

  const command = require(path);

  if(command.ownerOnly && ownerOnly.includes(message.author.id)) command.run(bot, message, args);
  if(!command.ownerOnly || command.ownerOnly) command.run(bot, message, args);
  else message.channel.send(new(require("discord.js")).RichEmbed().setColor(0xff073a).setTitle("Alert!").setDescription("User was not permitted to use that command."));
});

bot.on("message", message => {
  if(message.content === "prefix") {message.delete();message.channel.send(new(require("discord.js")).MessageEmbed().setColor(0xbc13fe).setTitle(prefix).setTimestamp());
  } else if(message.content.startsWith("amazin")) {
    message.delete();
    message.channel.send("https://cdn.glitch.com/faf005d6-da2c-495f-b3be-cd426065a2db%2Famazin.mp4?v=1616249583420");
  } else if(message.content === "pog") {
    message.channel.send("champ") 
  } else if(message.content === "sonic") {
    message.delete();
    message.channel.send("https://cdn.glitch.com/b01c0bcf-bf5c-4127-a650-113edcdc310f%2Fy2mate.com_-_Sonic_Plays_Rocket_League_1080p_1.mp4?v=1618832916613");
  };
});

bot.on("messageDelete", (m) => {
  if(m.author.bot) return;
  let x = require(`${__dirname}/snipe.json`);
  x[m.channel.id] = [m.author.id, m.content, m.attachments.first() ? m.attachments.first().proxyURL : undefined];
  require("fs").writeFileSync(`${__dirname}/snipe.json`, JSON.stringify(x, null, 2));
});